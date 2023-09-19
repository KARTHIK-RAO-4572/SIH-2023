from django.urls import path
from . import views

urlpatterns = [
    path('',views.Doctor_Lander),
    path('/Validate',views.Login),
]