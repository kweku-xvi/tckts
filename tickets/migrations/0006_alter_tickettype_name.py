# Generated by Django 4.2.1 on 2024-05-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_alter_tickettype_ticket_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickettype',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
