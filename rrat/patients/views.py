from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient as PatientModel
from .forms import PatientForm
from .decorators import check_patient_hidden
from .cloudinary_helpers import *
from retina_photos.views import upload_retina_photo

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
    context['form'] = form
    context['patients'] = patients

    return render(request, 'patients/patients_list.html', context)

@login_required(login_url='users:login')  # Protect the view_patient view
@check_patient_hidden
def view_patient(request, id):
    """
    Patient page to view patient details.
    """
    patient = get_object_or_404(PatientModel, id=id)

    # Handle retina photo upload
    form = upload_retina_photo(request=request, patient=patient)

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
@check_patient_hidden
def delete_patient(request, id):
    """
    Soft deletes patient from database by marking the hidden field as true.
    """
    patient = get_object_or_404(PatientModel, id=id)

    # Confirm deletion via POST request
    if request.method == "POST":
        patient.hidden = True  # Mark as hidden
        patient.save(update_fields=["hidden"])
        messages.success(request, "Patient deleted successfully!")  # Feedback on successful deletion
        return redirect("patients:list")

    context = {"patient": patient}
    return render(request, "patients/delete_patient.html", context)
