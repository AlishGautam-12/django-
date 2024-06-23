# Generated by Django 4.2.5 on 2024-03-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Singing_Event_Booking_System", "0002_booking"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="date_created",
        ),
        migrations.AddField(
            model_name="booking",
            name="event_id",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="booking",
            name="phone",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="booking",
            name="user_name",
            field=models.CharField(max_length=100),
        ),
    ]
