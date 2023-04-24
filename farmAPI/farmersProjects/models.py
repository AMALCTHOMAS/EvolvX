from django.db import models
from django.utils.timezone import now

class Projects(models.Model):
    farmer = models.EmailField(max_length=255)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=50,null=True) 
    zipcode = models.CharField(max_length=20)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=3)
    photo1 = models.ImageField(upload_to="projects/")
    photo2 = models.ImageField(upload_to="projects/")
    photo3 = models.ImageField(upload_to="projects/")

    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return self.title