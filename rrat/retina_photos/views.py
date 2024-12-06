import requests
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.http import JsonResponse
from .models import RetinaPhoto as RetinaPhotoModel
from .forms import RetinaForm
from .utils import upload_cloudinary_retina, hard_delete_image_from_all_db, get_prognosis_choice
from .choices import StatusChoices
from patients.models import Patien as PatientModel
from django.contrib import messages



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
            if request.FILES.get('image'):
                image_file = request.FILES['image']

                # Upload image to Cloudinary with transformations
                result = upload_cloudinary_retina(image_file, image_instance)

                # Set the image URL to the patient instance
                image_instance.image = result['url']

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
    return render(request, 'retina_photos/photo_confirm_delete.html', context)

def analyze_retina_photo(request, id):
    # Retrieve the image from the database
    image = get_object_or_404(RetinaPhotoModel, id=id)
    
    # Verify image has not been processed so that it won't be analyzed multiple times
    if image.status == StatusChoices.DONE or image.status == StatusChoices.PENDING:
        messages.error(request, "Image has already been analyzed.")
        return redirect("patients:patient_view", id=image.patient.id)

    api_url = settings.AGENT_URL + '/analyze'
    print(f"API URL: {api_url}")

    # get patient ID
    patient_id = image.patient.id
    patient = PatientModel.objects.get(id=patient_id)


    try:
        image.status = StatusChoices.PENDING
        image.save()

        response = requests.post(api_url)
        response.raise_for_status()
        response_data = response.json()
        response_result = response_data.get('result')
    except Exception as e:
        return JsonResponse({'error': f'API request failed: {e}'}, status=500)
    
    # Update the status and prognosis of the image
    prognosis_choice = get_prognosis_choice(response_result)
    image.prognosis = prognosis_choice
    image.status = StatusChoices.DONE
    image.save()

    print(f"Retina photo analyzed: {image}")
    print(f"Prognosis: {prognosis_choice}")
    print(f"Status: {image.status}")
    print(f"Response: {response_result}")
    print('+============================')
    print('/n')
    # return JsonResponse({"message": "Image analyzed successfully."})
    return redirect("patients:patient_view", id=patient_id)