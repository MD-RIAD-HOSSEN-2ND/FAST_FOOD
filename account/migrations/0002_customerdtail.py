# Generated by Django 5.0.2 on 2024-08-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDtail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('paymenttype', models.CharField(max_length=50)),
                ('deliveryAddress', models.TextField(blank=True)),
            ],
        ),
    ]
