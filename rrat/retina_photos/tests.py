from django.test import TestCase
from unittest.mock import patch
import pytest
@pytest.fixture
def mock_cloudinary_destroy():
    with patch("cloudinary.uploader.destroy") as mock_destroy:
        # Set a default return value for the mock
        mock_destroy.return_value = {"result": "ok"}
        yield mock_destroy

# Create your tests here.
