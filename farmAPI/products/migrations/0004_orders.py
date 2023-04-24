# Generated by Django 4.0.10 on 2023-04-24 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('farmer', models.EmailField(max_length=255)),
                ('customer', models.EmailField(max_length=255)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
