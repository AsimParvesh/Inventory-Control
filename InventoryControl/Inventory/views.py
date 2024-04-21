from django.shortcuts import render
from .models import Products
from django.db.models import Q


def inventory(request):
    products = Products.objects.all()

    product_code = request.GET.get('product_code')
    if product_code:
        products = products.filter(product_code__icontains=product_code)

    product_name = request.GET.get('q')
    if product_name:
        products = products.filter(product_name__icontains=product_name)

    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    return render(request, 'inventory.html', {'products': products})