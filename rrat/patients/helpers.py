from django.utils.timezone import now


def set_cloudinary_public_id(patient_instance):
    """
    This function will set the cloudinary public id for a patient instance. 
    String will include the current time.
    Returns nothing.
    """
    date_str = now().strftime("%Y-%m-%d--%H:%M")
    
    custom_public_id = f"{patient_instance.last_name}-{patient_instance.first_name[0]}-{str(patient_instance.id)}-{date_str}"

    patient_instance.cloudinary_public_id = custom_public_id