# Generated by Django 4.2 on 2023-04-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('type_room', models.CharField(max_length=250, verbose_name='Тип номера')),
                ('main_photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('facilities', models.TextField(blank=True, null=True, verbose_name='Удобства')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
    ]