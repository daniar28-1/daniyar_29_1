from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(max_length=200)
    quantity = models.FloatField()

