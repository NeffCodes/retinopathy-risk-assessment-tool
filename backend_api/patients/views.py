from django.shortcuts import render, get_object_or_404
from .models import Patient

def profile(request, id):
    patient = get_object_or_404(Patient, id=id)
    return render(request, 'patients/profile.html', {'patient': patient})
