# Generated by Django 2.0.5 on 2018-07-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_dish_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='verified',
            field=models.BooleanField(default=True),
        ),
    ]
