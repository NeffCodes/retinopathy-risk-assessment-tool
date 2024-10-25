from django.shortcuts import get_object_or_404
from .models import RetinaPhoto as RetinaPhotoModel
from .forms import RetinaForm
from .utils import upload_cloudinary_retina
from patients.cloudinary_helpers import destroy_cloudinary_image
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
    Hard deletes the image from both the database and from cloudinary.
    """
    
    # retrieve photo from the local db
    db_image = get_object_or_404(RetinaPhotoModel, id=id)


    # get cloudinary pubilc ID
    cloudinary_public_id = db_image.cloudinary_public_id
    print(f"Public ID: {cloudinary_public_id}")

    if db_image.status == StatusChoices.UNPROCESSED: 
        # if image has not been sent to the wizard, hard delete
        try:
            # delete from cloudinary
            cloud = destroy_cloudinary_image(cloudinary_public_id)

            if cloud.get('result') == 'not found':
                print("Image not found in Cloudinary. Check the public ID and folder structure.")

            if cloud.get('result') == "error":
                print("Error trying to delete the image on cloudinary:")
                print(cloud.message)
            
            # delete from local db if successful
            if cloud.get('result') == 'ok':
                db_image.delete()
                print("Retina photo deleted")
        except Exception as e:
            print(f"Error trying to delete image in Cloudinary: {e}")
    else:
        # if processed, soft delete?
        # will need to add a new field to the model for hidden
        # set hidden to true
        pass