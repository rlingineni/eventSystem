from django.conf.urls import include, url
from .views import EventTrigger

urlpatterns = [
    url(r'', EventTrigger.as_view(), name='event'),
]
