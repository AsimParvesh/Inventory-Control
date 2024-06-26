# Generated by Django 4.2.7 on 2024-03-02 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SalesSummary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySalesSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, unique=True)),
                ('total_sales', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='SalesSummary',
        ),
    ]
