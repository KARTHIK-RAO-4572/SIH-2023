from django.urls import path
from . import views

urlpatterns = [
    path('',views.User_lander),
]