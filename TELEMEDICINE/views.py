from django.shortcuts import render
from django.http import HttpResponse
import pyttsx3

def Lander(request,lang='en'):
    if(lang=='en'):
        content = {
            'govt_name':'Goverment of Kerala',
            'kiosk_name':' Welcome to AI assisted Tele Medicine Kiosk !',
            'type_text':'please select your role to continue',
            'citizen_text':'Citizen',
            'doctor_text':'Doctor'
        }

        obj1 = pyttsx3.init()
        obj1.setProperty('voice', 'en-UK')
        obj1.setProperty("rate", 155)
        obj1.say("Welcome to AI assisted telemdicine kiosk !")
        obj1.say("Please select your role to continue")
        obj1.runAndWait()
        return render(request,'Lander_Page.html',content)
    if(lang=='tel'):
        content = {
            'govt_name':'కేరళ ప్రభుత్వం',
            'kiosk_name':'కృతిమ మేధస్సు ఆధారిత టెలి మెడిసిన్ కియోస్క్ కి స్వాగతం !',
            'type_text':'మీరు ఎటువంటి యూజర్ అనేది  ఎంపిక చేస్కోండి ',
            'citizen_text':'పౌరుడు/పౌరురాలు',
            'doctor_text':'డాక్టర్ '
        }
        return render(request,'Lander_Page.html',content)
    
def Sample(request):
    return HttpResponse("hello")


    #return HttpResponse("This is home page with welcome text and doctor user button")
    #return render(request,'home_page.html')
