from helpers import *
import sys, django, requests, json, datetime

DAYS_LIMIT = 30
HOTEL_OFFER = "http://terminal2.expedia.com/x/mhotels/offers?hotelId={}&checkInDate={}&checkOutDate={}&room1=2&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
Tbloffer.objects.filter(startdate__lt=TODAY).delete()
print "today", datetime.datetime.now()

cities = {}
all_cities = Tblcity.objects.all()
for i in all_cities:
	cities[i.cityname] = i.countryid.countrycode

for city in cities:
		
		for hotel in hotelsByCity(city):
			print hotel.hotelname.encode('utf-8')
			hotel_offer_prices = {}
			hotel_offer_start = ''
			days_up_front = 2
			start_date = TODAY
			last_its_same = False 
			while days_up_front <= DAYS_LIMIT:
				print start_date
				end_day = datetime.datetime.now() + datetime.timedelta(days=days_up_front)
				end_day = end_day.strftime("%Y-%m-%d")
				r = requests.get(HOTEL_OFFER.format(hotel.hotelid,start_date,end_day))
				try:
					content = json.loads(r.content)
					hotel_prices = createOfferByHotelPrice(content['hotelRoomResponse'])

					if len(hotel_prices) != 0:
						if len(hotel_offer_prices) == 0:
							hotel_offer_prices = hotel_prices
							hotel_offer_start = start_date

						elif hotel_offer_prices != hotel_prices:

							print "Diferentes(?)",hotel_offer_prices,hotel_prices,hotel_offer_start,end_day
							print createOfferByHotel(hotel,hotel_offer_start,end_day,hotel_offer_prices)
							hotel_offer_start = end_day
							hotel_offer_prices = hotel_prices
							last_its_same = False
						else:
							last_its_same = True
					start_date = end_day
					days_up_front += 2
				except Exception as e:
					print e
					break
			if last_its_same:
				createOfferByHotel(hotel,hotel_offer_start,end_day,hotel_offer_prices)
			days_up_front = 2