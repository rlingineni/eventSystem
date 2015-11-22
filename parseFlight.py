import xml.etree.ElementTree as ET
import urllib2
import django
import flightQuery 
import json
from ems.models import Flight


tree = ET.parse('tripData.xml')
departPlaces = []
bookingReferences = []
departTimes = []
arrivalPlaces = []
arrivalTimes = []
flightCodes = []
flights = []

def getUniqueID():
	root = tree.getroot()
	root = root[2][0]
	e_mail = root.get('value')
	e_mail = e_mail.rstrip('>')
	e_mail = e_mail.lstrip('<')
	print e_mail

def getDeparaturePlace():
	root = tree.getroot()
	root = root[5];
	for item in root:
		if(item.tag == "flight"):
			departPlaces.append(item[5][2].text)
		
def getDepartTimes():
	root = tree.getroot()
	root = root[5];
	for item in root:
		if(item.tag == "flight"):
		 	departTimes.append(item[5][6].text)

def getArrivalTimes():
	root = tree.getroot()
	root = root[5];
	for item in root:
		if(item.tag == "flight"):
			arrivalTimes.append(item[6][6].text)

def getArrivalPlace():
	root = tree.getroot()
	root = root[5];
	for item in root:
		if(item.tag == "flight"):
			arrivalPlaces.append(item[6][2].text)

def getFlightInfo():
	root = tree.getroot()
	root = root[5];
	for item in root:
		if(item.tag == "flight"):
			number = item[4].get('number')
			code = item[4].get('airline-code')
			flightcode = code + number
			flightCodes.append(flightcode)

def getReference():
	root = tree.getroot()
	root = root[5]
	for item in root:
		if(item.tag == "flight"):
			reference = item[1][1].text
			bookingReferences.append(reference)

def populateFlights():
	root = tree.getroot()
	root = root[5]
	for index,item in enumerate(root):
		tempflight = Flight()
		tempflight.source = departPlaces[index]
		tempflight.destination = arrivalPlaces[index]
		tempflight.airline = flightCodes[index]
		tempflight.departure = departTimes[index]
		tempflight.arrival = arrivalTimes[index]
		tempflight.reference_no = bookingReferences[index]
		tempflight.save()
		flights.append(tempflight)
		return flights

''' getUniqueID();
getDeparaturePlace();
getArrivalPlace();
getArrivalTimes();
getDepartTimes();
getFlightInfo();
getReference();

populateFlights();  '''

#flightQuery.getFlightStatus(flights[1]);



