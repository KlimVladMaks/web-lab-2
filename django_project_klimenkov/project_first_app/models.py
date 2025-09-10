from django.db import models

class CarOwner(models.Model):
    id_owner = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)

class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

class DrivingLicense(models.Model):
    id_license = models.AutoField(primary_key=True)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateField()

class Ownership(models.Model):
    id_ownership = models.AutoField(primary_key=True)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
