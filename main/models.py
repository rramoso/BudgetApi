from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tbluser(models.Model):
    userid = models.CharField(max_length=1,db_column='userID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(max_length=1,db_column='firstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(max_length=1,db_column='lastName', blank=True, null=True)  # Field name made lowercase.
    useremail = models.CharField(max_length=1,db_column='userEmail', blank=True, null=True)  # Field name made lowercase.
    userphonenumber = models.CharField(max_length=1,db_column='userPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    userbirthdate = models.DateField(db_column='userBirthdate', blank=True, null=True)  # Field name made lowercase.
    usergender = models.CharField(max_length=1,db_column='userGender', blank=True, null=True)  # Field name made lowercase.
    useraddress = models.IntegerField(db_column='userAddress', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=1,blank=True, null=True)

    class Meta:
        
        db_table = 'tblUser'
class Tblapi(models.Model):
    apiid = models.CharField(max_length=1,db_column='apiID')  # Field name made lowercase.
    apisource = models.CharField(max_length=1,db_column='apiSource', blank=True, null=True)  # Field name made lowercase.
    apilogo = models.CharField(max_length=1,db_column='apiLogo')  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblAPI'
        unique_together = (('apiid', 'apilogo'),)


class Tblactivity(models.Model):
    activityid = models.CharField(max_length=1,db_column='activityID', primary_key=True)  # Field name made lowercase.
    actype = models.CharField(max_length=1,db_column='acType')  # Field name made lowercase.
    acname = models.CharField(max_length=1,db_column='acName')  # Field name made lowercase.
    acdescription = models.CharField(max_length=1,db_column='acDescription', blank=True, null=True)  # Field name made lowercase.
    accost = models.CharField(max_length=1,db_column='acCost', blank=True, null=True)  # Field name made lowercase.
    acbegintime = models.CharField(max_length=1,db_column='acBeginTime', blank=True, null=True)  # Field name made lowercase.
    acendtime = models.CharField(max_length=1,db_column='acEndTime', blank=True, null=True)  # Field name made lowercase.
    acstatus = models.CharField(max_length=1,db_column='acStatus', blank=True, null=True)  # Field name made lowercase.
    acdate = models.DateField(db_column='acDate', blank=True, null=True)  # Field name made lowercase.
    acrating = models.CharField(max_length=1,db_column='acRating',null=True)  # Field name made lowercase.
    aclocation = models.ForeignKey('Tbllocation', models.DO_NOTHING, db_column='activityAddress', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 'tblActivity'


class Tblcity(models.Model):
    cityid = models.CharField(max_length=1,db_column='cityID', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(max_length=1,db_column='cityName', blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey('Tblcountry', models.DO_NOTHING, db_column='countryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblCity'


class Tblcountry(models.Model):
    countryid = models.CharField(max_length=1,db_column='countryID', primary_key=True)  # Field name made lowercase.
    countryname = models.CharField(max_length=1,db_column='countryName', blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(max_length=1,blank=True, null=True)
    countrycode = models.CharField(max_length=1,db_column='countryCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblCountry'


class Tblcreditcard(models.Model):
    creditcardnumber = models.CharField(max_length=1,db_column='creditCardNumber', primary_key=True)  # Field name made lowercase.
    creditcardcvv = models.CharField(max_length=1,db_column='creditCardCVV', blank=True, null=True)  # Field name made lowercase.
    creditcardexpyear = models.CharField(max_length=1,db_column='creditCardExpYear', blank=True, null=True)  # Field name made lowercase.
    creditcardexpdate = models.DateField(db_column='creditCardExpDate', blank=True, null=True)  # Field name made lowercase.
    creditcardtype = models.CharField(max_length=1,db_column='creditCardType', blank=True, null=True)  # Field name made lowercase.
    creditcardowner = models.ForeignKey('Tbluser', models.DO_NOTHING, db_column='creditCardOwner', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblCreditCard'


class Tblcuisine(models.Model):
    cuisineid = models.CharField(max_length=1,db_column='cuisineID', primary_key=True)  # Field name made lowercase.
    cuisine = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        
        db_table = 'tblCuisine'


class Tbldebitcard(models.Model):
    debitcardnumber = models.CharField(max_length=1,db_column='debitCardNumber', primary_key=True)  # Field name made lowercase.
    debitcardexpyear = models.CharField(max_length=1,db_column='debitCardExpYear', blank=True, null=True)  # Field name made lowercase.
    debitcardexpdate = models.DateField(db_column='debitCardExpDate', blank=True, null=True)  # Field name made lowercase.
    debitcardtype = models.CharField(max_length=1,db_column='debitCardType', blank=True, null=True)  # Field name made lowercase.
    debitcardowner = models.ForeignKey('Tbluser', models.DO_NOTHING, db_column='debitCardOwner', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblDebitCard'


class Tblhotel(models.Model):
    hotelid = models.CharField(max_length=1,db_column='hotelID', primary_key=True)  # Field name made lowercase.
    hotelname = models.CharField(max_length=1,db_column='hotelName')  # Field name made lowercase.
    hotelphonenumber = models.CharField(max_length=1,db_column='hotelPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    hotelwebsite = models.CharField(max_length=1,db_column='hotelWebsite', blank=True, null=True)  # Field name made lowercase.
    hotelrating = models.IntegerField(db_column='hotelRating')  # Field name made lowercase.
    hoteladdress = models.ForeignKey('Tbllocation', models.DO_NOTHING, db_column='hotelAddress', blank=True, null=True)  # Field name made lowercase.
    hotelcountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='hotelCountry')  # Field name made lowercase.
    hotelcity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='hotelCity')  # Field name made lowercase.
    
    class Meta:
        db_table = 'tblHotel'


class Tbllocation(models.Model):
    locationid = models.CharField(max_length=1,db_column='locationID', primary_key=True)  # Field name made lowercase.
    streetname = models.CharField(max_length=1,db_column='streetName', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=1,blank=True, null=True)
    zipcode = models.CharField(max_length=1,db_column='zipCode', blank=True, null=True)  # Field name made lowercase.
    lcountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='lCountry', blank=True, null=True)  # Field name made lowercase.
    lcity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='lCity', blank=True, null=True)  # Field name made lowercase.
    longitud = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'tblLocation'


class Tbloffer(models.Model):
    offerid = models.CharField(max_length=1,db_column='offerID', primary_key=True)  # Field name made lowercase.
    budget = models.IntegerField(blank=True, null=True)
    sourcelocation = models.ForeignKey(Tbllocation, models.DO_NOTHING, db_column='sourceLocation', blank=True, null=True, related_name='offer_sourcelocation')  # Field name made lowercase.
    destinylocation = models.ForeignKey(Tbllocation, models.DO_NOTHING, db_column='destinyLocation', blank=True, null=True, related_name='offer_destinylocation')  # Field name made lowercase.
    transportationid = models.ForeignKey('Tbltransportation', models.DO_NOTHING, db_column='transportationID', blank=True, null=True)  # Field name made lowercase.
    sourcecountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='sourceCountry', blank=True, null=True, related_name='offer_sourcecountry')  # Field name made lowercase.
    destinationcountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='destinationCountry', blank=True, null=True, related_name='offer_destinationcountry')  # Field name made lowercase.
    transportationtype = models.CharField(max_length=1,db_column='transportationType', blank=True, null=True)  # Field name made lowercase.
    transportationrating = models.CharField(max_length=1,db_column='transportationRating', blank=True, null=True)  # Field name made lowercase.
    restaurantid = models.ForeignKey('Tblrestaurant', models.DO_NOTHING, db_column='restaurantID', blank=True, null=True)  # Field name made lowercase.
    restaurantname = models.CharField(max_length=1,db_column='restaurantName', blank=True, null=True)  # Field name made lowercase.
    rtcountry = models.CharField(max_length=1,db_column='rtCountry', blank=True, null=True)  # Field name made lowercase.
    rtcity = models.CharField(max_length=1,db_column='rtCity', blank=True, null=True)  # Field name made lowercase.
    rtcuisine = models.CharField(max_length=1,db_column='rtCuisine', blank=True, null=True)  # Field name made lowercase.
    rtexpense = models.CharField(max_length=1,db_column='rtExpense', blank=True, null=True)  # Field name made lowercase.
    apiid = models.ForeignKey(Tblapi, models.DO_NOTHING, db_column='apiID', blank=True, null=True)  # Field name made lowercase.
    apilogo = models.CharField(max_length=1,db_column='apiLogo', blank=True, null=True)  # Field name made lowercase.
    hotelid = models.CharField(max_length=1,db_column='hotelID', blank=True, null=True)  # Field name made lowercase.
    hotelname = models.CharField(max_length=1,db_column='hotelName', blank=True, null=True)  # Field name made lowercase.
    hotelrating = models.IntegerField(db_column='hotelRating', blank=True, null=True)  # Field name made lowercase.
    hotelcountry = models.CharField(max_length=1,db_column='hotelCountry', blank=True, null=True)  # Field name made lowercase.
    hotelcity = models.CharField(max_length=1,db_column='hotelCity', blank=True, null=True)  # Field name made lowercase.
    activityid = models.ForeignKey(Tblactivity, models.DO_NOTHING, db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    accountry = models.CharField(max_length=1,db_column='acCountry', blank=True, null=True)  # Field name made lowercase.
    accity = models.CharField(max_length=1,db_column='acCity', blank=True, null=True)  # Field name made lowercase.
    acname = models.CharField(max_length=1,db_column='acName', blank=True, null=True)  # Field name made lowercase.
    actype = models.CharField(max_length=1,db_column='acType', blank=True, null=True)  # Field name made lowercase.
    acrating = models.CharField(max_length=1,db_column='acRating', blank=True, null=True)  # Field name made lowercase.
    sourcecity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='sourceCity', blank=True, null=True, related_name='offer_sourcecity')  # Field name made lowercase.
    destinationcity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='destinationCity', blank=True, null=True, related_name='offer_destinationcountry')  # Field name made lowercase.
    rtrating = models.CharField(max_length=1,db_column='rtRating', blank=True, null=True)  # Field name made lowercase.
    hotelexpense = models.CharField(max_length=1,db_column='hotelExpense', blank=True, null=True)  # Field name made lowercase.
    transportationcost = models.IntegerField(db_column='transportationCost', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    maxexpense = models.CharField(max_length=1,db_column='maxExpense', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    minexpense = models.CharField(max_length=1,db_column='minExpense', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'tblOffer'


class Tblorder(models.Model):
    orderid = models.CharField(max_length=1,db_column='orderID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Tbluser', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    ordercost = models.IntegerField(db_column='orderCost', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.
    reservationid = models.ForeignKey('Tblreservation', models.DO_NOTHING, db_column='reservationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblOrder'


class Tblpayment(models.Model):
    paymentid = models.CharField(max_length=1,db_column='paymentID', primary_key=True)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='paymentDate', blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.CharField(max_length=1,db_column='paymentType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblPayment'


class Tblport(models.Model):
    portname = models.CharField(max_length=1,db_column='portName', primary_key=True)  # Field name made lowercase.
    portcode = models.CharField(max_length=1,db_column='portCode', blank=True, null=True)  # Field name made lowercase.
    portlocation = models.ForeignKey(Tbllocation, models.DO_NOTHING, db_column='portLocation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblPort'


class Tblpreference(models.Model):
    preferenceid = models.CharField(max_length=1,db_column='preferenceID', primary_key=True)  # Field name made lowercase.
    preferencetype = models.CharField(max_length=1,db_column='preferenceType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblPreference'


class Tblreservation(models.Model):
    reservationid = models.CharField(max_length=1,db_column='reservationID', primary_key=True)  # Field name made lowercase.
    reservationtype = models.CharField(max_length=1,db_column='reservationType', blank=True, null=True)  # Field name made lowercase.
    hotelname = models.CharField(max_length=1,db_column='hotelname', blank=True, null=True)
    hotelprice = models.CharField(max_length=1,db_column='hotelprice', blank=True, null=True)
    hotelroomdescription = models.CharField(max_length=1,db_column='hotelroomdescription', blank=True, null=True)
    hoteladdress = models.CharField(max_length=1,db_column='hoteladdress', blank=True, null=True)
    actprice = models.CharField(max_length=1,db_column='actprice', blank=True, null=True)
    actitinerary = models.CharField(max_length=1,db_column='actitinerary', blank=True, null=True)
    transportationinfo = models.CharField(max_length=1,db_column='transportationinfo', blank=True, null=True)
    origin = models.CharField(max_length=1,db_column='origin', blank=True, null=True)
    destination = models.CharField(max_length=1,db_column='destination', blank=True, null=True)
    user = models.CharField(max_length=1,db_column='user', blank=True, null=True)
    startdate = models.CharField(max_length=1,db_column='startdate', blank=True, null=True)
    enddate = models.CharField(max_length=1,db_column='enddate', blank=True, null=True)
    preference = models.CharField(max_length=1,db_column='preference', blank=True, null=True)
    rating = models.CharField(max_length=1,db_column='rating', blank=True, null=True)
    budget = models.CharField(max_length=1,db_column='budget', blank=True, null=True)
    adult = models.CharField(max_length=1,db_column='adult', blank=True, null=True)
    children = models.CharField(max_length=1,db_column='children', blank=True, null=True)

    class Meta:
        
        db_table = 'tblReservation'


class Tblrestaurant(models.Model):
    restaurantid = models.CharField(max_length=1,db_column='restaurantID')  # Field name made lowercase.
    restaurantname = models.CharField(max_length=1,db_column='restaurantName')  # Field name made lowercase.
    rtphonenumber = models.CharField(max_length=1,db_column='rtPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    rtaddress = models.ForeignKey(Tbllocation, models.DO_NOTHING, db_column='rtAddress', blank=True, null=True)  # Field name made lowercase.
    rtcity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='rtCity')  # Field name made lowercase.
    rtcuisine = models.CharField(max_length=1,db_column='rtCuisine',null=True)  # Field name made lowercase.
    rtrating = models.CharField(max_length=1,db_column='rtRating',null=True)  # Field name made lowercase.
    rtcountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='rtCountry')  # Field name made lowercase.
    cuisineid = models.ForeignKey(Tblcuisine, models.DO_NOTHING, db_column='cuisineID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblRestaurant'


class Tbltransportation(models.Model):
    transportationid = models.CharField(max_length=1,db_column='transportationID')  # Field name made lowercase.
    transportationtype = models.CharField(max_length=1,db_column='transportationType')  # Field name made lowercase.
    departureport = models.CharField(max_length=1,db_column='departurePort')  # Field name made lowercase.
    destinationport = models.CharField(max_length=1,db_column='destinationPort')  # Field name made lowercase.
    terminal = models.CharField(max_length=1,blank=True, null=True)
    tripstatus = models.CharField(max_length=1,db_column='tripStatus', blank=True, null=True)  # Field name made lowercase.
    tripnumber = models.CharField(max_length=1,db_column='tripNumber', blank=True, null=True)  # Field name made lowercase.
    sitnumber = models.CharField(max_length=1,db_column='sitNumber', blank=True, null=True)  # Field name made lowercase.
    departuretime = models.DateTimeField(db_column='departureTime', blank=True, null=True)  # Field name made lowercase.
    arrivedtime = models.DateTimeField(db_column='arrivedTime', blank=True, null=True)  # Field name made lowercase.
    companyid = models.ForeignKey('Tbltransportationcompany', models.DO_NOTHING, db_column='companyID', blank=True, null=True)  # Field name made lowercase.
    portid = models.ForeignKey(Tblport, models.DO_NOTHING, db_column='portID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblTransportation'





# class TblofferPreference(models.Model):
#     offerid = models.ForeignKey(Tbloffer, models.DO_NOTHING, db_column='offerID')  # Field name made lowercase.
#     preferenceid = models.ForeignKey(Tblpreference, models.DO_NOTHING, db_column='preferenceID')  # Field name made lowercase.

#     class Meta:
        
#         db_table = 'tbloffer_preference'
#         unique_together = (('offerid', 'preferenceid'),)


class Tbltransportationcompany(models.Model):
    name = models.CharField(max_length=1,db_column='Name')  # Field name made lowercase.
    transportationcompanyid = models.CharField(max_length=1,db_column='transportationCompanyID', primary_key=True)  # Field name made lowercase.
    transportationCompanyType = models.CharField(max_length=1,db_column='transportationCompanyType')
    class Meta:
        
        db_table = 'tbltransportationCompany'
