"""
URL configuration for InventoryControl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AdminLogin.urls')),
    path('',include("django.contrib.auth.urls")),
    path('Home/', include('Home.urls')),
    path('Home/Inventory', include('Inventory.urls')),
    path('Home/Billing', include('Billing.urls')),
    path('Home/Insights', include('Insights.urls')),
    path('Home/SalesSummary', include('SalesSummary.urls')),
    path('Home/CashHandling', include('CashHandling.urls')),

]
