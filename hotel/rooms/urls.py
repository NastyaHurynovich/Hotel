from django.urls import path

from rooms import views

app_name = "rooms"

urlpatterns = [
    path('', views.RoomsListView.as_view(), name="list"),
    path("create/", views.CreateRoomView.as_view(), name="create"),
    path("<int:pk>/", views.DetailRoomView.as_view(), name="detail"),
    path("<int:pk>/update/", views.UpdateRoomView.as_view(), name="update"),
    path("<int:pk>/delete/", views.DeleteRoomView.as_view(), name="delete")
]
