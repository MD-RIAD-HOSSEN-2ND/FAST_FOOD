# Generated by Django 5.0.2 on 2024-08-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.CharField(max_length=100),
        ),
    ]
