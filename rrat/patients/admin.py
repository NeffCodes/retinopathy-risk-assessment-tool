from django.contrib import admin
from .models import Patient as PatientModel
from .cloudinary_helpers import destroy_cloudinary_image

class PatientModelAdmin(admin.ModelAdmin):
    actions = ['delete_model']
    
    readonly_fields = ("cloudinary_public_id",)

    # What shows up on the admin panel list
    list_display = ("id","first_name","last_name","hidden","date_created","date_updated", 'user')

    # what shows up when you edit or add a patient via the admin panel
    fields = ("first_name","last_name","date_of_birth","hidden", "user", "avatar", "cloudinary_public_id")


    """
    Custom admin delete method that allows us to also delete image from Cloudinary Database. 
    NOTE: this does not allow deleting from the queryset, will need a different function if we want that capablility.
    Source: https://stackoverflow.com/a/56165570
    """
    def delete_model(self, request, obj):
        print(f"===== Deleting Patient: {obj}")

        # Verify if patient has profile picture
        if obj.avatar:
            try:
                # Ensure that obj.cloudinary_public_id contains only the ID, not the path
                public_id = obj.cloudinary_public_id
                print(f"Public ID: {public_id}")

                cloud = destroy_cloudinary_image(public_id)
                            
                if cloud.get('result') == 'not found':
                    print("Image not found in Cloudinary. Check the public ID and folder structure.")

                if cloud.get('result') == "error":
                    print("Error trying to delete the image on cloudinary:")
                    print(cloud.message)

                # If image is successfully removed, delete patient object from database.
                if cloud.get('result') == 'ok':
                    obj.delete()
                    print('Patient deleted')
            except Exception as e:
                print(f"Error trying to delete image in Cloudinary: {e}")
        else:
            print("Patient does not have a profile picture")
            obj.delete()
            print('Patient deleted')

        print(f"===== end of deleting")

# Register your models here.
admin.site.register(PatientModel, PatientModelAdmin)
