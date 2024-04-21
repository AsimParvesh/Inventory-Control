from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_summary, name='sales_summary'),
]
