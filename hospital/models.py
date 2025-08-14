from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)  # Changed to CharField for better flexibility
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15, null=True)  # Changed to CharField
    address = models.CharField(max_length=100)  # Increased max_length for address

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} -- {self.patient.name}"  # Corrected to access the doctor's name


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=50, null=True)  # Changed to EmailField for validation
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.BooleanField(default=False)  # Changed to BooleanField for better readability

    def __str__(self):
        return f"{self.name} ({self.id})"  # Changed to return name with ID

