# Generated by Django 4.2.11 on 2024-05-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restraun", "0006_alter_booking_reservation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="reservation_date",
            field=models.DateField(default="2004-02-02"),
        ),
    ]
