# Generated by Django 4.2.7 on 2024-03-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CashHandling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdetails',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
