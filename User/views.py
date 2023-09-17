from django.shortcuts import render
from django.http import HttpResponse
def User_lander(request):
    return render(request,"user_home.html")
