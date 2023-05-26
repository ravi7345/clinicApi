# urls.py

from django.urls import path
from .views import ReportCreateView, ReportListView, ReportStatusListView



urlpatterns = [
    path('<str:status>/', ReportStatusListView.as_view(), name='report_status_list'),
]
