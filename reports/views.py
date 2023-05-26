from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Report
from .serializers import ReportSerializer
from patients.models import Patient
from docter.models import Doctor

class ReportCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, patient_id):
        # Retrieve the patient
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)
        
        # Retrieve the doctor (current user)
        doctor = Doctor.objects.get(username=request.user.username)

        
        # Create a new report for the patient
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=patient, created_by=doctor)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ReportListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        # Retrieve all reports of a patient
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)
        
        reports = Report.objects.filter(patient=patient).order_by('date')
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

class ReportStatusListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, status):
        # Retrieve all reports filtered by status
        reports = Report.objects.filter(status=status)
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)
