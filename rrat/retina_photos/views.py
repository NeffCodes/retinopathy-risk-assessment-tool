import requests
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.http import Http404, HttpResponse
from .models import RetinaPhoto as RetinaPhotoModel
from .forms import RetinaForm
from .utils import (
    upload_cloudinary_retina,
    hard_delete_image_from_all_db,
    get_prognosis_choice,
)
from .choices import StatusChoices
from django.contrib import messages
import json


def upload_retina_photo(request, patient):
    """
    Logic to add a new retina photo to Cloudinary db.
    Handles POST/Redirect/GET to prevent duplicate submissions on page refresh.
    """
    if request.method == "POST":
        retinaForm = RetinaForm(request.POST, request.FILES)

        # Check if form data is valid
        if retinaForm.is_valid():
            # Get data from form instance
            image_instance = retinaForm.save(commit=False)
            image_instance.patient = patient

            # If instance has an image
            if request.FILES.get("image"):
                image_file = request.FILES["image"]

                # Upload image to Cloudinary with transformations
                result = upload_cloudinary_retina(image_file, image_instance)

                # Set the image URL to the patient instance
                image_instance.image = result["url"]

                # Save the image instance
                image_instance.save()

            # Redirect to the patient view after successful submission
            return redirect("patients:patient_view", id=patient.id)

    # If not POST, return an empty form
    return RetinaForm()


def delete_retina_photo(request, id):
    """
    Hard deletes the image from both the database and from cloudinary if image has not been processed. Otherwise will soft delete and mark the image as "hidden".
    """
    # retrieve photo from the local db
    retina_image = get_object_or_404(RetinaPhotoModel, id=id)

    # get patient ID
    patient_id = retina_image.patient.id

    # if confirm deletion
    if request.method == "POST":
        # if image has not been sent to the wizard, hard delete
        if retina_image.status == StatusChoices.UNPROCESSED:
            hard_delete_image_from_all_db(retina_image)
        else:
            # if processed or pending, mark as hidden for soft delete
            retina_image.hidden = True
            retina_image.save(update_fields=["hidden"])
        return redirect("patients:patient_view", id=patient_id)

    # render the confirmation page
    context = {}
    context["patient_id"] = patient_id
    context["photo"] = retina_image
    return render(request, "retina_photos/photo_confirm_delete.html", context)


def analyze_retina_photo(request, id):
    # Retrieve the image from the database
    image = get_object_or_404(RetinaPhotoModel, id=id)
    patient_id = image.patient.id

    # Verify image has not been processed so
    # that it won't be analyzed multiple times
    if image.status == StatusChoices.DONE or image.status == StatusChoices.PENDING:
        messages.info(request, "Image has already been analyzed.")
        return HttpResponse(status=204)

    try:

        api_url = settings.AGENT_URL + "/analyze"
        image_file = image.image
        data = {"image_url": image_file.url, "image_id": image.cloudinary_public_id}

        response = requests.post(api_url, json=data)
        response.raise_for_status()
        response_data = response.json()
        response_result = response_data.get("result")
    except Exception as e:
        messages.error(request, f"Failed to analyze image: {e}")
        print(f"Failed to analyze image: {e}")
        raise Http404("Failed to analyze image.")

    # Update the status and prognosis of the image
    prognosis_choice = get_prognosis_choice(response_result)
    image.prognosis = prognosis_choice
    image.status = StatusChoices.DONE
    image.save()

    print("\n+============================")
    print(f"Retina photo analyzed: {image}")
    print(f"Response: {response_result}")
    print(f"Prognosis: {prognosis_choice}")
    print(f"Status: {image.status}")
    print("+============================\n")

    messages.success(request, "Image successfully analyzed.")
    return redirect("patients:patient_view", id=patient_id)
