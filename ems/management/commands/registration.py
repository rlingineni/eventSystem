from django.core.management.base import BaseCommand, CommandError
from ems.models import Journey, Events


class Command(BaseCommand):
    help = " Registration events "

    def handle(self, *args, **kwargs):
        # get the list of objects which are created within 1 minute
        jobj = Journey.objects.all()

        # in all list of objects trigger event
        for j in jobj:
            # check which event is it
            Events.on_register(j)
            self.stdout.write("Successfully registered event on %s"%(j,))