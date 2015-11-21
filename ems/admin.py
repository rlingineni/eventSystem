from django.contrib import admin
from .models import Flight, CarTrip, Customer, Journey
# Register your models here.


admin.site.register(Journey)
admin.site.register(Flight)
admin.site.register(Customer)
admin.site.register(CarTrip)
