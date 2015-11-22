import urllib2
import django
import json
from ems.models import Flight

def getFlightStatus(flight):
    code = flight.airline
    requestUrl = "https://api.import.io/store/data/c3444b67-8ff2-43e1-ac0b-c242b12f0951/_query?input/webpage/url=https%3A%2F%2Fflightaware.com%2Flive%2Fflight%2F"+code+"&_user=021a8fdc-5921-4f4e-8db9-97de66fb0973&_apikey=021a8fdc59214f4e8db997de66fb09734153437fcc9a8d2a95258d400b3dea39e1780069bca4b584ecc4c9a8e09255e7d3c95a9553cd69d6eaa38dd84f25bfd99284d379f33cd6d0c1cf1a6f00a7b16b"
    content = urllib2.urlopen(requestUrl, timeout=10).read()
    try:
        lst = parseJson(content)
    except:
        lst = ["", "ontime", 1, 0, 0, 0]
    return lst

def parseJson(content):
    parsed_json = json.loads(content)
    st = getStatusString(parsed_json['results'][0]['content'])

    prestatus = determinePreStatus(parsed_json['results'][0]['content'])
    currentstatus = determineCurrentStatus(parsed_json['results'][0]['content'])
    poststatus = determinePostStatus(parsed_json['results'][0]['content'])
    delaystatus = determineDelayStatus(parsed_json['results'][0]['content'])
    return [st, parsed_json['results'][0], prestatus, currentstatus, poststatus, delaystatus ]

def determineCurrentStatus(status):
    substring = "On Time"
    if substring in status:
        return 0
    else:
        return 1

def determinePreStatus(status):
    substring = "Scheduled"
    if substring in status:
        return 1
    else:
        return 0

def determinePostStatus(status):
    substring = "Arrived"
    if substring in status or "Landed" in status:
        return 1
    else:
        return 0

def getStatusString(status):
    return status

def determineDelayStatus(status):
    substring = "Delayed"
    if substring in status:
        return 1
    else:
        return 0

