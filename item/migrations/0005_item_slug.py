# Generated by Django 5.0.2 on 2024-08-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_rename_reviewer_review_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=None, max_length=100),
        ),
    ]
