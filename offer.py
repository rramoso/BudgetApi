from helpers import *

GOOGLE_MAP_DISTANCE = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode={}&language={}&key=AIzaSyCKGFSlE0eiWyjd9UZaNxTEdIUHBRV8GEU"


def addActivitiesToOffer(offer):


# gets offers hotel location
	offer_hotel = Tblhotel.objects.get(hotelid = offer.hotelid)
	print offer_hotel.hoteladdress.lcity.cityname
	activities =  Tblactivity.objects.filter(aclocation__lcity__cityname = offer_hotel.hoteladdress.lcity.cityname)
	print activities
	for i in activities:
		print i.title



for j in Tbloffer.objects.all():
	addActivitiesToOffer(j)

