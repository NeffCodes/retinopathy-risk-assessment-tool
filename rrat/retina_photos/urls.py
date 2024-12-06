from django.urls import path
from . import views

app_name = "retina_photos"

urlpatterns = [
    path('<uuid:id>/delete/', views.delete_retina_photo, name='delete_retina_photo'),
    path('<uuid:id>/analyze/', views.analyze_retina_photo, name='analyze_retina_photo')
]
