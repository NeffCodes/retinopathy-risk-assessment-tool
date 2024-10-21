from django.utils.timezone import now
import cloudinary.uploader

def set_cloudinary_public_id(patient_instance):
    """
    This function will set the cloudinary public id for a patient instance. 
    String will include the current time.
    Returns nothing.
    """
    date_str = now().strftime("%Y-%m-%d--%H:%M")
    
    custom_public_id = f"{patient_instance.last_name}-{patient_instance.first_name[0]}-{str(patient_instance.id)}-{date_str}"

    patient_instance.cloudinary_public_id = custom_public_id

def destroy_cloudinary_image(public_id):
    """
    This function will delete an image from cloudinary database by public id
    """
    # Full path should be constructed only if needed
    try:
        cloud = cloudinary.uploader.destroy(f"rrat/avatars/{public_id}")
    except Exception:
        print(Exception)

    print(f"= Cloudinary Destroy Response: {public_id} {cloud}")
    return cloud

def upload_cloudinary_avatar(image_file, public_id, folder= 'rrat/avatars'):
    try:
        cloud = cloudinary.uploader.upload(
            image_file,
            public_id=public_id,
            transformation=[
                {"width": 300, "height": 300, "crop": "fill", "quality": "auto", "gravity": "auto"}
            ],
            folder=folder,
        )
        return cloud
    except Exception:
        print(Exception)

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

