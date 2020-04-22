from django.db import models

# Create your models here.


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    img = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    currency = models.CharField(max_length=5)
    price = models.FloatField()
    quantity = models.IntegerField()
    total_price = models.FloatField()