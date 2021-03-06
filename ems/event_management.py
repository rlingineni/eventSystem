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

        msg = "Oh no, it seems that your flight %s %s is delayed. Don't worry, we think you can still make it. Let us know " \
              "if there are any updates "%(obj, obj.airline)
        print msg
        number = obj.journey.customer.mobile_number
        send_msg(msg, number)

    @staticmethod
    def on_flight_intimation(obj):

        msg = "Your plane departure is within one hour. We look forward to seeing you. Here is your confirmation %s"%(obj.airline)
        number = obj.journey.customer.mobile_number
        print msg
        send_msg(msg, number)

    @staticmethod
    def on_flight_landed(obj):
        event = obj.journey.event
        msg = "Welcome to your final destination! We can't wait to see you at %s. Let us know if there are any" \
              "questions "%(event.name)
        number = obj.journey.customer.mobile_number
        print msg
        send_msg(msg, number)

    @staticmethod
    def on_flight_ontime(obj):
        msg = "flight is on time %s - %s"%(obj, obj.departure.strftime('%d, %b %Y %H:%M'),)
        number = obj.journey.customer.mobile_number
        print msg
        send_msg(msg, number)

    @staticmethod
    def on_flight_added(obj):
        event = obj.journey.event
        msg = "Hey, thanks for sending in your trip Data. We look forward " \
              "to seeing you at %s on %s "%(event.name, event.date.strftime('%d, %b %Y %H:%M'))
        number = obj.journey.customer.mobile_number
        print msg
        send_msg(msg, number)