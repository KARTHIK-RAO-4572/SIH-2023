from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models

def Doctor_Lander(request):
    return render(request,'Doctor_Login.html')

def Login(request):
    ID = request.POST['doc_id']
    passw = request.POST['password']
    try:
        record = models.Doctor_Info.objects.get(doc_id=ID)
        if(record.doc_pass == passw):
            return HttpResponseRedirect("http://127.0.0.1:8000/Doctor/dashboard"+"?"+str(ID))
        else:
            return HttpResponse("Wrong bro")
    except(DoesNotExist):
        return HttpResponse("Wrong password")
    

