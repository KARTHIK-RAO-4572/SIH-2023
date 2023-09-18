from django.shortcuts import render
from django.http import HttpResponse

def Doctor_lander(request):
    return render(request,'doctor_home.html')

def Login(request):
    ID = request.POST['doc_id']
    passw = request.POST['password']
    return HttpResponse(str(ID)+passw) 
