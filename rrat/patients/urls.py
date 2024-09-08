from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.patients_list, name="list"),
    path('<uuid:id>/', views.view_patient, name="patient_page"),
]