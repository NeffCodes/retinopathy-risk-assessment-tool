from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient as PatientModel
from .forms import PatientForm
from .decorators import check_patient_hidden, check_permission_to_view_patient
from .cloudinary_helpers import *
from retina_photos.views import upload_retina_photo
from retina_photos.models import RetinaPhoto
from retina_photos.forms import RetinaForm


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
        
        # Set the patient's user
        patient_instance.user = request.user

        # Handle avatar image upload
        if request.FILES.get('avatar'):
            image_file = request.FILES['avatar']
            set_cloudinary_public_id(patient_instance)
            result = upload_cloudinary_avatar(image_file, patient_instance.cloudinary_public_id)

            if result.get('url'):
                patient_instance.avatar = result['url']
            else:
                messages.error(request, "Failed to upload avatar to Cloudinary.")

        # Save patient instance to the database
        patient_instance.save()
        messages.success(request, "Patient added successfully!")
        return redirect("patients:list")
    else:
        if form.errors:
            messages.error(request, "Please correct the form errors below.")

    # Fetch all non-hidden patients from the database
    patients = PatientModel.objects.filter(user=request.user).exclude(hidden=True).order_by('last_name')

    # Set context for rendering
    context['form'] = form
    context['patients'] = patients

    return render(request, 'patients/patients_list.html', context)


@login_required(login_url='users:login')  # Protect the view_patient view
@check_patient_hidden
@check_permission_to_view_patient
def view_patient(request, id):
    """
    Patient page to view patient details.
    Handles displaying the form and uploaded retina scans.
    """
    # Retrieve the patient instance
    patient = get_object_or_404(PatientModel, id=id)

    # Retrieve retina images associated with the patient
    unprocessed_images = RetinaPhoto.objects.filter(patient=patient, status='unprocessed').order_by('-date_created')
    processed_images = RetinaPhoto.objects.filter(patient=patient).exclude(status='unprocessed').order_by('-date_updated')

    # If a POST request is made, delegate to the upload logic
    if request.method == "POST":
        # Perform upload logic and handle redirect
        return upload_retina_photo(request=request, patient=patient)

    # On GET, provide an empty form for display
    form = RetinaForm()

    # Render the page with patient details and the form
    context = {
        "form": form,
        "patient": patient,
        "images_processed": processed_images,
        "images_unprocessed": unprocessed_images
    }

    return render(request, 'patients/view_patient.html', context)


@login_required(login_url='users:login')  # Protect the update_patient view
@check_patient_hidden
@check_permission_to_view_patient
def update_patient(request, id):
    """
    Patient page to change patient details.
    """
    patient = get_object_or_404(PatientModel, id=id)
    context = {}

    # Initialize the form with the patient instance
    form = PatientForm(request.POST or None, request.FILES or None, instance=patient)

    if form.is_valid():
        patient_instance = form.save(commit=False)

        # Handle avatar image update
        if request.FILES.get('avatar'):
            image_file = request.FILES['avatar']
            cloud = destroy_cloudinary_image(patient_instance.cloudinary_public_id)

            if cloud.get('result') == 'ok':
                set_cloudinary_public_id(patient_instance)
                result = upload_cloudinary_avatar(image_file, patient_instance.cloudinary_public_id)

                if result.get('url'):
                    patient_instance.avatar = result['url']
                else:
                    messages.error(request, "Failed to upload new avatar to Cloudinary.")
                    return redirect("patients:list")

        # Save updated patient instance
        patient_instance.save()
        messages.success(request, "Patient updated successfully!")
        return redirect("patients:patient_view", id)
    else:
        messages.error(request, "Please correct the errors below.")

    context["form"] = form
    context["patient"] = patient

    return render(request, 'patients/update_patient.html', context)


@login_required(login_url='users:login')  # Protect the delete_patient view
@check_patient_hidden
@check_permission_to_view_patient
def delete_patient(request, id):
    """
    Soft deletes patient from the database by marking the hidden field as true.
    """
    patient = get_object_or_404(PatientModel, id=id)

    if request.method == "POST":
        patient.hidden = True
        patient.save(update_fields=["hidden"])
        messages.success(request, "Patient deleted successfully!")
        return redirect("patients:list")

    context = {"patient": patient}
    return render(request, "patients/delete_patient.html", context)
