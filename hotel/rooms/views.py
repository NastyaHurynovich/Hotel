from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from rooms import consts as rooms_consts
from rooms import forms, models


class IndexView(TemplateView):
    template_name = "base.html"


class RoomsListView(ListView):
    permission_required = "rooms.view_room"
    context_object_name = "rooms"
    template_name = "rooms/list.html"
    model = models.Rooms
    paginate_by = rooms_consts.PAGE_SIZE


class CreateRoomView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "rooms.add_room"
    form_class = forms.RoomsForm
    template_name = "rooms/create.html"
    success_url = reverse_lazy("rooms:list")
    success_message = "Запись успешно создана"


class DetailRoomView(DetailView):
    permission_required = "rooms.view_room"
    model = models.Rooms
    template_name = "rooms/detail.html"
    context_object_name = "room"


class UpdateRoomView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "rooms.change_room"
    context_object_name = "room"
    model = models.Rooms
    template_name = "rooms/update.html"
    form_class = forms.RoomsForm
    success_message = "Запись успешно обновлена"


class DeleteRoomView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "rooms.delete_room"
    model = models.Rooms
    success_url = reverse_lazy("rooms:list")
    success_message = "Запись успешно удалена"

    def get(self, *args, **kwargs):
        if self.success_message:
            messages.success(self.request, self.success_message)
        return self.delete(*args, **kwargs)
