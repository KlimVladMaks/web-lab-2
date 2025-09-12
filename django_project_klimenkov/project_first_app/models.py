from django.db import models

class CarOwner(models.Model):
    id_owner = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    cars = models.ManyToManyField('Car', through='Ownership')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.model} ({self.license_plate})"


class DrivingLicense(models.Model):
    LICENSE_TYPES = [
        ('A', 'Категория A'),
        ('B', 'Категория B'),
        ('C', 'Категория C'),
        ('D', 'Категория D'),
        ('BE', 'Категория BE'),
        ('CE', 'Категория CE'),
        ('DE', 'Категория DE'),
        ('Tm', 'Категория Tm'),
        ('Tb', 'Категория Tb'),
        ('M', 'Категория M'),
        ('A1', 'Подкатегория A1'),
        ('B1', 'Подкатегория B1'),
        ('C1', 'Подкатегория C1'),
        ('D1', 'Подкатегория D1'),
        ('C1E', 'Подкатегория C1E'),
        ('D1E', 'Подкатегория D1E'),
    ]

    id_license = models.AutoField(primary_key=True)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10, choices=LICENSE_TYPES)
    issue_date = models.DateField()

    def __str__(self):
        return f"{self.license_number} ({self.license_type})"


class Ownership(models.Model):
    id_ownership = models.AutoField(primary_key=True)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.owner} - {self.car} ({self.start_date} - {self.end_date})"
