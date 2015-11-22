from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from .models import Flight, Journey,Event
from event_management import Events

@receiver(pre_save , sender = Flight)
@receiver(pre_save, sender=Event)
def model_pre_change(sender, **kwargs):
    inst = kwargs['instance']
    print "in callback pre save "

    try:
        obj = sender.objects.get(pk=inst.pk)
    except sender.DoesNotExist:
        pass # object is new , so field hasn't technically changed

    else:
        print "oldstatus",obj.status, "new status ",inst.status
        if obj.status != inst.status:
            inst.convey = 0

@receiver(post_save, sender = Journey )
def model_post_save(sender, **kwargs):
    instance = kwargs['instance']
    Events.on_register(instance)