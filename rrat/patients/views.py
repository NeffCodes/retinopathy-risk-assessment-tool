from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient as PatientModel
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
  patients = PatientModel.objects.all().order_by('last_name')

  # set context
  context['form'] = form
  context['patients'] = patients

  return render(request, 'patients/patients_list.html', context)

def view_patient(request, id):
  """
  [READ]
  Patient page to view patient details.
  """
  patient = PatientModel.objects.get(id=id)
  return render(request, 'patients/view_patient.html', { 'patient': patient })

def update_patient(request, id):
  """
  [UPDATE]
  Patient page to change patient details
  """
  context = {}

  # fetch the object related to the provided patient id
  patient = get_object_or_404(PatientModel, id=id)

  # pass the patient object as an instance into the form
  form = PatientForm(request.POST or None, instance = patient)

  # validate and save data from the form and redirect to patient_view
  if form.is_valid():
    form.save()
    return redirect("patients:patient_view", id)

  # set context
  context["form"] = form
  context["patient"] = patient

  return render(request, 'patients/update_patient.html', context)

def delete_patient(request, id):
  """
  [DELETE]
  Removes patient from database.
  """
  context = {}

  patient = get_object_or_404(PatientModel, id = id)

  # delete patient and redirect to dashboard
  if request.method == "POST":
    patient.delete()
    return redirect("patients:list")
  
  context["patient"] = patient
  return render(request, "patients/delete_patient.html", context)