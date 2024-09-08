from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  ## Triggers the function passed into it
    path('room/<str:pk>/', views.room, name="room"),
]
