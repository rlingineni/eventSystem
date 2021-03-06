from django.core.management.base import BaseCommand, CommandError
from ems.models import Journey, Flight
from django.db.models import F
from ems.event_management import Events

class Command(BaseCommand):
    help = " Flight Delay events "

    def handle(self, *args, **kwargs):
        # get the list of objects which are created within 1 minute
        flights = Flight.objects.filter(status=2).exclude(convey=1)

        # in all list of objects trigger event
        for j in flights:
            # check which event is it
            Events.on_flight_landed(j)
            self.stdout.write("Successfully sent flight landed event on %s"%(j,))
            Flight.objects.filter(pk=j.pk).update(convey =1)