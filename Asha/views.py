from django.shortcuts import render
from django.http import HttpResponse
from . import models
def Asha_Lander(request):
    return render(request,"Asha_Lander.html")

def Login(request):
    phn = request.POST['phon']
    passw = request.POST['password']
    try:
        record = models.Asha_Info.objects.get(phone=phn)
        if(record.password == passw):
            content = {
                "name":record.name,
                "phone":record.phone,
                "village":record.village

            }

            return render(request,"Asha_dashboard.html",content,)
        else:
            return render(request,"Wrong_Details_ASHA.html")
    except(models.Asha_Info.DoesNotExist):
        return render(request,"Wrong_Details_ASHA.html")
    
    