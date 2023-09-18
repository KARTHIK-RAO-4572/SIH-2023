from django.urls import path
from . import views

urlpatterns = [
    path('',views.Doctor_lander),
    path('Validate/',views.Login),
]