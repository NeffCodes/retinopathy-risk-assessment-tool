from django.contrib import admin
from .models import Patient as PatientModel
import cloudinary.uploader

class PatientModelAdmin(admin.ModelAdmin):
    actions = ['delete_model']
    
    # What shows up on the admin panel list
    list_display = ("id","first_name","last_name","hidden","date_created","date_updated", 'avatar')

    # what shows up when you edit or add a patient via the admin panel
    fields = ("first_name","last_name","date_of_birth","hidden", "avatar")

    """
    Custom admin delete method that allows us to also delete image from Cloudinary Database. 
    NOTE: this does not allow deleting from the queryset, will need a different function if we want that capablility.
    Source: https://stackoverflow.com/a/56165570
    """
    def delete_model(self, request, obj):
        print(f"===== Deleting Patient: {obj}")

        try:
            # Ensure that obj.cloudinary_public_id contains only the ID, not the path
            public_id = obj.cloudinary_public_id
            print(f"Public ID: {public_id}")

            # Full path should be constructed only if needed
            cloud = cloudinary.uploader.destroy(f"rrat/avatars/{public_id}")
            print(f"Cloudinary Response: {cloud}")
            
            if cloud.get('result') == 'not found':
                print("Image not found in Cloudinary. Check the public ID and folder structure.")
            
            # If image is successfully removed, delete patient object from database.
            if cloud.get('result') == 'ok':
                obj.delete()
        except Exception as e:
            print(f"Error trying to delete image in Cloudinary: {e}")

        print(f"===== end of deleting")

# Register your models here.
admin.site.register(PatientModel, PatientModelAdmin)