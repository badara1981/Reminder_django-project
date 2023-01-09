from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Reminder
from django.views.decorators.csrf import csrf_exempt
import json
def index(request):
    # Query The Reminders Tables
    # -Return JSON
    # -Return HTML
    reminders = Reminder.objects.all()
    print("@" * 38)
    print(reminders)
    empty_list = []
    for reminder in reminders:
        empty_list.append(
            {
                "id": reminder.id,
                "title": reminder.id,
                "description": reminder.description,
            }
        )
    # TODO: new_reminders
    #  CRFS Stand for Cross  Site Request Forgery 
@csrf_exempt
def new_reminder(request):
    
    # parse  json string
    data = json.loads(request.body)
    return HttpResponse("Hello World")
 
def html(request):
        reminders = Reminder.objects.all()
        return render(request,"reminders/index.html",dict(reminders=reminders))

 