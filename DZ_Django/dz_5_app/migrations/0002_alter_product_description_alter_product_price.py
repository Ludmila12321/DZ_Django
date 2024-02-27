# Generated by Django 5.0.2 on 2024-02-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dz_5_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Это прекрасный продукт!'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=8),
        ),
    ]
