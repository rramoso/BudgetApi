from tastypie.resources import ModelResource,Resource
from tastypie.authorization import Authorization
from tastypie.constants import ALL
import time
from tastypie import fields
from main.models import *
from helpers import *
import urllib3,ast,re

class OfferResource(ModelResource):
     

	class Meta:
		queryset = Tblcity.objects.filter(cityname = 'Santo Domingo')
		resource_name = 'offer'
		limit = 0
		authorization= Authorization()
		list_allowed_methods = ['get']


	def dehydrate(self,bundle):

		begintime = str(bundle.request.GET['begintime'])
		endtime = str(bundle.request.GET['endtime'])
		budget = int(bundle.request.GET['limit'])
		city = bundle.request.GET['city']
		preferences = re.split('[\[,\,,\',\]]',bundle.request.GET['preferences'])
		while '' in preferences: preferences.remove('')
		result = createOffersToUser(datetime.datetime.strptime(begintime,"%Y-%m-%d %H:%M:%S"), datetime.datetime.strptime(endtime,"%Y-%m-%d %H:%M:%S"),budget,Tblcity.objects.get(cityname = city),preferences,{"Adult":1})

		return result

class ReserveResource(ModelResource):

	class Meta:
		queryset = Tblreservation.objects.all()
		resource_name = 'detailoffer'
		authorization= Authorization()
		list_allowed_methods = ['post','get']

	def dehydrate(self,bundle):

		st = str(bundle.data["actitinerary"].encode('utf-8'))
		st = re.sub("</p>"," ",st)
		st = re.sub("<p>"," ",st)
		st = re.sub("\n"," ",st)

		print ast.literal_eval(st)
		bundle.data["actitinerary"] = ast.literal_eval(st)
		return bundle



