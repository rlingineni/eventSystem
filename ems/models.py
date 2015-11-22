from django.db import models
from datetime import datetime
from django.utils.timezone import now
# Create your models here.


class Events:

    REGISTRATION = 1
    FLIGHT_DELAY= 2
    FLIGHT_CANCEL = 3
    EVERY_MINUTE = 4

    @staticmethod
    def on_register(obj):
        print "On Register %s" %(obj)

    @staticmethod
    def on_every_minute(obj ):
        print "On Every minute %s"%(obj)

    @staticmethod
    def on_delay(obj):
        print "On Delay of event %s"%(obj)

    @staticmethod
    def on_cancelled(obj):
        print "On Cancelled of flight %s"%(obj)

    @staticmethod
    def on_delay_flight(obj):
        print "On delay flight %s"%(obj)


    @staticmethod
    def on_flight_intimation(obj):
        print "On flight intimation %s"%(obj,)

class Flight(models.Model):

    DEFAULT = 0
    ONTIME = 1
    LANDED = 2
    DELAY = 3
    CANCELLED = 4


    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    airline = models.CharField(max_length=10)
    departure = models.DateTimeField(default=now, blank=True)
    arrival = models.DateTimeField(default=now, blank=True)
    reference_no = models.CharField(max_length=20)
    status = models.IntegerField(default=0, blank=False)
    convey = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return '%s - %s'%(self.source, self.destination)


class CarTrip(models.Model):
    city = models.CharField(max_length=20)
    pickup = models.DateTimeField(default=now, blank=True)
    drop = models.DateTimeField(default=now, blank=True)
    type = models.CharField(max_length=20)
    confirmation_no = models.CharField(max_length=20)
    num_of_cars = models.IntegerField(default=1)

    def __str__(self):
        return '%s'%(self.confirmation_no)


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

    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=now, blank=True)
    status = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return "%s"%(self.name,);


class Journey(models.Model):
    event = models.ForeignKey(Event, default=1)
    customer = models.ForeignKey(Customer)
    flight = models.ForeignKey(Flight)
    car = models.ForeignKey(CarTrip)

    def __str__(self):
        return '%s'%(self.customer)

