from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC0c70347420364a9d4d3ee9d78ce0f31a"
AUTH_TOKEN = "da05a42d0afb1ccf5043b19467b73f6a"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def send_msg(msg):
    client.messages.create(
	    to="9724087652",
	    from_="+18179853232",
	    body=msg,
    )

class Events:

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

        msg = "flight is delayed %s"%(obj,)
        print msg
        send_msg(msg)

    @staticmethod
    def on_flight_intimation(obj):

        msg = "flight about to take off %s"%(obj)
        print msg
        send_msg(msg)
