from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from parseFlight import populateFlights, getUniqueID,process
# Create your views here.

from .models import Customer


class EventTrigger(View):


    def get(self,request):
        return HttpResponse("Sample page")


    def post(self, request):
        print request.body
        process(request.body)
        flights = populateFlights()
        email = getUniqueID()
        print flights, email

        ac = Customer.get(email=email)
        if(ac != None):
            j = ac.journey
            for f in flights:
                f.journey = j
                f.save()
        
        return HttpResponse(request.body, content_type='application/xhtml+xml')
