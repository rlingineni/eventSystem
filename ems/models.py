from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.db.models.signals import pre_save

# Create your models here.



class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_number = models.IntegerField('Phone Number')
    trip_type = models.CharField(max_length=10)

    def __str__(self):
        return '%s-%s'%(self.first_name, self.last_name)


class Event(models.Model):

    DEFAULT = 0
    ONTIME = 1
    CANCELLED = 2
    DELAY = 3

    MSG_CONVEYED = (
        (0, 'Message Due'),
        (1, 'No New Message'),
    )

    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=now, blank=True)
    status = models.IntegerField(default=0, blank=False)
    convey = models.IntegerField(default=0, blank=False, choices=MSG_CONVEYED)

    def __str__(self):
        return "%s"%(self.name,)


class Journey(models.Model):
    event = models.ForeignKey(Event, default=1)
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return '%s'%(self.customer)


class Flight(models.Model):
    STATUSES = (
        (0, 'Default'),
        (1, 'OnTime'),
        (2, 'Landed'),
        (3, 'Delay'),
        (4, 'Cancelled'),
    )

    MSG_CONVEYED = (
        (0, 'Message Due'),
        (1, 'No New Message'),
    )


    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    airline = models.CharField(max_length=10)
    departure = models.DateTimeField(default=now, blank=True)
    arrival = models.DateTimeField(default=now, blank=True)
    reference_no = models.CharField(max_length=20)
    status = models.IntegerField(default=0, blank=False, choices=STATUSES)
    convey = models.IntegerField(default=0, blank=False, choices=MSG_CONVEYED)

    journey = models.ForeignKey(Journey)

    def __str__(self):
        return '%s - %s'%(self.source, self.destination)



class CarTrip(models.Model):
    city = models.CharField(max_length=20)
    pickup = models.DateTimeField(default=now, blank=True)
    drop = models.DateTimeField(default=now, blank=True)
    type = models.CharField(max_length=20)
    confirmation_no = models.CharField(max_length=20)
    num_of_cars = models.IntegerField()

    journey = models.ForeignKey(Journey, default=0)

    def __str__(self):
        return '%s'%(self.confirmation_no)



