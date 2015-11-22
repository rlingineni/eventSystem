from django.core.management.base import BaseCommand, CommandError
from ems.models import Journey, Flight
from ems.event_management import Events
from datetime import datetime, timedelta

#intimate the user before flight time

class Command(BaseCommand):
    help = " Flight Intimation events "

    def handle(self, *args, **kwargs):
        # get the list of objects which are created within 1 minute
        flights = Flight.objects.filter(departure__gt = datetime.now() + timedelta(hours=1)).exclude(convey=1)

        # in all list of objects trigger event
        for j in flights:
            # check which event is it
            Events.on_flight_intimation(j)
            self.stdout.write("Successfully registered event on %s"%(j,))
            Flight.objects.filter(pk=j.pk).update(convey =1)