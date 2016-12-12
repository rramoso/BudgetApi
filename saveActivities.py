from requests.auth import HTTPDigestAuth
from django.conf import settings
from helpers import *
import sys, django, requests, json, datetime


# No crear cada actividad por fecha sino muchas ofertas teniendo diferentes.

EXPEDIA = "http://terminal2.expedia.com/x/activities/search?location={}&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"
EXPEDIA_ACT = "http://terminal2.expedia.com:80/x/activities/details?activityId={}&startDate={}&endDate={}&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"
# "PUJ":"DOM","STI":"DOM","SDQ":"DOM","SFO":"USA"
startDate = datetime.datetime.now().strftime("%Y-%m-%d")
Tblactivity.objects.filter(acdate__lt=startDate).delete()
endDate = datetime.datetime.now() + datetime.timedelta(days=7)
endDate = endDate.strftime("%Y-%m-%d")

cities = {"Santo Domingo":"DOM"}#"Santo Domingo":"DOM", "Santiago de los Caballeros":"DOM","Punta Cana":"DOM"}
activitiesIDs = []
for city in cities: 
	r = requests.get(EXPEDIA.format(city))
	try:
		content = json.loads(r.content)
	except Exception as e:
		continue
	for activity in content["activities"]:
		activitiesIDs.append(activity['id'])

for actId in activitiesIDs:

	r = requests.get(EXPEDIA_ACT.format(actId,startDate,endDate))
	try:
		content = json.loads(r.content)

	except Exception as e:
		activitiesIDs.append(actId)
		continue
	if len(Tblactivity.objects.filter(activityid = actId)) > 0:
			print Tblactivity.objects.get(activityid = actId).actype,actId
			continue
	prices_by_date = expediaActivityOffers(content['offersDetail'])
	latLng = content["latLng"].split(',')

	try:
		location = checkAPILocation(latLng[0],latLng[1],content['address'],"DOM","Santo Domingo")
		print location.lcity.cityname
	except Exception as e:
		continue
	try: 
		duration = content['duration']
	except:
		duration = UNAVAILABLE
	act = Tblactivity.objects.create(
			activityid = actId,
			actype = str(content['category']),
			acname = content["title"],
			acdescription = content["description"] if content["description"] is not None else "No disponible",
			acdate = content["startDate"],
			acbegintime = duration,
			accost = str(prices_by_date),
			aclocation = location)
	act.save()



