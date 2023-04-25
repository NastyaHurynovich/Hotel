from django.db import models

from rooms.models import Rooms

from core.models import User


class Orders(models.Model):
    check_in = models.DateField(verbose_name='Заезд')
    check_out = models.DateField(verbose_name='Выезд')
    number_of_visitors = models.IntegerField(verbose_name='Количество посетителей')
    room = models.ForeignKey(
        Rooms,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    user = models.ForeignKey(
        User,
        verbose_name="Заказчик",
        on_delete=models.PROTECT,
        related_name="client",
        blank=True,
        null=True)

    def __str__(self):
        return self.title_room

    def get_absolute_url(self):
        return f"/orders/{self.pk}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-check_in"]
        get_latest_by = "created_at"
