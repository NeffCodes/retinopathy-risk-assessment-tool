import pytest
from unittest.mock import patch
from django.contrib.auth.models import User
from retina_photos.models import RetinaPhoto
from patients.models import Patient


# Mock Cloudinary upload fixture
@pytest.fixture
def mock_cloudinary_upload():
    with patch("cloudinary.uploader.upload") as mock_upload:
        mock_upload.return_value = {
            "url": "https://example.com/photo.jpg",
            "public_id": "sample_id",
        }
        yield mock_upload


# Mock Cloudinary destroy fixture
@pytest.fixture
def mock_cloudinary_destroy():
    with patch("cloudinary.uploader.destroy") as mock_destroy:
        mock_destroy.return_value = {"result": "ok"}
        yield mock_destroy


# Mock creating a user and a patient
@pytest.fixture
def mock_user_and_patient(db):
    user = User.objects.create_user(username="testuser", password="testpassword")
    patient = Patient.objects.create(
        first_name="John", last_name="Doe", date_of_birth="1990-01-01", user=user
    )
    return user, patient


@pytest.mark.django_db
def test_hard_delete_unprocessed_scans(
    client, mock_user_and_patient, mock_cloudinary_upload, mock_cloudinary_destroy
):
    """
    Test that a RetinaPhoto is properly deleted from the database and removed from Cloudinary if the status is 'unprocessed'.
    Also verifies that the user is redirected to the photos list after deletion.
    """

    # Unpack the returned user and patient from the fixture
    user, patient = mock_user_and_patient

    # Log in the user using the test client
    client.login(username="testuser", password="testpassword")

    # Create a sample RetinaPhoto to test deletion
    retina_photo = RetinaPhoto.objects.create(
        image="https://example.com/image.jpg",
        patient=patient,
        position="left",
        status="unprocessed",
        cloudinary_public_id="sample_id",
    )

    # Ensure the RetinaPhoto exists in the database
    assert RetinaPhoto.objects.count() == 1
    mock_cloudinary_upload.assert_not_called()  # Ensure upload wasn't triggered yet

    # Now, perform the deletion
    delete_url = f"/retina_photos/{retina_photo.id}/delete/"
    response = client.post(delete_url)

    # Ensure the photo was deleted from the database
    assert RetinaPhoto.objects.count() == 0

    # Ensure Cloudinary's destroy API was called
    mock_cloudinary_destroy.assert_called_once_with(
        f"rrat/retina_photos/{retina_photo.cloudinary_public_id}"
    )

    # Ensure the user is redirected to the photos list
    assert response.status_code == 302
    assert response.url == f"/patients/{patient.id}/"


@pytest.mark.django_db
def test_soft_delete_processed_scans(
    client, mock_user_and_patient, mock_cloudinary_upload, mock_cloudinary_destroy
):
    """
    Test that a RetinaPhoto is marked as hidden and not deleted from the database or removed from Cloudinary if the status is 'processed'.
    Also verifies that the user is redirected to the photos list after deletion.
    """

    # Unpack the returned user and patient from the fixture
    user, patient = mock_user_and_patient

    # Log in the user using the test client
    client.login(username="testuser", password="testpassword")

    # Create a sample RetinaPhoto to test deletion
    retina_photo = RetinaPhoto.objects.create(
        image="https://example.com/image.jpg",
        patient=patient,
        position="left",
        status="pending",
        cloudinary_public_id="sample_id",
    )

    # Ensure the RetinaPhoto exists in the database
    assert RetinaPhoto.objects.count() == 1
    mock_cloudinary_upload.assert_not_called()  # Ensure upload wasn't triggered yet

    # Now, perform the deletion
    delete_url = f"/retina_photos/{retina_photo.id}/delete/"
    response = client.post(delete_url)

    # Ensure the photo was not deleted from the databases and marked hidden
    assert RetinaPhoto.objects.get(id=retina_photo.id).hidden == True
    assert RetinaPhoto.objects.count() == 1
    mock_cloudinary_destroy.assert_not_called()

    # Ensure the user is redirected to the photos list
    assert response.status_code == 302
    assert response.url == f"/patients/{patient.id}/"


def test_delete_nonexistent_retina_photo(client):
    """
    Test that attempting to delete a non-existent RetinaPhoto results in a 404 error
    """
    delete_url = "/retina_photos/999/delete/"
    response = client.post(delete_url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_retina_photo_without_permission(client):
    """
    Test that attempting to delete a RetinaPhoto without permission results in a 404 error
    Ensure that even if a user is not logged in, they cannot delete a RetinaPhoto
    """
    delete_url = "/retina_photos/1/delete/"
    client.logout()
    response = client.post(delete_url)
    assert response.status_code == 404
