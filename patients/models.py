from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, default='')
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

