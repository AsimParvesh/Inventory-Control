from django.db import models
from datetime import date

class Products(models.Model):
    product_id = models.CharField(max_length=10, primary_key=True,default='001')
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    product_code = models.CharField(max_length=13)
    manufacture = models.DateField()
    expiry = models.DateField()

    def __str__(self):
        return self.product_name

    def is_near_expiry(self):
        today = date.today()
        days_remaining = (self.expiry - today).days
        return days_remaining <= 7 