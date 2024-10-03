from django.forms import ModelForm      
from cloudinary.forms import CloudinaryFileField      
from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

    image = CloudinaryFileField(
        attrs = { 'style': "margin-top: 30px" }, 
        options = { 
            'tags': "directly_uploaded",
            'crop': 'limit', 'width': 1000, 'height': 1000,
            'eager': [{ 'crop': 'fill', 'width': 150, 'height': 100 }]
        })