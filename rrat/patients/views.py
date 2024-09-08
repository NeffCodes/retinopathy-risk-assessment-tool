from django.shortcuts import render
from .models import Patient
from .forms import PatientForm

def patients_list(request):
  """
  [CREATE, READ]
  Patient page to view a full list of patients which also has a section to add new patients.
  """
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

def view_patient(request, id):
  """
  [READ]
  Patient page to view patient details.
  """
  patient = Patient.objects.get(id=id)
  return render(request, 'patients/view_patient.html', { 'patient': patient })

def update_patient(request, id):
  """
  [UPDATE]
  Patient page to change patient details
  """
  context = {}
  return render(request, 'patients/update_patient.html')
