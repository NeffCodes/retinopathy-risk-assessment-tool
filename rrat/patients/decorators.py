from django.http import Http404
from .models import Patient as PatientModel

def check_patient_hidden(view_func):
    """
    @decorator checks to see if the patient is hidden and redirects to 404 if true.

    TODO: Update 404 redirect to actual 404 page once created.
    """
    def wrapper(request, *args, **kwargs):
        try:
            patient = PatientModel.objects.get(id = kwargs["id"])
        except PatientModel.DoesNotExist:
        #  if not patient
            raise Http404('Patient not found')
    
        if patient.hidden:
            raise Http404('Patient does not exist')
    
        return view_func(request, *args, **kwargs)
    return wrapper