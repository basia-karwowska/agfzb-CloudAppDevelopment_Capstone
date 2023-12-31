from django.db import models
from django.utils.timezone import now

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
# Car Make model
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Ferrari')
    description = models.CharField(null=False, max_length=300, default='')

    # Create a toString method for object string representation
    def __str__(self):
        return self.name + " (" + self.description + ")"


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon')
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    dealer_id = models.IntegerField()  # Assuming dealer_id is an integer
    car_type = models.CharField(choices=CAR_TYPES, max_length=10)
    year = models.DateField()
    # Any other fields 

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year.year}, {self.car_type})"


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
