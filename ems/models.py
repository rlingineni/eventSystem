from django.db import models

# Create your models here.


class Flight(models.Model):

    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    airline = models.CharField(max_length=10)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    reference_no = models.CharField(max_length=20)

    def __str__(self):
        return '%s - %s'%(self.source, self.destination)


class CarTrip(models.Model):
    city = models.CharField(max_length=20)
    pickup = models.DateTimeField()
    drop = models.DateTimeField()
    type = models.CharField(max_length=20)
    confirmation_no = models.CharField(max_length=20)
    num_of_cars = models.IntegerField()

    def __str__(self):
        return '%s'%(self.confirmation_no)


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_number = models.IntegerField('Phone Number')
    trip_type = models.CharField(max_length=10)

    def __str__(self):
        return '%s-%s'%(self.first_name, self.last_name)


class Journey(models.Model):
    customer = models.ForeignKey(Customer)
    flight = models.ForeignKey(Flight)
    car = models.ForeignKey(CarTrip)

    def __str__(self):
        return '%s'%(self.customer)