from .forms import RetinaForm
from .utils import upload_cloudinary_retina

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
    pass