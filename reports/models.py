from django.db import models
from docter.models import Doctor
from patients.models import Patient

class Report(models.Model):
    STATUS_CHOICES = (
        ('Negative', 'Negative'),
        ('Travelled-Quarantine', 'Travelled-Quarantine'),
        ('Symptoms-Quarantine', 'Symptoms-Quarantine'),
        ('Positive-Admit', 'Positive-Admit'),
    )
    created_by = models.ForeignKey(Doctor, on_delete=models.CASCADE ,editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateField(auto_now_add=True)
