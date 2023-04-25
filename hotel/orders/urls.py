from django.urls import path

from orders import views

app_name = "orders"

urlpatterns = [
    path('', views.OrdersListView.as_view(), name="list"),
    path("<int:room_id>/create/", views.CreateOrderView.as_view(), name="create"),
    ]