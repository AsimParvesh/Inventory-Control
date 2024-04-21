from django import forms
from .models import BillingDetails

class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = ['name', 'phn', 'gender', 'age_category', 'pname', 'pcategory', 'price', 'paymenttype','transaction_date']
        exclude = ['transactionid']