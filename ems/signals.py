from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from .models import Flight

@receiver(pre_save , sender = Flight)
def model_pre_change(sender, **kwargs):
    inst = kwargs['instance']
    print "in callback pre save"
    try:
        obj = sender.objects.get(pk=inst.pk)
    except sender.DoesNotExist:
        pass # object is new , so field hasn't technically changed

    else:
        if not obj.status == inst.status:
            inst.convey = 1
        else:
            inst.convey = 0
