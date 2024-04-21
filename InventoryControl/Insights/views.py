from django.shortcuts import render
from Billing.models import BillingDetails
from Inventory.models import Products
from datetime import date, timedelta


def insights(request):
    transactions = BillingDetails.objects.all()  # Retrieve all transactions from the database
    
    # Retrieve nearby expiry products (within 7 days)
    today = date.today()
    threshold_date = today + timedelta(days=7) 
    nearby_expiry_products = Products.objects.filter(expiry__lte=threshold_date,expiry__gt=today)
    
    # If there are no nearby expiry products, set the variable to "None"
    if not nearby_expiry_products:
        nearby_expiry_products = None
    
    # Retrieve expired products
    expired_products = Products.objects.filter(expiry__lte=today)
    
    return render(request, 'insight.html', {'transactions': transactions,
                                             'nearby_expiry_products': nearby_expiry_products,
                                             'expired_products': expired_products})   
