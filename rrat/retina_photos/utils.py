from django.utils.timezone import now
import cloudinary.uploader

def set_retina_cloudinary_public_id(image_instance):
    """
    This function will set the cloudinary public id for a retina image instance. 
    String will include the current time.
    Returns nothing.
    """
    date_str = now().strftime("%Y-%m-%d--%H:%M")
    
    custom_public_id = f"{image_instance.position}--{str(image_instance.id)}--{date_str}"

    image_instance.cloudinary_public_id = custom_public_id
    return image_instance.cloudinary_public_id

def upload_cloudinary_retina(image_file, image_instance, folder= 'rrat/retina_photos'):
    public_id = set_retina_cloudinary_public_id(image_instance)

    try:
        cloud = cloudinary.uploader.upload(
            file=image_file,
            public_id=public_id,
            transformation=[
                {"width": 256, "height": 256, "crop": "fill", "quality": "auto", "gravity": "auto"}
            ],
            folder=folder,
        )
        print("+===== Image successfully uploaded")
        return cloud
    except Exception as e:
        print(f"\n+===== Image upload error: {e}\n")

