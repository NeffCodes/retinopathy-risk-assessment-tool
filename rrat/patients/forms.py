from django import forms
from .models import Patient as PatientModel

# create a ModelForm
class PatientForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = PatientModel
		fields = "__all__"
