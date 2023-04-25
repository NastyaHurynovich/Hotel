from django import forms
from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput

from rooms import models
# from portal import validators


class RoomsForm(forms.ModelForm):
    # date_added = forms.DateField(
    #     label="Дата публикации",
    #     required=True,
    #     widget=DatePickerInput(
    #         options=FlatpickrOptions(altFormat="d.m.Y"),
    #     ),
    #     validators=[validators.validate_starte_date]
    # )

    class Meta:
        model = models.Rooms
        fields = (
            "title",
            "type_room",
            "description",
            "facilities",
            # "main_photo",
        )