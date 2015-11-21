from django.conf.urls import include, url
from .views import EventTrigger
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'', csrf_exempt(EventTrigger.as_view()), name='event'),
]
