from django.shortcuts import render
from .models import Patient
from .forms import PatientForm

def patients_list(request):
  context = {}
  
  # create an object of the form
  form = PatientForm(request.POST or None, request.FILES or None)

  # check if form data is valid
  if form.is_valid():
      # save the form data to model
      form.save()

  # get all patients in db
  patients = Patient.objects.all().order_by('last_name')

  # set context
  context['form'] = form
  context['patients'] = patients

  return render(request, 'patients/patients_list.html', context)

def patient_page(request, id):
  patient = Patient.objects.get(id=id)
  return render(request, 'patients/patient_page.html', { 'patient': patient })