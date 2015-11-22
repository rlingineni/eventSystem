from django.core.management.base import BaseCommand, CommandError
from ems.models import Journey, Event
from ems.event_management import Events


class Command(BaseCommand):
    help = " Flight Delay events "

    def handle(self, *args, **kwargs):
        # get the list of objects which are created within 1 minute
        events = Event.objects.filter(event__status= Event.DELAY)

        # in all list of objects trigger event
        for j in events:
            # check which event is it
            Events.on_delay(j)
            self.stdout.write("Successfully sent event delay event on %s"%(j,))

            Event.objects.filter(pk=j.pk).update(convey =1)