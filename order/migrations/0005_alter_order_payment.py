# Generated by Django 5.0.4 on 2024-05-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_options_alter_orderitem_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('cash', 'CASH'), ('card', 'CARD')], max_length=5),
        ),
    ]
