# Generated by Django 4.2 on 2023-04-25 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_remove_rooms_main_photo'),
        ('orders', '0002_orders_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.rooms'),
        ),
    ]