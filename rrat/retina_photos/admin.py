from django.contrib import admin
from .models import RetinaPhoto as RetinaPhotoModel

class RetinaPhotoAdmin(admin.ModelAdmin):
    # What shows up on the admin panel list
    list_display = ("id",)

    # what shows up when you edit or add a patient via the admin panel
    fields = ("id",)

    
# Register your models here.
admin.site.register(RetinaPhotoModel, RetinaPhotoAdmin)
