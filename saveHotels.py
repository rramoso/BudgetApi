from requests.auth import HTTPDigestAuth
from django.conf import settings
from helpers import *
import os
import django
import requests
import json

EXPEDIA = "http://terminal2.expedia.com/x/mhotels/search?city={}&checkInDate=2016-08-16&checkOutDate=2016-08-19&room1=2&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"
GOOGLE_PLACES_KEY = ""
cities = ["PUJ","STI","SDQ","SFO","CDMX"]


hotelList = []
hotelNames = []
for city in cities: 
	r = requests.get(EXPEDIA.format(city))
	print json.loads(r.content)
	city =  json.loads(r.content)
	for num,i in enumerate(city['hotelList']):
		name = i['name']
		city = i['city']
		idHotel = i['hotelId']
		try:
			hotelList.append(idHotel)
			hotelNames.append(name)
		except Exception as e:
			hotelNames.append(name.encode('utf-8'))

hotelByID = "http://terminal2.expedia.com/x/mhotels/info?hotelId=%s&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"
aux = {}
result = {}
n = 0
for hId in hotelList:
	r = requests.get(hotelByID%hId)
	try:
		content = json.loads(r.content)
	except Exception as e:
		hotelList.append(hId)
		continue
	
	if len(Tblhotel.objects.filter(hotelid = hId)) > 0:
		print hId
		continue
	hotel_location = checkAPILocation(content['latitude'],content['longitude'],content['hotelAddress'],content['hotelCountry'],content['hotelCity'])#lat,log,address,country,city
	h = Tblhotel.objects.create( 
		hotelid = content['hotelId'],
		hotelname = content['hotelName'],
		hotelphonenumber = content['telesalesNumber'],
		hoteladdress = hotel_location,
		hotelcity = hotel_location.lcity,
		hotelcountry = hotel_location.lcountry,
		hotelrating = 5)
	h.save()
	n = n+1
	print n


