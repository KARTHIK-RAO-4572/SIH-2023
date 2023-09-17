from django.shortcuts import render
from django.http import HttpResponse
def Lander(request):
    #return HttpResponse("This is home page with welcome text and doctor user button")
    return render(request,'home_page.html')
