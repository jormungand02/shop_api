# Generated by Django 5.0.4 on 2024-05-03 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('D', 'Deliverd'), ('ND', 'Not Deliverd')], max_length=4),
        ),
    ]
