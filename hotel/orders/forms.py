import datetime as dt

import pandas
from django import forms
from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput
from django.core.exceptions import ValidationError

from orders import models

from orders import validators


# from portal import validators


class OrdersForm(forms.ModelForm):
    check_in = forms.DateField(
        label="Заезд",
        required=True,
        widget=DatePickerInput(
            options=FlatpickrOptions(altFormat="d.m.Y")
        ),
        validators=[validators.validate_check_in]
    )
    check_out = forms.DateField(
        label="Выезд",
        required=True,
        widget=DatePickerInput(
            options=FlatpickrOptions(altFormat="d.m.Y")
        ))

    def __init__(self, request, params, *args, **kwargs):
        self.request = request
        self.params = params
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if "check_in" in self.cleaned_data and "check_out" in self.cleaned_data and \
                self.cleaned_data["check_in"] >= self.cleaned_data["check_out"]:
            raise ValidationError("День выезда должен быть позже дня вселения")
        return cleaned_data

    # def clean(self):
    #     cleaned_data = super().clean()
    #     if self.cleaned_data["check_in"] in pandas.date_range(self.cleaned_data["check_in"],
    #                                                           self.cleaned_data["check_out"]) or self.cleaned_data[
    #         "check_out"] in pandas.date_range(self.cleaned_data["check_in"], self.cleaned_data["check_out"]):
    #         raise ValidationError("Извините, но эти даты забронированы")
    #     return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.room_id = self.params['room_id']
        instance.save()
        instance.user = self.request.user
        instance.save()
        return instance

    class Meta:
        model = models.Orders
        fields = (
            "check_in",
            "check_out",
            "number_of_visitors"
        )
