from django.shortcuts import render
from django.db.models import Sum, Count
from datetime import datetime, timedelta, timezone
from Billing.models import BillingDetails

def sales_summary(request):
    summary_type = request.GET.get('summary_type')
    selected_date = request.GET.get('date')
    sales_summary_data = None
    daily_sales = {}
    upi_payments = 0
    cash_payments = 0
    card_payments = 0
    transactions = []

    if not summary_type and selected_date:
        summary_type = 'daily'
        selected_date = str(timezone.now().date())

    if summary_type and selected_date:
        if summary_type == 'daily':
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            sales_summary_data = BillingDetails.objects.filter(transaction_date__date=selected_date).aggregate(total_sales=Sum('price'))
            daily_sales[selected_date] = sales_summary_data['total_sales']
            upi_payments = BillingDetails.objects.filter(transaction_date__date=selected_date, paymenttype='UPI').count()
            cash_payments = BillingDetails.objects.filter(transaction_date__date=selected_date, paymenttype='Cash').count()
            card_payments = BillingDetails.objects.filter(transaction_date__date=selected_date, paymenttype='Card').count()
            transactions = BillingDetails.objects.filter(transaction_date__date=selected_date)
        elif summary_type == 'weekly':
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            start_date = selected_date - timedelta(days=selected_date.weekday())
            end_date = start_date + timedelta(days=6)
            sales_summary_data = BillingDetails.objects.filter(transaction_date__date__range=[start_date, end_date]).aggregate(total_sales=Sum('price'))
            for i in range(7):
                current_date = start_date + timedelta(days=i)
                daily_sales[current_date] = BillingDetails.objects.filter(transaction_date__date=current_date).aggregate(total_sales=Sum('price'))['total_sales'] or 0
                upi_payments += BillingDetails.objects.filter(transaction_date__date=current_date, paymenttype='UPI').count()
                cash_payments += BillingDetails.objects.filter(transaction_date__date=current_date, paymenttype='Cash').count()
                card_payments += BillingDetails.objects.filter(transaction_date__date=current_date, paymenttype='Card').count()
                transactions.extend(list(BillingDetails.objects.filter(transaction_date__date=current_date)))
        elif summary_type == 'monthly':
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            start_date = selected_date.replace(day=1)
            end_date = start_date.replace(day=1, month=start_date.month+1) - timedelta(days=1)
            sales_summary_data = BillingDetails.objects.filter(transaction_date__date__range=[start_date, end_date]).aggregate(total_sales=Sum('price'))
            while start_date <= end_date:
                daily_sales[start_date] = BillingDetails.objects.filter(transaction_date__date=start_date).aggregate(total_sales=Sum('price'))['total_sales'] or 0
                upi_payments += BillingDetails.objects.filter(transaction_date__date=start_date, paymenttype='UPI').count()
                cash_payments += BillingDetails.objects.filter(transaction_date__date=start_date, paymenttype='Cash').count()
                card_payments += BillingDetails.objects.filter(transaction_date__date=start_date, paymenttype='Card').count()
                transactions.extend(list(BillingDetails.objects.filter(transaction_date__date=start_date)))
                start_date += timedelta(days=1)

    return render(request, 'sales_summary.html', {
        'summary_type': summary_type,
        'selected_date': selected_date,
        'sales_summary_data': sales_summary_data,
        'daily_sales': daily_sales,
        'upi_payments': upi_payments,
        'cash_payments': cash_payments,
        'card_payments': card_payments,
        'transactions': transactions,
    })
