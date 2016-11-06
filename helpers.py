from requests.auth import HTTPDigestAuth
from django.conf import settings
from django.utils import timezone
from datetime import datetime
import dateutil.parser, ast
import urllib3,os, django, requests, json, datetime,re, calendar
os.environ['DJANGO_SETTINGS_MODULE'] = 'BudgetApi.settings'
django.setup()
from main.models import *

UNAVAILABLE = "No disponible"
COUNTRY_BY_CODE = "https://restcountries.eu/rest/v1/alpha?codes={}"
DISTANCE_BY_LATLNG = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode={}&language=en-EN&key=AIzaSyBQ1HrMPB8GipRSP7VteAWWgGR1mM2lf1k"
urllib3.disable_warnings()
		
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
	
	check_country = Tblcountry.objects.filter(countrycode = country)
	if(len(check_country)>0):
		return check_country[0]

	r = requests.get(COUNTRY_BY_CODE.format(country))
	content =  json.loads(r.content)
	
	check_country = Tblcountry.objects.create(
		countryid = "id_"+country,
		countryname = content[0]["name"],
		continent = content[0]["region"],
		countrycode = country)
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

def intPrices(budget,hotelexpense,days):

	prices = []
	
	for price in re.split('[\[,\,,\]]',hotelexpense):
		try:
			if int(price)*days <= budget:
				prices.append(price)
				continue
		except:
			continue
	return prices

def createOffersToUser(begin_time,end_time, budget, city,preferences):
	urllib3.disable_warnings()
		
	print begin_time,end_time
	hotel_money_limit = budget*0.5
	activities_money = budget*0.125
	restaurant_money = budget*0.25	 
	
	selectedOffers = []
	selectedActivities = []
	hotelsActivity = {}
	
	hotel_offers = Tbloffer.objects.filter(startdate__gte = begin_time,enddate__lte = end_time, hotelcity = city.cityname)
	number_of_days = (begin_time - end_time).days * -1

	#Get activities by preferences
	for preference in preferences:
		selectedActivities += Tblactivity.objects.filter(aclocation__lcity = city,actype = preference)
	
	#Get hotels by price limit
	for offer in hotel_offers:
		prices = intPrices(hotel_money_limit,offer.hotelexpense,number_of_days)
		if prices != []:
			selectedOffers.append(offer)
	
	#Asigning activities to hotel by arrival time
	for offer in selectedOffers:
		hotelsActivity[offer.offerid] = activitiesByHotel(offer.hotelid,selectedActivities)
	return hotelsActivity
	#Creating itinerary
	# createItinerary(hotelsActivity,begin_time,end_time)
	
def createItinerary(hotelsActivity,begin_time,end_time,days):

	itinerary = {}
	regular_activity_start_hour,regular_activity_end_hour = 8,20
	itinerary[begin_time.hour],itinerary[end_time.hour] = 'Hotel Arrival', 'End of Offer'
	while days > 0:

		for offer in hotelsActivity:
			print offer
			for activityid in hotelsActivity[offer]:

				act = Tblactivity.objects.get(activityid = activityid)
				if act.accost != None:
					for date in act.accost:
						if date > begin_time:
							print date
		days -= 1

def activitiesByHotel(hotelid,activities):

	result = {}

	offer_location = Tblhotel.objects.get(hotelid = hotelid).hoteladdress
	origin = str(offer_location.latitude)+','+str(offer_location.longitud)
		
	for act in activities:
		destination = str(act.aclocation.latitude)+','+str(act.aclocation.longitud)
		r = requests.get(DISTANCE_BY_LATLNG.format(origin,destination,'driving'))
		try: 
			arrival_time = json.loads(r.content)['rows'][0]['elements'][0]['duration']['text']
		except:
			pass
		if 'hour' not in arrival_time:
			result[act.activityid] = arrival_time
	return result

def createOfferByActivities(activities):

	for activity in activities:
		
		costs = ast.literal_eval(activity.accost)
		for date in costs:
			print lol[i].split(',')


def createRestaurant(location,restaurant):
	if len(Tblrestaurant.objects.filter(restaurantid = restaurant['place_id']))>0:
		pass
	else:
		r =  Tblrestaurant.objects.create(
			restaurantid = restaurant['place_id'],
			restaurantname = restaurant['name'],
			rtphonenumber = restaurant['international_phone_number'],
			rtaddress = location,
			rtcity = location.lcity,
			rtcuisine = UNAVAILABLE,
			rtrating = restaurant['rating'],
			rtcountry = location.lcountry,
			cuisineid = None)
		r.save()

def createOfferByHotel(hotel,hotel_offer_start,end_day,hotel_offer_prices):
	
	offer = Tbloffer.objects.filter(offerid=hotel.hotelid+"_"+hotel_offer_start+"_"+end_day)
	if len(offer) > 0:
		return offer[0]
	endday = end_day.split('-')
	startdate = hotel_offer_start.split('-')
	print "\t\t\t",endday,startdate
	new_offer = Tbloffer.objects.create(
		offerid = hotel.hotelid+"_"+hotel_offer_start+"_"+end_day,
		hotelid = hotel.hotelid,
		hotelname = hotel.hotelname,
		hotelcountry= hotel.hotelcountry.countryname,
		hotelcity = hotel.hotelcity.cityname,
		hotelexpense = str(hotel_offer_prices),
		startdate = datetime(int(startdate[0]), int(startdate[1]), int(startdate[2]), 23, 30, 1, tzinfo=timezone.utc),
		enddate = datetime(int(endday[0]), int(endday[1]), int(endday[2]), 23, 30, 1, tzinfo=timezone.utc))
	
	new_offer.save()
	return new_offer

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

def createActivityGooglePlaces(location,activity):
	
	if len(Tblactivity.objects.filter(activityid=activity['place_id'])) > 0:
		pass
	else:
		
		act = Tblactivity.objects.create(
			activityid = activity['place_id'],
			actype = activity['type'],
			acname = activity['name'],
			acdescription = activity['international_phone_number'],
			accost = activity['price_level'],
			acbegintime = activity['hours'],
			acendtime = UNAVAILABLE,
			acstatus = UNAVAILABLE,
			acdate = None,
			acrating = activity['rating'],
			aclocation = location)

		act.save()



