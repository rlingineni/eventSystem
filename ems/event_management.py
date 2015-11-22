from twilio.rest import TwilioRestClient
from datetime import datetime
# put your own credentials here
ACCOUNT_SID = "AC0c70347420364a9d4d3ee9d78ce0f31a"
AUTH_TOKEN = "da05a42d0afb1ccf5043b19467b73f6a"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def send_msg(msg, number):
    client.messages.create(
	    to=number,
	    from_="+18179853232",
	    body=msg,
    )

class Events:

    @staticmethod
    def on_register(obj):
        print "On Register %s" %(obj)
        msg="Thank you for registering. Contact xxx for more information"
        number = obj.customer.mobile_number
        send_msg(msg, number)

    @staticmethod
    def on_cancel_event(obj):
        number = obj.journey_set.first().customer.mobile_number
        msg = "Event %s is cancelled "%(obj,)
        print msg
        send_msg(msg, number)

    @staticmethod
    def on_delay(obj):
        print "On Delay of event %s"%(obj)
        number = obj.journey_set.first().customer.mobile_number
        msg = "Event is delayed to %s"%(obj.date.strftime('%d, %b %Y %H:%M'),)
        print msg
        send_msg(msg, number)

    @staticmethod
    def on_cancelled(obj):
        print "On Cancelled of flight %s"%(obj)
        msg = "flight is cancelled %s"%(obj)
        print msg
        number = obj.journey.customer.mobile_number
        send_msg(msg, number)

    @staticmethod
    def on_delay_flight(obj):

        msg = "flight is delayed %s"%(obj,)
        print msg
        number = obj.journey.customer.mobile_number
        send_msg(msg, number)

    @staticmethod
    def on_flight_intimation(obj):

        msg = "flight about to take off %s"%(obj)
        number = obj.journey.customer.mobile_number
        print msg
        send_msg(msg, number)

    @staticmethod
    def on_flight_landed(obj):
        msg = "flight landed %s"%(obj)
        number = obj.journey.customer.mobile_number
        print msg
        send_msg(msg, number)

    @staticmethod
    def on_flight_ontime(obj):
        msg = "flight is on time %s - %s"%(obj, obj.departure.strftime('%d, %b %Y %H:%M'),)
        number = obj.journey.customer.mobile_number
        print msg
        send_msg(msg, number)