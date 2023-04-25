from django.db import models
from django.urls import reverse_lazy


# from portal import validators


class Rooms(models.Model):
    class TypeChoices(models.TextChoices):
        SINGLE = "Одноместный", "Одноместный"
        DOUBLE = "Двухместный", "Двухместный"
        TRIPLE = "Трехместный", "Трехместный"
        LUX = "Люкс", "Люкс"
        __empty__ = "Выберите значение"

    title = models.CharField(verbose_name='Название', max_length=250)
    type_room = models.CharField(verbose_name="Тип номера", max_length=15, choices=TypeChoices.choices, blank=True,
                                 null=True)
    description = models.TextField(blank=True, verbose_name="Описание")
    facilities = models.TextField(verbose_name='Удобства', null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("rooms:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"
        # ordering = ["-type_room"]
