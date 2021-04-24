from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.home),
    path('order/', views.order, name="order"),


]
