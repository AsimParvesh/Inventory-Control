from django.db import models

class BillingDetails (models.Model):
    transactionid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phn = models.CharField(max_length=15)
    gender = models.CharField(max_length=1)
    pname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pcategory =models.CharField(max_length=30)
    age_category = models.CharField(max_length=25)
    paymenttype = models.CharField(max_length=30)
    transaction_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name + "-" + str(self.transactionid)
        