from requests.auth import HTTPDigestAuth
from django.conf import settings
from django.utils import timezone
from datetime import datetime
import dateutil.parser
import os, django, requests, json
os.environ['DJANGO_SETTINGS_MODULE'] = 'BudgetApi.settings'
django.setup()
from main.models import *

UNAVAILABLE = "No disponible"

def checkAPILocation(lat,log,address,country,city):
	
	loct = Tbllocation.objects.filter(latitude=lat,longitud=log)
	if(len(loct) > 0):
		return loct[0]
	idCountry = checkCountry(country)
	idCity = checkCity(city,idCountry)
	loct = Tbllocation.objects.create(
		locationid = lat+log,
		streetname = address,
		state = "",
		zipcode = "",
		lcountry = idCountry,
		lcity = idCity,
		longitud = log,
		latitude = lat)
	loct.save()
	return loct

def checkCity(city,idCountry):
	
	check_city = Tblcity.objects.filter(cityname = city)
	if(len(check_city)>0):
		return check_city[0]
	check_city = Tblcity.objects.create(
		cityid = "id_"+city,
		cityname= city,
		countryid = idCountry)
	check_city.save()
	return check_city

def checkCountry(country):
	
	check_country = Tblcountry.objects.filter(countryname = country)
	if(len(check_country)>0):
		return check_country[0]
	check_country = Tblcountry.objects.create(
		countryid = "id_"+country,
		countryname = country,
		continent = UNAVAILABLE,
		countrycode = UNAVAILABLE)
	check_country.save()
	return check_country

def hotelsByCity(city):
	return Tblhotel.objects.filter(hotelcity__cityname=city)

def checkAirline():
	pass

def checkAirport():
	pass

def checkAirplane():
	pass

def checkFlight():
	pass

def checkTransportation():
	pass

def createOfferByHotel(hotel,hotel_offer_start,end_day,hotel_offer_prices):
	
	offer = Tbloffer.objects.create(
		offerid = hotel.hotelid+"_"+hotel_offer_start+"_"+end_day,
		hotelid = hotel.hotelid,
		hotelname = hotel.hotelname,
		hotelcountry= hotel.hotelcountry.countryname,
		hotelcity = hotel.hotelcity.cityname,
		hotelexpense = str(hotel_offer_prices),
		startdate = datetime(2015, 6, 15, 23, 30, 1, tzinfo=timezone.utc),
		enddate = datetime(2015, 6, 15, 23, 30, 1, tzinfo=timezone.utc))
	
	offer.save()

def createOfferByHotelPrice(offers):
	price_hotel = []
	for offer in offers:
		price_hotel.append(int(offer['rateInfo']['chargeableRateInfo']['priceToShowUsers']))
	return price_hotel

def expediaActivityOffers(offers):

	result = {}
	for offer in offers['offers']:
		for i in offer['availabilityInfo']:
			prices = ""
			for j in i['tickets']:
				 prices += j['code']+':'+j['price']+','
			result[i['availabilities']['valueDate']] = prices
	
	return result