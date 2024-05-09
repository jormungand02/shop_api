# Generated by Django 5.0.4 on 2024-05-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('card', 'CARD'), ('cash', 'CASH')], max_length=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ND', 'Not Deliverd'), ('D', 'Deliverd')], max_length=4),
        ),
    ]
