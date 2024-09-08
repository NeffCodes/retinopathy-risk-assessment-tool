from django.shortcuts import render
from .models import Patient

# Create your views here.
def patients_list(request):
  patients = Patient.objects.all().order_by('last_name')
  return render(request, 'patients/patients_list.html', { 'patients': patients })

def patient_page(request, id):
  patient = Patient.objects.get(id=id)
  return render(request, 'patients/patient_page.html', { 'patient': patient })