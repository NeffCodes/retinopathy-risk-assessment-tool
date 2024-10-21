from django import forms
from .models import RetinaPhoto as PhotoModel

form_custom_class = "block w-full rounded-md border-0 py-2 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-500 sm:text-sm sm:leading-6"

class RetinaForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = [
            "position",
            "image"
        ]

        widgets = {
            "position": forms.Select(attrs={"class":form_custom_class}),
            "image": forms.ClearableFileInput(attrs={
				'class': form_custom_class,
			}),
        }