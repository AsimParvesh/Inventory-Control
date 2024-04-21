from django.shortcuts import render, redirect
from .forms import BillingForm
from Inventory.models import Products
from django.utils import timezone
import logging, razorpay

logger = logging.getLogger(__name__)

def billing(request):
    try:
        product_names = Products.objects.values_list('product_name', flat=True)
        product_categories = Products.objects.values_list('category', flat=True).distinct()

        if request.method == 'POST':
            form = BillingForm(request.POST)
            if form.is_valid():
                form.instance.transaction_date = timezone.now()
                form.save()
                logger.info("Form data saved successfully")

                # Convert amount from rupees to paise (subunits)
                amount_in_rupees = form.cleaned_data.get('price')
                amount_in_paise = int(amount_in_rupees * 100)  # Convert rupees to paise

                # Initialize Razorpay client with your API keys
                client = razorpay.Client(auth=("rzp_test_KoPpsQKbIRrTsm", "hCOckhqZ8LwkfNv8c8vFbHYr"))

                # Create order with specified amount in paise and currency
                order_response = client.order.create({
                    "amount": amount_in_paise,
                    "currency": "INR",
                })

                # Handle order creation response as needed
                order_id = order_response.get('id')
                logger.info("Razorpay order created successfully with ID: %s", order_id)

                # Continue with your existing logic
                return redirect('Billing')  # Redirect to success URL after successful submission
            else:
                logger.error("Form data is invalid: %s", form.errors)
        else:
            form = BillingForm()

        return render(request, 'billing.html', {
            'form': form,
            'product_names': product_names,
            'product_categories': product_categories,
        })
    except Exception as e:
        logger.exception("An error occurred: %s", str(e))
        return render(request, 'error.html')  # Render a generic error page
