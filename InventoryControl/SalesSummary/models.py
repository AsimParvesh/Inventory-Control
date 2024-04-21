from django.db import models
from django.utils import timezone

class DailySalesSummary(models.Model):
    date = models.DateField(default=timezone.now, unique=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Daily Sales Summary - {self.date}"