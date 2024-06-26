# Generated by Django 4.2.1 on 2024-05-28 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticketpurchase_payment_verified'),
        ('payments', '0004_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='purchase',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.ticketpurchase'),
        ),
    ]
