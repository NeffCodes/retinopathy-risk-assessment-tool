from django.utils.timezone import now
import cloudinary.uploader
from .choices import PrognosisChoices

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
    """
    This function will transform and upload a retina photo to cloudinary
    """
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

def destroy_cloudinary_retina_image(public_id):
    """
    This function will delete an image from cloudinary database by public id
    """
    # Full path should be constructed only if needed
    try:
        cloud = cloudinary.uploader.destroy(f"rrat/retina_photos/{public_id}")
    except Exception:
        print(Exception)

    print(f"= Cloudinary Destroy Response: {public_id} {cloud}")
    return cloud

def hard_delete_image_from_all_db(image_obj):
    """
    This function trys to delete an image from both cloudinary and local db
    """
    # get cloudinary pubilc ID
    cloudinary_public_id = image_obj.cloudinary_public_id
    print(f"Public ID: {cloudinary_public_id}")

    try:
        # delete from cloudinary
        cloud = destroy_cloudinary_retina_image(cloudinary_public_id)

        if cloud.get('result') == 'not found':
            print("Image not found in Cloudinary. Check the public ID and folder structure.")

        if cloud.get('result') == "error":
            print("Error trying to delete the image on cloudinary:")
            print(cloud.message)

        
        # delete from local db if successful
        if cloud.get('result') == 'ok':
            image_obj.delete()
            print("Retina photo deleted")

        return cloud

    except Exception as e:
        print(f"Error trying to delete image in Cloudinary: {e}")

def get_prognosis_choice(api_result: int) -> str:
    API_RESULT_MAPPING = {
        0:PrognosisChoices.NORMAL,
        1:PrognosisChoices.MILD,
        2:PrognosisChoices.MODERATE,
        3:PrognosisChoices.SEVERE,
        4:PrognosisChoices.PROLIFERATIVE
    }

    return API_RESULT_MAPPING[api_result]