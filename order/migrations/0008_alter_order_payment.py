# Generated by Django 5.0.4 on 2024-05-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_payment_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('cash', 'CASH'), ('card', 'CARD')], max_length=5),
        ),
    ]