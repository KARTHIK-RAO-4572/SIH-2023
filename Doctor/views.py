from django.shortcuts import render
from django.http import HttpResponse

def Doctor_lander(request):
    return render(request,'doctor_home.html')
