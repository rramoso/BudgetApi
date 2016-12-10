from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tbluser(models.Model):
    userid = models.TextField(db_column='userID', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='firstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName', blank=True, null=True)  # Field name made lowercase.
    useremail = models.TextField(db_column='userEmail', blank=True, null=True)  # Field name made lowercase.
    userphonenumber = models.TextField(db_column='userPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    userbirthdate = models.DateField(db_column='userBirthdate', blank=True, null=True)  # Field name made lowercase.
    usergender = models.TextField(db_column='userGender', blank=True, null=True)  # Field name made lowercase.
    useraddress = models.IntegerField(db_column='userAddress', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'tblUser'
class Tblapi(models.Model):
    apiid = models.TextField(db_column='apiID')  # Field name made lowercase.
    apisource = models.TextField(db_column='apiSource', blank=True, null=True)  # Field name made lowercase.
    apilogo = models.TextField(db_column='apiLogo')  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblAPI'
        unique_together = (('apiid', 'apilogo'),)


class Tblactivity(models.Model):
    activityid = models.TextField(db_column='activityID')  # Field name made lowercase.
    actype = models.TextField(db_column='acType')  # Field name made lowercase.
    acname = models.TextField(db_column='acName')  # Field name made lowercase.
    acdescription = models.TextField(db_column='acDescription', blank=True, null=True)  # Field name made lowercase.
    accost = models.TextField(db_column='acCost', blank=True, null=True)  # Field name made lowercase.
    acbegintime = models.TextField(db_column='acBeginTime', blank=True, null=True)  # Field name made lowercase.
    acendtime = models.TextField(db_column='acEndTime', blank=True, null=True)  # Field name made lowercase.
    acstatus = models.TextField(db_column='acStatus', blank=True, null=True)  # Field name made lowercase.
    acdate = models.DateField(db_column='acDate', blank=True, null=True)  # Field name made lowercase.
    acrating = models.TextField(db_column='acRating',null=True)  # Field name made lowercase.
    aclocation = models.ForeignKey('Tbllocation', models.DO_NOTHING, db_column='aclocation', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 'tblActivity'


class Tblcity(models.Model):
    cityid = models.TextField(db_column='cityID', primary_key=True)  # Field name made lowercase.
    cityname = models.TextField(db_column='cityName', blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey('Tblcountry', models.DO_NOTHING, db_column='countryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblCity'


class Tblcountry(models.Model):
    countryid = models.TextField(db_column='countryID', primary_key=True)  # Field name made lowercase.
    countryname = models.TextField(db_column='countryName', blank=True, null=True)  # Field name made lowercase.
    continent = models.TextField(blank=True, null=True)
    countrycode = models.TextField(db_column='countryCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblCountry'


class Tblcreditcard(models.Model):
    creditcardnumber = models.TextField(db_column='creditCardNumber', primary_key=True)  # Field name made lowercase.
    creditcardcvv = models.TextField(db_column='creditCardCVV', blank=True, null=True)  # Field name made lowercase.
    creditcardexpyear = models.TextField(db_column='creditCardExpYear', blank=True, null=True)  # Field name made lowercase.
    creditcardexpdate = models.DateField(db_column='creditCardExpDate', blank=True, null=True)  # Field name made lowercase.
    creditcardtype = models.TextField(db_column='creditCardType', blank=True, null=True)  # Field name made lowercase.
    creditcardowner = models.ForeignKey('Tbluser', models.DO_NOTHING, db_column='creditCardOwner', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblCreditCard'


class Tblcuisine(models.Model):
    cuisineid = models.CharField(db_column='cuisineID', primary_key=True, max_length=1)  # Field name made lowercase.
    cuisine = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        
        db_table = 'tblCuisine'


class Tbldebitcard(models.Model):
    debitcardnumber = models.TextField(db_column='debitCardNumber', primary_key=True)  # Field name made lowercase.
    debitcardexpyear = models.TextField(db_column='debitCardExpYear', blank=True, null=True)  # Field name made lowercase.
    debitcardexpdate = models.DateField(db_column='debitCardExpDate', blank=True, null=True)  # Field name made lowercase.
    debitcardtype = models.TextField(db_column='debitCardType', blank=True, null=True)  # Field name made lowercase.
    debitcardowner = models.ForeignKey('Tbluser', models.DO_NOTHING, db_column='debitCardOwner', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblDebitCard'


class Tblhotel(models.Model):
    hotelid = models.TextField(db_column='hotelID', primary_key=True)  # Field name made lowercase.
    hotelname = models.TextField(db_column='hotelName')  # Field name made lowercase.
    hotelphonenumber = models.TextField(db_column='hotelPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    hotelwebsite = models.TextField(db_column='hotelWebsite', blank=True, null=True)  # Field name made lowercase.
    hotelrating = models.IntegerField(db_column='hotelRating')  # Field name made lowercase.
    hoteladdress = models.ForeignKey('Tbllocation', models.DO_NOTHING, db_column='hotelAddress', blank=True, null=True)  # Field name made lowercase.
    hotelcountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='hotelCountry')  # Field name made lowercase.
    hotelcity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='hotelCity')  # Field name made lowercase.
    
    class Meta:
        db_table = 'tblHotel'


class Tbllocation(models.Model):
    locationid = models.TextField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    streetname = models.TextField(db_column='streetName', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(blank=True, null=True)
    zipcode = models.TextField(db_column='zipCode', blank=True, null=True)  # Field name made lowercase.
    lcountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='lCountry', blank=True, null=True)  # Field name made lowercase.
    lcity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='lCity', blank=True, null=True)  # Field name made lowercase.
    longitud = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'tblLocation'


class Tbloffer(models.Model):
    offerid = models.CharField(db_column='offerID', primary_key=True, max_length=1)  # Field name made lowercase.
    budget = models.IntegerField(blank=True, null=True)
    sourcelocation = models.ForeignKey(Tbllocation, models.DO_NOTHING, db_column='sourceLocation', blank=True, null=True, related_name='offer_sourcelocation')  # Field name made lowercase.
    destinylocation = models.ForeignKey(Tbllocation, models.DO_NOTHING, db_column='destinyLocation', blank=True, null=True, related_name='offer_destinylocation')  # Field name made lowercase.
    transportationid = models.ForeignKey('Tbltransportation', models.DO_NOTHING, db_column='transportationID', blank=True, null=True)  # Field name made lowercase.
    sourcecountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='sourceCountry', blank=True, null=True, related_name='offer_sourcecountry')  # Field name made lowercase.
    destinationcountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='destinationCountry', blank=True, null=True, related_name='offer_destinationcountry')  # Field name made lowercase.
    transportationtype = models.CharField(db_column='transportationType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    transportationrating = models.CharField(db_column='transportationRating', max_length=1, blank=True, null=True)  # Field name made lowercase.
    restaurantid = models.ForeignKey('Tblrestaurant', models.DO_NOTHING, db_column='restaurantID', blank=True, null=True)  # Field name made lowercase.
    restaurantname = models.CharField(db_column='restaurantName', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rtcountry = models.CharField(db_column='rtCountry', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rtcity = models.CharField(db_column='rtCity', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rtcuisine = models.CharField(db_column='rtCuisine', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rtexpense = models.CharField(db_column='rtExpense', max_length=1, blank=True, null=True)  # Field name made lowercase.
    apiid = models.ForeignKey(Tblapi, models.DO_NOTHING, db_column='apiID', blank=True, null=True)  # Field name made lowercase.
    apilogo = models.CharField(db_column='apiLogo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hotelid = models.CharField(db_column='hotelID', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hotelname = models.CharField(db_column='hotelName', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hotelrating = models.IntegerField(db_column='hotelRating', blank=True, null=True)  # Field name made lowercase.
    hotelcountry = models.CharField(db_column='hotelCountry', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hotelcity = models.CharField(db_column='hotelCity', max_length=1, blank=True, null=True)  # Field name made lowercase.
    activityid = models.ForeignKey(Tblactivity, models.DO_NOTHING, db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    accountry = models.CharField(db_column='acCountry', max_length=1, blank=True, null=True)  # Field name made lowercase.
    accity = models.CharField(db_column='acCity', max_length=1, blank=True, null=True)  # Field name made lowercase.
    acname = models.CharField(db_column='acName', max_length=1, blank=True, null=True)  # Field name made lowercase.
    actype = models.CharField(db_column='acType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    acrating = models.CharField(db_column='acRating', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sourcecity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='sourceCity', blank=True, null=True, related_name='offer_sourcecity')  # Field name made lowercase.
    destinationcity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='destinationCity', blank=True, null=True, related_name='offer_destinationcountry')  # Field name made lowercase.
    rtrating = models.CharField(db_column='rtRating', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hotelexpense = models.CharField(db_column='hotelExpense', max_length=1, blank=True, null=True)  # Field name made lowercase.
    transportationcost = models.IntegerField(db_column='transportationCost', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    maxexpense = models.TextField(db_column='maxExpense', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    minexpense = models.TextField(db_column='minExpense', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'tblOffer'


class Tblorder(models.Model):
    orderid = models.TextField(db_column='orderID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Tbluser', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    ordercost = models.IntegerField(db_column='orderCost', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.
    reservationid = models.ForeignKey('Tblreservation', models.DO_NOTHING, db_column='reservationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblOrder'


class Tblpayment(models.Model):
    paymentid = models.TextField(db_column='paymentID', primary_key=True)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='paymentDate', blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.TextField(db_column='paymentType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblPayment'


class Tblport(models.Model):
    portname = models.TextField(db_column='portName', primary_key=True)  # Field name made lowercase.
    portcode = models.TextField(db_column='portCode', blank=True, null=True)  # Field name made lowercase.
    portlocation = models.ForeignKey(Tbllocation, models.DO_NOTHING, db_column='portLocation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblPort'


class Tblpreference(models.Model):
    preferenceid = models.TextField(db_column='preferenceID', primary_key=True)  # Field name made lowercase.
    preferencetype = models.TextField(db_column='preferenceType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblPreference'


class Tblreservation(models.Model):
    reservationid = models.TextField(db_column='reservationID', primary_key=True)  # Field name made lowercase.
    reservationtype = models.TextField(db_column='reservationType', blank=True, null=True)  # Field name made lowercase.
    hotelname = models.TextField(db_column='hotelname', blank=True, null=True)
    hotelprice = models.TextField(db_column='hotelprice', blank=True, null=True)
    hotelroomdescription = models.TextField(db_column='hotelroomdescription', blank=True, null=True)
    hoteladdress = models.TextField(db_column='hoteladdress', blank=True, null=True)
    actprice = models.TextField(db_column='actprice', blank=True, null=True)
    actitinerary = models.TextField(db_column='actitinerary', blank=True, null=True)
    transportationinfo = models.TextField(db_column='transportationinfo', blank=True, null=True)
    origin = models.TextField(db_column='origin', blank=True, null=True)
    destination = models.TextField(db_column='destination', blank=True, null=True)
    user = models.TextField(db_column='user', blank=True, null=True)
    startdate = models.TextField(db_column='startdate', blank=True, null=True)
    enddate = models.TextField(db_column='enddate', blank=True, null=True)
    preference = models.TextField(db_column='preference', blank=True, null=True)
    rating = models.TextField(db_column='rating', blank=True, null=True)
    budget = models.TextField(db_column='budget', blank=True, null=True)
    adult = models.TextField(db_column='adult', blank=True, null=True)
    children = models.TextField(db_column='children', blank=True, null=True)

    class Meta:
        
        db_table = 'tblReservation'


class Tblrestaurant(models.Model):
    restaurantid = models.TextField(db_column='restaurantID')  # Field name made lowercase.
    restaurantname = models.TextField(db_column='restaurantName')  # Field name made lowercase.
    rtphonenumber = models.TextField(db_column='rtPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    rtaddress = models.ForeignKey(Tbllocation, models.DO_NOTHING, db_column='rtAddress', blank=True, null=True)  # Field name made lowercase.
    rtcity = models.ForeignKey(Tblcity, models.DO_NOTHING, db_column='rtCity')  # Field name made lowercase.
    rtcuisine = models.TextField(db_column='rtCuisine',null=True)  # Field name made lowercase.
    rtrating = models.TextField(db_column='rtRating',null=True)  # Field name made lowercase.
    rtcountry = models.ForeignKey(Tblcountry, models.DO_NOTHING, db_column='rtCountry')  # Field name made lowercase.
    cuisineid = models.ForeignKey(Tblcuisine, models.DO_NOTHING, db_column='cuisineID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tblRestaurant'


class Tbltransportation(models.Model):
    transportationid = models.TextField(db_column='transportationID')  # Field name made lowercase.
    transportationtype = models.TextField(db_column='transportationType')  # Field name made lowercase.
    departureport = models.TextField(db_column='departurePort')  # Field name made lowercase.
    destinationport = models.TextField(db_column='destinationPort')  # Field name made lowercase.
    terminal = models.TextField(blank=True, null=True)
    tripstatus = models.TextField(db_column='tripStatus', blank=True, null=True)  # Field name made lowercase.
    tripnumber = models.TextField(db_column='tripNumber', blank=True, null=True)  # Field name made lowercase.
    sitnumber = models.TextField(db_column='sitNumber', blank=True, null=True)  # Field name made lowercase.
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
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    transportationcompanyid = models.TextField(db_column='transportationCompanyID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tbltransportationCompany'
