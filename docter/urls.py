# urls.py

from django.urls import path
from .views import DoctorRegisterView, DoctorLoginView

urlpatterns = [
    path('register/', DoctorRegisterView.as_view(), name='doctor_register'),
    path('login/', DoctorLoginView.as_view(), name='doctor_login'),
]
