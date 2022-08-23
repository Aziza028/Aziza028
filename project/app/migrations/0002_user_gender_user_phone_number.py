# Generated by Django 4.0.5 on 2022-08-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="", max_length=1
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]