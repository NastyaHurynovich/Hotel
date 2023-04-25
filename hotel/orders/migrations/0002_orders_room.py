# Generated by Django 4.2 on 2023-04-25 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_remove_rooms_main_photo'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='room',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='rooms.rooms'),
            preserve_default=False,
        ),
    ]
