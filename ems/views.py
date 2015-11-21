from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class EventTrigger(View):

    def get(self,request):
        print HttpResponse("Sample page")

    def post(self, request):
        print HttpResponse(request.body, content_type='application/xhtml+xml')
