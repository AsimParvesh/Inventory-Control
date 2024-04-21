# Generated by Django 4.2.7 on 2024-01-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billing', '0002_customer_paymenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDetails',
            fields=[
                ('transactionid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phn', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=1)),
                ('pname', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pcategory', models.CharField(max_length=30)),
                ('age_category', models.CharField(max_length=25)),
                ('paymenttype', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]