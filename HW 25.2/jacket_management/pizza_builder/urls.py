from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.pizza_view, name='pizza_create'),
]
