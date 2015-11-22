from django.core.management.base import BaseCommand, CommandError
from ems.models import Journey, Events
from datetime import datetime, timedelta

#intimate the user before flight time

class Command(BaseCommand):
    help = " Flight Intimation events "

    def handle(self, *args, **kwargs):
        # get the list of objects which are created within 1 minute
        jobj = Journey.objects.filter(flight__departure__lt = datetime.now() - timedelta(hours=1)).exclude(status = convey)

        # in all list of objects trigger event
        for j in jobj:
            # check which event is it
            Events.on_flight_intimation(j)
            j.convey=j.status
            j.save()
            self.stdout.write("Successfully registered event on %s"%(j,))