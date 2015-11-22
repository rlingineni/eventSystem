from django.core.management.base import BaseCommand, CommandError
from ems.models import Journey, Flight
from django.db.models import F
from ems.event_management import Events

from flightQuery import getFlightStatus
class Command(BaseCommand):
    help = " Flight Delay events "

    def handle(self, *args, **kwargs):
        # get the list of objects which are created within 1 minute
        jobjs = Journey.objects.filter(status=1)

        # in all list of objects trigger event
        for j in jobjs:
            flights = j.flight_set.all()
            for f in flights:
                lst = getFlightStatus(f)
                print lst
                if lst and lst[0] != None:
                    f.statusstr = lst[0]
                    if(lst[3] == 1):
                        #on time
                        f.status = 1
                    if(lst[2] == 1):
                        # delay
                        f.status = 3
                    if(lst[4] == 1):
                        # landed
                        f.status = 2
                    if(lst[5] == 1):
                        f.status = 4
                    f.save()

                self.stdout.write("query flight %s"%(f,))
            #Flight.objects.filter(pk=j.pk).update(convey =1)