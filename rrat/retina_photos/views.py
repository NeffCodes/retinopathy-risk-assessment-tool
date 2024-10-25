from django.shortcuts import get_object_or_404, redirect, render
from .models import RetinaPhoto as RetinaPhotoModel
from .forms import RetinaForm
from .utils import upload_cloudinary_retina, hard_delete_image_from_all_db
from .choices import StatusChoices


def form_add_new_retina_photo(request, patient):
    """
    Logic to add new retina photo to cloudinary db
    Returns retina form context
    """
    retinaForm = RetinaForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if retinaForm.is_valid():
        # get data from form instance
        image_instance = retinaForm.save(commit=False) # Don't save the form yet

        # Set the patient id
        image_instance.patient = patient

        # If instance has an image
        if request.FILES.get('image'):
            image_file = request.FILES['image']

            # Upload image to Cloudinary with transformations
            result = upload_cloudinary_retina(image_file, image_instance)

            # Set the image URL to the patient instance
            image_instance.image = result['url']

            image_instance.save()
        else:
            print(retinaForm.errors)
    return retinaForm

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