from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient as PatientModel
from .forms import PatientForm
from .decorators import check_patient_hidden
from .cloudinary_helpers import *
from retina_photos.views import form_add_new_retina_photo

def patients_list(request):
  """
  Patient page to view a full list of patients which also has a section to add new patients.
  """
  context = {}

  # create an object of the patient form to create a new patient
  form = PatientForm(request.POST or None, request.FILES or None)

  # check if form data is valid
  if form.is_valid():
    # get data from form instance
    patient_instance = form.save(commit=False) # don't save the form yet

    # If instance has an image
    if request.FILES.get('avatar'):
      image_file = request.FILES['avatar']

      # Set the new public ID 
      set_cloudinary_public_id(patient_instance)

      # Upload the image to Cloudinary with transformations
      result = upload_cloudinary_avatar(image_file, patient_instance.cloudinary_public_id)

      # Set the image URL to the patient instance
      patient_instance.avatar = result['url']

    # Save patient
    patient_instance.save()
    return redirect("patients:list")
  else:
    print(form.errors)

  # get all patients in db that are not hidden
  patients = PatientModel.objects.all().exclude(hidden=True).order_by('last_name')

  # set context
  context['form'] = form
  context['patients'] = patients

  return render(request, 'patients/patients_list.html', context)

@check_patient_hidden
def view_patient(request, id):
  """
  Patient page to view patient details.
  """
  patient = PatientModel.objects.get(id=id)
  form = form_add_new_retina_photo(request=request, patient=patient)

  context = {}
  context["form"] = form
  context["patient"] = patient
  return render(request, 'patients/view_patient.html', context)

@check_patient_hidden
def update_patient(request, id):
  """
  Patient page to change patient details
  """
  context = {}

  # fetch the object related to the provided patient id
  patient = get_object_or_404(PatientModel, id=id)

  # pass the patient object as an instance into the form
  form = PatientForm(request.POST or None, request.FILES or None, instance = patient)


  # validate and save data from the form and redirect to patient_view
  if form.is_valid():
    # get data from form instance
    patient_instance = form.save(commit=False) # don't save the form yet

    # If instance has an image, update image info
    if request.FILES.get('avatar'):
      image_file = request.FILES['avatar']

      # Remove old image
      cloud = destroy_cloudinary_image(patient_instance.cloudinary_public_id)
                
      if cloud.get('result') == 'not found':
          print("Image not found in Cloudinary. Check the public ID and folder structure.")

      if cloud.get('result') == "error":
          print("Error trying to delete the image on cloudinary:")
          print(cloud.message)

      if cloud.get('result') == 'ok':
        # Set a new public ID 
        set_cloudinary_public_id(patient_instance)

        # Upload the new image to Cloudinary
        result = upload_cloudinary_avatar(image_file,patient_instance.cloudinary_public_id)

        # Set the image URL to the patient instance
        patient_instance.avatar = result['url']

    # Save patient
    patient_instance.save()
    return redirect("patients:patient_view", id)
  else:
    print(form.errors)

  # set context
  context["form"] = form
  context["patient"] = patient

  return render(request, 'patients/update_patient.html', context)

@check_patient_hidden
def delete_patient(request, id):
  """
  Soft deletes patient from database by marking the hidden field as true.
  """
  context = {}

  # retrieve patient
  patient = get_object_or_404(PatientModel, id = id)

  # if confirmation modal approved
  if request.method == "POST":
    # mark as hidden and return to list
    patient.hidden = True

    # update the db and redirect to patient list dashboard
    patient.save(update_fields=["hidden"])
    return redirect("patients:list")
  
  context["patient"] = patient
  return render(request, "patients/delete_patient.html", context)