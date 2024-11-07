from django.shortcuts import render, get_object_or_404, redirect
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
=======
from django.contrib.auth.decorators import login_required
from django.contrib import messages
>>>>>>> b3bbbc5f42648fc7a3cd5d923688293eb0e65cae
from .models import Patient as PatientModel
from .forms import PatientForm
from .decorators import check_patient_hidden
from .cloudinary_helpers import *
from retina_photos.views import upload_retina_photo

<<<<<<< HEAD
@login_required(login_url='login')  # Protect the patients_list view
def patients_list(request):
    """
    Patient page to view a full list of patients which also has a section to add new patients.
    """
    context = {}

    # Create an object of the patient form to create a new patient
    form = PatientForm(request.POST or None, request.FILES or None)

    # Check if form data is valid
    if form.is_valid():
        # Get data from form instance
        patient_instance = form.save(commit=False)  # Don't save the form yet

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

    # Get all patients in db that are not hidden
    patients = PatientModel.objects.all().exclude(hidden=True).order_by('last_name')

    # Set context
=======
@login_required(login_url='users:login')  # Protect the patients_list view
def patients_list(request):
    """
    Patient page to view a full list of patients, with an option to add new patients.
    """
    context = {}

    # Create an instance of the patient form to create a new patient
    form = PatientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        # Create a patient instance without saving yet
        patient_instance = form.save(commit=False)

        # Handle avatar image upload
        if request.FILES.get('avatar'):
            image_file = request.FILES['avatar']

            # Set the new public ID
            set_cloudinary_public_id(patient_instance)

            # Attempt to upload the image to Cloudinary
            result = upload_cloudinary_avatar(image_file, patient_instance.cloudinary_public_id)

            if result.get('url'):
                patient_instance.avatar = result['url']
            else:
                messages.error(request, "Failed to upload avatar to Cloudinary.")

        # Save patient instance to the database
        patient_instance.save()
        messages.success(request, "Patient added successfully!")
        return redirect("patients:list")  # Ensure the redirect uses the correct namespaced URL
    else:
        messages.error(request, "Please correct the errors below.")
        print(form.errors)

    # Fetch all non-hidden patients from the database
    patients = PatientModel.objects.all().exclude(hidden=True).order_by('last_name')

    # Set context for rendering
>>>>>>> b3bbbc5f42648fc7a3cd5d923688293eb0e65cae
    context['form'] = form
    context['patients'] = patients

    return render(request, 'patients/patients_list.html', context)

<<<<<<< HEAD

@login_required(login_url='login')  # Protect the view_patient view
=======
@login_required(login_url='users:login')  # Protect the view_patient view
>>>>>>> b3bbbc5f42648fc7a3cd5d923688293eb0e65cae
@check_patient_hidden
def view_patient(request, id):
    """
    Patient page to view patient details.
    """
    patient = get_object_or_404(PatientModel, id=id)
<<<<<<< HEAD
    return render(request, 'patients/view_patient.html', {'patient': patient})
  """
  Patient page to view patient details.
  """
  patient = PatientModel.objects.get(id=id)
  form = upload_retina_photo(request=request, patient=patient)
=======
>>>>>>> b3bbbc5f42648fc7a3cd5d923688293eb0e65cae

    # Handle retina photo upload
    form = upload_retina_photo(request=request, patient=patient)

<<<<<<< HEAD
@login_required(login_url='login')  # Protect the update_patient view
@check_patient_hidden
def update_patient(request, id):
    """
    Patient page to change patient details
    """
    context = {}

    # fetch the object related to the provided patient id
    patient = get_object_or_404(PatientModel, id=id)

    # pass the patient object as an instance into the form
    form = PatientForm(request.POST or None, request.FILES or None, instance=patient)

    # validate and save data from the form and redirect to patient_view
    if form.is_valid():
        # get data from form instance
        patient_instance = form.save(commit=False)  # don't save the form yet

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

<<<<<<< HEAD
                # Upload the new image to Cloudinary
                result = upload_cloudinary_avatar(image_file, patient_instance.cloudinary_public_id, 'rrat/avatars')
=======
        # Upload the new image to Cloudinary
        result = upload_cloudinary_avatar(image_file,patient_instance.cloudinary_public_id)
>>>>>>> main

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

@login_required(login_url='login')  # Protect the delete_patient view
=======
    context = {
        "form": form,
        "patient": patient
    }

    return render(request, 'patients/view_patient.html', context)

@login_required(login_url='users:login')  # Protect the update_patient view
@check_patient_hidden
def update_patient(request, id):
    """
    Patient page to change patient details.
    """
    patient = get_object_or_404(PatientModel, id=id)
    context = {}

    # Initialize the form with the patient instance
    form = PatientForm(request.POST or None, request.FILES or None, instance=patient)

    if form.is_valid():
        patient_instance = form.save(commit=False)  # Don't save yet

        # Handle avatar image update
        if request.FILES.get('avatar'):
            image_file = request.FILES['avatar']

            # Remove old image from Cloudinary
            cloud = destroy_cloudinary_image(patient_instance.cloudinary_public_id)

            # Check for the result of the delete operation
            if cloud.get('result') == 'ok':
                # Set a new public ID and upload the new image
                set_cloudinary_public_id(patient_instance)
                result = upload_cloudinary_avatar(image_file, patient_instance.cloudinary_public_id)

                if result.get('url'):
                    patient_instance.avatar = result['url']
                else:
                    messages.error(request, "Failed to upload new avatar to Cloudinary.")
                    return redirect("patients:list")  # Return on error

        # Save updated patient instance
        patient_instance.save()
        messages.success(request, "Patient updated successfully!")
        return redirect("patients:patient_view", id)

    else:
        messages.error(request, "Please correct the errors below.")
        print(form.errors)

    # Set context for rendering
    context["form"] = form
    context["patient"] = patient

    return render(request, 'patients/update_patient.html', context)

@login_required(login_url='users:login')  # Protect the delete_patient view
>>>>>>> b3bbbc5f42648fc7a3cd5d923688293eb0e65cae
@check_patient_hidden
def delete_patient(request, id):
    """
    Soft deletes patient from database by marking the hidden field as true.
    """
<<<<<<< HEAD
    context = {}

    # retrieve patient
    patient = get_object_or_404(PatientModel, id=id)

    # if confirmation modal approved
    if request.method == "POST":
        # mark as hidden and return to list
        patient.hidden = True

        # update the db and redirect to patient list dashboard
        patient.save(update_fields=["hidden"])
        return redirect("patients:list")
  
    context["patient"] = patient
=======
    patient = get_object_or_404(PatientModel, id=id)

    # Confirm deletion via POST request
    if request.method == "POST":
        patient.hidden = True  # Mark as hidden
        patient.save(update_fields=["hidden"])
        messages.success(request, "Patient deleted successfully!")  # Feedback on successful deletion
        return redirect("patients:list")

    context = {"patient": patient}
>>>>>>> b3bbbc5f42648fc7a3cd5d923688293eb0e65cae
    return render(request, "patients/delete_patient.html", context)
