from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
import pyttsx3

def Doctor_Lander(request):
    return render(request,'Doctor_Login.html')

def Login(request):
    ID = request.POST['doc_id']
    passw = request.POST['password']
    try:
        record = models.Doctor_Info.objects.get(doc_id=ID)
        if(record.doc_pass == passw):
            return render(request,"Doctor_dash.html")
        else:
            return render(request,"Wrong_Details_doc.html")
    except(models.Doctor_Info.DoesNotExist):
        return render(request,"Wrong_Details_doc.html")
    

