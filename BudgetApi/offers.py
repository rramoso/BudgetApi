from helpers import *

GOOGLE_MAP_DISTANCE = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode={}&language={}&key=AIzaSyCKGFSlE0eiWyjd9UZaNxTEdIUHBRV8GEU"


for j in Tbloffer.objects.all():
	addActivitiesToOffer(j)

def addActivitiesToOffer(offer):


# gets offers hotel location
	offer_hotel = Tblhotel.objects.get(hotelid = offer.hotelid)
	activities =  Tblactivity.objects.filter(aclocation = offer_hotel.hoteladdress)

	for i in activities:
		print i.title