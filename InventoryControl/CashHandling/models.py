# cash_register/models.py

from django.db import models

class StartingCash(models.Model):
    date = models.DateField(auto_now_add=True)
    starting_cash = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.date) + " - StartCash"
        

class EndingCash(models.Model):
    date = models.DateField(auto_now_add=True)
    ending_cash = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.date) + " - EndCash"
        