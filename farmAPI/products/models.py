from django.db import models
from django.utils.timezone import now

class Products(models.Model):
    pname = models.CharField(null=False,max_length=100)
    discription = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    farmer = models.EmailField(max_length=255)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    unit = models.CharField(max_length=15)
    photo = models.ImageField(upload_to="products/")
    create_time = models.DateTimeField(default=now)

class Orders(models.Model):
    pname = models.CharField(max_length=100,null=True)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    farmer = models.EmailField(max_length=255)
    customer = models.EmailField(max_length=255)
    order_date = models.DateTimeField(default=now)