# Generated by Django 4.2 on 2023-04-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_remove_rooms_main_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='type_room',
            field=models.CharField(blank=True, choices=[(None, 'Выберите значение'), ('single_room', 'Одноместный'), ('double_room', 'Двухместный'), ('triple_room', 'Трехместный'), ('lux', 'Люкс')], max_length=15, null=True, verbose_name='Тип номера'),
        ),
    ]
