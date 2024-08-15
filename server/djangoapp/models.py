# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to="car_makes/logos/",
                             blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Car Make"
        verbose_name_plural = "Car Makes"
        ordering = ["name"]  # Orders the car makes by name alphabetically

    def __str__(self):
        return self.name  # Return the name as the string representation

    def get_established_year(self):
        if self.established_date:
            return self.established_date.year
        return None


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE
    )  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        ("COUPE", "Coupe"),
        ("CONVERTIBLE", "Convertible"),
        ("HATCHBACK", "Hatchback"),
        ("TRUCK", "Truck"),
        ("VAN", "Van"),
        # Add more choices as required
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2023, validators=[MaxValueValidator(2023),
                                  MinValueValidator(2015)]
    )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2, blank=True, null=True)
    is_electric = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="car_models/photos/",
                              blank=True, null=True)

    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"
        ordering = ["name"]  # Orders the car models by name alphabetically

    def __str__(self):
        # Return the name and year as the string representation
        return f"{self.name} ({self.year})"
