from requests.auth import HTTPDigestAuth
from django.conf import settings
from django.utils import timezone
from datetime import datetime,timedelta
import dateutil.parser, ast
import os, django, requests, json,datetime,re, calendar
os.environ['DJANGO_SETTINGS_MODULE'] = 'BudgetApi.settings'
django.setup()
from main.models import *

UNAVAILABLE = "No disponible"
COUNTRY_BY_CODE = "https://restcountries.eu/rest/v1/alpha?codes={}"
DISTANCE_BY_LATLNG = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode={}&language=en-EN&key=AIzaSyBtj4q8RrfxwVZoQQ1iBeaJ4U7XBrEWkEk"
		
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

	prices = {}
	
	for price in ast.literal_eval(hotelexpense).keys():
		try:
			if int(price)*days <= budget:
				prices[int(price)] = hotelexpense[price]
				continue
		except:
			continue
	return prices

def createOffersToUser(begin_time,end_time, budget, city,preferences):
		
	hotel_money_limit = budget*0.5
	activities_money = budget*0.125
	restaurant_money = budget*0.25	 
	
	selectedOffers = []
	selectedActivities = []
	hotelsActivity = {}
	
	hotel_offers = Tbloffer.objects.filter(startdate__lte = begin_time,enddate__gte = end_time, hotelcity = city.cityname)
	number_of_days = (begin_time - end_time).days * -1
	
	#Get activities by preferences
	for preference in preferences:
		selectedActivities += Tblactivity.objects.filter(aclocation__lcity = city,actype = preference)
	
	#Get hotels by price limit
	for offer in hotel_offers:
		prices = intPrices(hotel_money_limit,offer.hotelexpense,number_of_days)
		if prices != {}:
			selectedOffers.append(offer)
	print selectedOffers
	#Filter activities by price limit	
	selectedActivities = activitiesByPrice(selectedActivities,activities_money,{"Adult":1})
	
	# # Asigning activities to hotel by arrival time
	for offer in selectedOffers:
		hotelsActivity[offer.offerid] = activitiesByHotel(offer.hotelid,selectedActivities)
	
	# #Creating itinerary
	offersItinerary = createItinerary(hotelsActivity,begin_time,end_time,number_of_days)
	print 'offersItinerary\n\t',offersItinerary
	return offersItinerary
	
def createItinerary(hotelsActivity,begin_time,end_time,days):

	
	regular_activity_start_hour,regular_activity_end_hour = 8,20
	print hotelsActivity
	
	google_places = []
	result = {}
	for offer in hotelsActivity:
		itinerary = {}
		itinerary[begin_time.strftime("%Y-%m-%d %H:%M:%S")],itinerary[end_time.strftime("%Y-%m-%d %H:%M:%S")] = 'Hotel Arrival', 'End of Offer'
		for activityid in hotelsActivity[offer]:

			act = Tblactivity.objects.get(activityid = activityid)
			print act.acname,act.accost
			if act.accost != None:
				dates = ast.literal_eval(act.accost).keys()
				for date in dates:

					date = datetime.datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
					if date.strftime("%Y-%m-%d %H:%M:%S") not in itinerary and act.acname not in itinerary.values() and date > begin_time and date < end_time:
						duration = 'AAAAHHHH',act.acbegintime.split('h')
						duration = int(act.acbegintime.split('h')[0]) if 'm' not in act.acbegintime.split('h')[0] else 1
						print '\tduration:',duration
						if date+timedelta(hours=duration) < end_time:
							for hour in range(duration):
								itinerary[(date+timedelta(hours=hour)).strftime("%Y-%m-%d %H:%M:%S")] = act.acname
						break
			else:
				google_places.append(act)
		result[offer] = itinerary
	
	for place in google_places:
		pass

	return result

def activitiesByPrice(selectedActivities,price_limit,people):
	
	activitiesSelected = []
	for act in selectedActivities:
		try:
			activities = ast.literal_eval(act.accost)
			for costs in activities.values():
				for cost in costs.split(','):
					for c in costs.split(','):
						i = c.split('$')
						for key in people.keys():
							print act.acname,key,int(i[1]),price_limit,people[key]*int(i[1]) <= price_limit
							if key in i[0] and people[key]*int(i[1]) <= price_limit:
								activitiesSelected.append(act) 
		except Exception as e:
			print e		
	return activitiesSelected	


def activitiesByHotel(hotelid,activities):

	result = {}
	print 'Desde activitiesByHotel this is ... ', hotelid
	offer_location = Tblhotel.objects.get(hotelid = hotelid).hoteladdress
	origin = str(offer_location.latitude)+','+str(offer_location.longitud)
		
	for act in activities:
		destination = str(act.aclocation.latitude)+','+str(act.aclocation.longitud)
		r = requests.get(DISTANCE_BY_LATLNG.format(origin,destination,'driving'))
		print 'UGH',json.loads(r.content)
		if json.loads(r.content)['rows'][0]['elements'][0]['status'] == 'OK':
			try: 
				arrival_time = json.loads(r.content)['rows'][0]['elements'][0]['duration']['text']
			except Exception as e:
				print e
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
		startdate = datetime.datetime(int(startdate[0]), int(startdate[1]), int(startdate[2]), 23, 30, 1, tzinfo=timezone.utc),
		enddate = datetime.datetime(int(endday[0]), int(endday[1]), int(endday[2]), 23, 30, 1, tzinfo=timezone.utc))
	
	new_offer.save()
	return new_offer

def createOfferByHotelPrice(offers):
	price_hotel = {}
	for offer in offers:
		price_hotel[int(offer['rateInfo']['chargeableRateInfo']['priceToShowUsers'])] = offer['roomLongDescription']
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



