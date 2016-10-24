# from tastypie.resources import ModelResource
# from tastypie.authorization import Authorization
# from tastypie.constants import ALL
# import time
# from tastypie import fields
# from hello.models import *


# class WhateverResource(ModelResource):
     
#     # acdescription = fields.CharField()
#     class Meta:
#     	queryset = Tblrestaurant.objects.all()
#         resource_name = 'whatever'
#         limit = 0
#         authorization= Authorization()
#         list_allowed_methods = ['post','get']


#     def hydrate(self,bundle):
#     	city = bundle.data['city']
#     	restaurant_name = bundle.data['restaurant_name']
#     	locationid = bundle.data['location']
#     	saved_city = Tblcity.objects.get(cityname = city)
#     	location = Tbllocation.objects.get(locationid=locationid)

#     	resta = Tblrestaurant.objects.create(
#     		restaurantname=restaurant_name,
#     		rtphonenumber="",
#     		rtaddress=location,
#     		rtcity=saved_city,
#     		rtcuisine="",
#     		rtrating="",
#     		rtcountry=saved_city.countryid,
#     		cuisineid=None)
#     	resta.save()
#     	return bundle
#     	# response = requests.post(url, data=data_json, headers=headers)
# #     	restaurantid
# # restaurantname
# # rtphonenumber
# # rtaddress
# # rtcity
# # rtcuisine
# # rtrating
# # rtcountry
# # cuisineid