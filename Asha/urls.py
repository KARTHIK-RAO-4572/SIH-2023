from django.urls import path
from . import views

urlpatterns = [
    path('',views.Asha_Lander),
    path('/Validate',views.Login),
]