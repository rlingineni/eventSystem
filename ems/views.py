from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class EventTrigger(View):


    def get(self,request):
        return HttpResponse("Sample page")


    def post(self, request):
        print request.body
        return HttpResponse(request.body, content_type='application/xhtml+xml')
