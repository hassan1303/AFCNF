from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_farmer = models.BooleanField(default=True)
    is_admin_user = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=100)
    farm_size = models.FloatField(help_text="Size in hectares")
    AGRIC_TYPE = [('Crop', 'Crop'), ('Livestock', 'Livestock'), ('Mixed', 'Mixed')]
    agriculture_type = models.CharField(max_length=10, choices=AGRIC_TYPE)

    def __str__(self):
        return self.user.username



   

class FarmDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=50)
    FARMING_METHOD = [('Traditional', 'Traditional'), ('Mechanized', 'Mechanized'), ('Organic', 'Organic')]
    method = models.CharField(max_length=20, choices=FARMING_METHOD)

class CropData(models.Model):
    farm = models.ForeignKey(FarmDetail, on_delete=models.CASCADE)
    crop_type = models.CharField(max_length=100)
    yield_expected = models.FloatField()
    yield_actual = models.FloatField()
    fertilizer_type = models.CharField(max_length=100)
    quantity_fertilizer = models.FloatField()
    pesticide_type = models.CharField(max_length=100)
    quantity_pesticide = models.FloatField()
    land_area = models.FloatField()

class LivestockData(models.Model):
    farm = models.ForeignKey(FarmDetail, on_delete=models.CASCADE)
    animal_type = models.CharField(max_length=50)
    count = models.IntegerField()
    feeding = models.CharField(max_length=100)
    manure_method = models.CharField(max_length=100)

class WaterUsage(models.Model):
    farm = models.ForeignKey(FarmDetail, on_delete=models.CASCADE)
    IRRIGATION_TYPE = [('Rain-fed', 'Rain-fed'), ('Borehole', 'Borehole'), ('River', 'River')]
    irrigation_type = models.CharField(max_length=20, choices=IRRIGATION_TYPE)
    water_consumption = models.FloatField()
    PUMP_TYPE = [('Manual', 'Manual'), ('Diesel', 'Diesel'), ('Solar', 'Solar'), ('Electric', 'Electric')]
    pump_type = models.CharField(max_length=20, choices=PUMP_TYPE)

class MachineryUse(models.Model):
    farm = models.ForeignKey(FarmDetail, on_delete=models.CASCADE)
    machine_type = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=20)
    estimated_consumption = models.FloatField()