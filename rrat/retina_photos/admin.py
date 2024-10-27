from django.contrib import admin
from .models import RetinaPhoto as RetinaPhotoModel
import datetime
import cloudinary.uploader
from .utils import hard_delete_image_from_all_db


class RetinaPhotoAdmin(admin.ModelAdmin):
    readonly_fields = ["cloudinary_public_id", 'image_tag']

    # What shows up on the admin panel list
    list_display = ("patient_name", "position", "cloudinary_public_id", "date_created")

    # what shows up when you edit or add a patient via the admin panel
    fields = ("patient", "image", "position", "cloudinary_public_id", "image_tag")

    # Pull the name of the patient through the foreign key relationship
    def patient_name(self, obj):
        return obj.patient.full_name
    patient_name.short_description = 'Patient Name'

    # This is a custom save model to allow us to upload images via the admin panel
    def save_model(self, request, obj, form, change):
        # Check if this is a new object (not updating an existing one)
        if not change:
            position = form.cleaned_data.get('position', 'default')  
            date_created = datetime.datetime.now().strftime('%Y-%m-%d')  
            
            # Save once to generate an ID if needed
            obj.save()  

            # Generate Public ID
            custom_public_id = f"{position}--{obj.id}--{date_created}"
            obj.cloudinary_public_id = custom_public_id

            # Update the public ID in cloudinary
            old_id = obj.image.public_id
            id_path = f"rrat/retina_photos/{custom_public_id}"
            if(old_id and old_id != custom_public_id):
                try:
                    cloudinary.uploader.rename(old_id,id_path)
                    obj.image.public_id = custom_public_id
                except Exception as e:
                    print(f"\n+===== Image public ID rename error: {e}\n")
            
            # Rename the display name in Cloudinary
            result = cloudinary.uploader.explicit(
                id_path,
                type="upload",
                display_name=custom_public_id
            )
            
            # Set the new url to the obj
            obj.image = result['url']

        # Save the object again with the updated image URL
        super().save_model(request, obj, form, change)
    
    # Set fields to read only after they have been added
    def get_readonly_fields(self, request, obj=None):
        if obj:  # This means the object already exists (it's being edited)
            return self.readonly_fields + ['image', 'position']  
        return self.readonly_fields  # When adding a new object, don't make the image field read-only

    def delete_model(self, request, obj):
        """
        Custom admin delete method that allows us to also delete the retina image from Cloudinary Database from the admin panel. 
        """ 
        print(f"===== Deleting Retina Photo: {obj}")

        if obj.image:
            try:
                hard_delete_image_from_all_db(obj)
                
            except Exception as e:
                print(f"Error trying to delete image from admin panel: {e}")

    def delete_queryset(self, request, queryset):
        """
        Custom admin delete method that allows us to also delete the selected retina image(s) from Cloudinary Database from the admin panel overview page. 
        """ 
        print("+===========================")
        print(queryset)

        for img_obj in queryset:
            try:
                hard_delete_image_from_all_db(img_obj)
            except Exception as e:
                print(f"Error trying to delete image from admin panel: {e}")
        queryset.delete()
        print("Queryset Deleted")
        return super().delete_queryset(request, queryset)


# Register your models here.
admin.site.register(RetinaPhotoModel, RetinaPhotoAdmin)
