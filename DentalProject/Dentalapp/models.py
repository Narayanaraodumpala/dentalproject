from django.db import models

# Create your models here.
class DoctorsModel(models.Model):
    doctor_name=models.CharField(max_length=20,null=True)
    specilization=models.CharField(max_length=30,null=True)
    rating=models.FloatField(null=True)
    fee=models.FloatField(null=True)
    distance=models.CharField(max_length=50,null=True)
    avilable_in=models.CharField(max_length=100,null=True)
    doctor=models.ImageField(upload_to='doctors/',null=True)

    def __str__(self):
        return self.doctor_name

class Next3Dentist(models.Model):
    doctor_name = models.CharField(max_length=20, null=True)
    specilization = models.CharField(max_length=30, null=True)
    rating = models.FloatField(null=True)
    fee = models.FloatField(null=True)
    distance = models.CharField(max_length=50, null=True)
    avilable_in = models.CharField(max_length=100, null=True)
    doctor = models.ImageField(upload_to='doctors/', null=True)


class AnotherNext3Dentist(models.Model):
    doctor_name = models.CharField(max_length=20, null=True)
    specilization = models.CharField(max_length=30, null=True)
    rating = models.FloatField(null=True)
    fee = models.FloatField(null=True)
    distance = models.CharField(max_length=50, null=True)
    avilable_in = models.CharField(max_length=100, null=True)
    doctor = models.ImageField(upload_to='doctors/', null=True)
