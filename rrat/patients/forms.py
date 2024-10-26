from django import forms
from .models import Patient as PatientModel

form_custom_class = "block w-full rounded-md border-0 py-2 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-500 sm:text-sm sm:leading-6"

# create a ModelForm
class PatientForm(forms.ModelForm):

	class Meta:
		model = PatientModel
		fields = [
			'first_name',
			'last_name',
			'date_of_birth',
			'avatar',
		]
		widgets = {
			'first_name': forms.TextInput(attrs={
				'class': form_custom_class,
			}),
			'last_name': forms.TextInput(attrs={
				'class': form_custom_class,
			}),
			'date_of_birth': forms.TextInput(attrs={
				'type': 'date',
				'class': form_custom_class,
			}),
			'avatar': forms.ClearableFileInput(attrs={
				'class': form_custom_class,
			}),
		}
