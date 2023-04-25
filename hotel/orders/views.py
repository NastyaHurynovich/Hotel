from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from orders import forms, models
from django.template import loader

from orders.models import Orders

from orders.mixins import FormRequestKwargMixin


# def index(request: HttpRequest) -> HttpResponse:
#     qs = Orders.objects.order_by("check_in").all()
#     return render(request, "orders/list.html", {"orders": qs})


class OrdersListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "orders.view_order"
    context_object_name = "orders"
    template_name = "orders/list.html"
    model = models.Orders


class CreateOrderView(FormRequestKwargMixin, LoginRequiredMixin, SuccessMessageMixin,
                      CreateView):
    form_class = forms.OrdersForm
    template_name = "orders/create.html"
    success_url = reverse_lazy("rooms:list")
    success_message = "Запись успешно создана"
