# views.py

from django.shortcuts import render, redirect
from .models import StartingCash, EndingCash
from django.utils import timezone
from Billing.models import BillingDetails
from django.db import models

def enter_cash(request):
    current_date = timezone.now().date()
    starting_cash_value = None
    ending_cash_value = None

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'start':
            starting_cash_value = request.POST.get('starting_cash')
            if starting_cash_value is not None:
                StartingCash.objects.update_or_create(date=current_date, defaults={'starting_cash': starting_cash_value})
                return redirect('CashHandling')
        elif action == 'end':
            ending_cash_value = request.POST.get('ending_cash')
            if ending_cash_value is not None:
                EndingCash.objects.update_or_create(date=current_date, defaults={'ending_cash': ending_cash_value})
                return redirect('CashHandling')

    starting_cash_entry = StartingCash.objects.filter(date=current_date).first()
    if starting_cash_entry:
        starting_cash_value = starting_cash_entry.starting_cash
    ending_cash_entry = EndingCash.objects.filter(date=current_date).first()
    if ending_cash_entry:
        ending_cash_value = ending_cash_entry.ending_cash

    total_cash_sales_current_date = BillingDetails.objects.filter(transaction_date__date=current_date, paymenttype='Cash').aggregate(total=models.Sum('price'))['total']
    if total_cash_sales_current_date is None:
        total_cash_sales_current_date = 0

    previous_date = current_date - timezone.timedelta(days=1)
    total_cash_sales_previous_date = BillingDetails.objects.filter(transaction_date__date=previous_date, paymenttype='Cash').aggregate(total=models.Sum('price'))['total']
    if total_cash_sales_previous_date is None:
        total_cash_sales_previous_date = 0

    starting_cash_deviation = starting_cash_value - total_cash_sales_previous_date if starting_cash_value is not None else 0
    ending_cash_deviation = ending_cash_value - total_cash_sales_current_date if ending_cash_value is not None else 0

    starting_cash_deviation_display = starting_cash_deviation if starting_cash_deviation <= 0 else f"+{starting_cash_deviation}"
    ending_cash_deviation_display = ending_cash_deviation if ending_cash_deviation <= 0 else f"+{ending_cash_deviation}"

    return render(request, 'cashhandling.html', {
        'current_date': current_date,
        'starting_cash': starting_cash_value,
        'ending_cash': ending_cash_value,
        'total_cash_sales_current_date': total_cash_sales_current_date,
        'total_cash_sales_previous_date': total_cash_sales_previous_date,
        'starting_cash_deviation': starting_cash_deviation_display,
        'ending_cash_deviation': ending_cash_deviation_display
    })
