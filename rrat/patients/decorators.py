from django.http import Http404
from .models import Patient as PatientModel
from django.contrib import messages
from django.shortcuts import redirect

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

def check_permission_to_view_patient(view_func):
    """
    Decorator to check if the user has permission to view a patient.
    """
    def wrapper(request, *args, **kwargs):
        # Get the patient based on the ID passed in the URL
        try:
            patient = PatientModel.objects.get(id=kwargs["id"])
        except PatientModel.DoesNotExist:
            raise Http404('Patient not found')
        
        # Verify that the logged-in user is the patient owner
        if patient.user != request.user:
            print(f"=== {request.user} does not own {patient}")
            messages.error(request, "Sorry, you do not have permission to view this patient.")
            return redirect("patients:list")
        
        # If permission check passes, call the view function
        return view_func(request, *args, **kwargs)
    return wrapper