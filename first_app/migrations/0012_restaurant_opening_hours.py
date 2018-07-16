# Generated by Django 2.0.5 on 2018-07-15 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_remove_restaurant_opening_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='opening_hours',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='first_app.OpeningHours'),
            preserve_default=False,
        ),
    ]
