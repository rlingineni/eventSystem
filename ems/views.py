from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from parseFlight import populateFlights, getUniqueID,process,reset
# Create your views here.

from .models import Customer
from event_management import Events

class EventTrigger(View):


    def get(self,request):
        return HttpResponse("Sample page")


    def post(self, request):
        print request.body
        process(request.body)
        flights = populateFlights()

        email = getUniqueID()
        print flights, email
        reset()

        ac = Customer.objects.filter(email=email).first()
        print "Customer ",ac
        if(ac != None):
            j = ac.journey_set.first()
            print " journey ",j
            for f in flights:
                print 'saving ',f
                f.journey = j
                f.save()
                Events.on_flight_added(f)

        return HttpResponse(request.body, content_type='application/xhtml+xml')
