from django.core.management.base import BaseCommand, CommandError
from ems.models import Journey, Events,Flight


class Command(BaseCommand):
    help = " Flight Delay events "

    def handle(self, *args, **kwargs):
        # get the list of objects which are created within 1 minute
        jobj = Journey.objects.filter(flight__status = Flight.DELAY)

        # in all list of objects trigger event
        for j in jobj:
            # check which event is it
            Events.on_delay_flight(j)
            self.stdout.write("Successfully sent flight delay event on %s"%(j,))