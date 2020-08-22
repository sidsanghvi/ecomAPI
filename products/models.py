from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(blank=True, null=True, max_length=120)
    active = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2)
    quantity = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
