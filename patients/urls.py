# urls.py

from django.urls import path
from .views import PatientRegisterView
from reports.views import ReportCreateView,ReportListView

urlpatterns = [
    path('register/', PatientRegisterView.as_view(), name='patient_register'),
    path('<int:patient_id>/create_report/', ReportCreateView.as_view(), name='report_create'),
    path('<int:patient_id>/all_reports/', ReportListView.as_view(), name='report_list'),
]
