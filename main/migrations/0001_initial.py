# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tblactivity',
            fields=[
                ('activityid', models.CharField(db_column='activityID', max_length=1, primary_key=True, serialize=False)),
                ('actype', models.CharField(db_column='acType', max_length=1)),
                ('acname', models.CharField(db_column='acName', max_length=1)),
                ('acdescription', models.CharField(blank=True, db_column='acDescription', max_length=1, null=True)),
                ('accost', models.CharField(blank=True, db_column='acCost', max_length=1, null=True)),
                ('acbegintime', models.CharField(blank=True, db_column='acBeginTime', max_length=1, null=True)),
                ('acendtime', models.CharField(blank=True, db_column='acEndTime', max_length=1, null=True)),
                ('acstatus', models.CharField(blank=True, db_column='acStatus', max_length=1, null=True)),
                ('acdate', models.DateField(blank=True, db_column='acDate', null=True)),
                ('acrating', models.CharField(db_column='acRating', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblActivity',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tblapi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiid', models.CharField(db_column='apiID', max_length=1)),
                ('apisource', models.CharField(blank=True, db_column='apiSource', max_length=1, null=True)),
                ('apilogo', models.CharField(db_column='apiLogo', max_length=1)),
            ],
            options={
                'db_table': 'tblAPI',
            },
        ),
        migrations.CreateModel(
            name='Tblcity',
            fields=[
                ('cityid', models.CharField(db_column='cityID', max_length=1, primary_key=True, serialize=False)),
                ('cityname', models.CharField(blank=True, db_column='cityName', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblCity',
            },
        ),
        migrations.CreateModel(
            name='Tblcountry',
            fields=[
                ('countryid', models.CharField(db_column='countryID', max_length=1, primary_key=True, serialize=False)),
                ('countryname', models.CharField(blank=True, db_column='countryName', max_length=1, null=True)),
                ('continent', models.CharField(blank=True, max_length=1, null=True)),
                ('countrycode', models.CharField(blank=True, db_column='countryCode', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblCountry',
            },
        ),
        migrations.CreateModel(
            name='Tblcreditcard',
            fields=[
                ('creditcardnumber', models.CharField(db_column='creditCardNumber', max_length=1, primary_key=True, serialize=False)),
                ('creditcardcvv', models.CharField(blank=True, db_column='creditCardCVV', max_length=1, null=True)),
                ('creditcardexpyear', models.CharField(blank=True, db_column='creditCardExpYear', max_length=1, null=True)),
                ('creditcardexpdate', models.DateField(blank=True, db_column='creditCardExpDate', null=True)),
                ('creditcardtype', models.CharField(blank=True, db_column='creditCardType', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblCreditCard',
            },
        ),
        migrations.CreateModel(
            name='Tblcuisine',
            fields=[
                ('cuisineid', models.CharField(db_column='cuisineID', max_length=1, primary_key=True, serialize=False)),
                ('cuisine', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblCuisine',
            },
        ),
        migrations.CreateModel(
            name='Tbldebitcard',
            fields=[
                ('debitcardnumber', models.CharField(db_column='debitCardNumber', max_length=1, primary_key=True, serialize=False)),
                ('debitcardexpyear', models.CharField(blank=True, db_column='debitCardExpYear', max_length=1, null=True)),
                ('debitcardexpdate', models.DateField(blank=True, db_column='debitCardExpDate', null=True)),
                ('debitcardtype', models.CharField(blank=True, db_column='debitCardType', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblDebitCard',
            },
        ),
        migrations.CreateModel(
            name='Tblhotel',
            fields=[
                ('hotelid', models.CharField(db_column='hotelID', max_length=1, primary_key=True, serialize=False)),
                ('hotelname', models.CharField(db_column='hotelName', max_length=1)),
                ('hotelphonenumber', models.CharField(blank=True, db_column='hotelPhoneNumber', max_length=1, null=True)),
                ('hotelwebsite', models.CharField(blank=True, db_column='hotelWebsite', max_length=1, null=True)),
                ('hotelrating', models.IntegerField(db_column='hotelRating')),
            ],
            options={
                'db_table': 'tblHotel',
            },
        ),
        migrations.CreateModel(
            name='Tbllocation',
            fields=[
                ('locationid', models.CharField(db_column='locationID', max_length=1, primary_key=True, serialize=False)),
                ('streetname', models.CharField(blank=True, db_column='streetName', max_length=1, null=True)),
                ('state', models.CharField(blank=True, max_length=1, null=True)),
                ('zipcode', models.CharField(blank=True, db_column='zipCode', max_length=1, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('lcity', models.ForeignKey(blank=True, db_column='lCity', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblcity')),
                ('lcountry', models.ForeignKey(blank=True, db_column='lCountry', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblcountry')),
            ],
            options={
                'db_table': 'tblLocation',
            },
        ),
        migrations.CreateModel(
            name='Tbloffer',
            fields=[
                ('offerid', models.CharField(db_column='offerID', max_length=1, primary_key=True, serialize=False)),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('transportationtype', models.CharField(blank=True, db_column='transportationType', max_length=1, null=True)),
                ('transportationrating', models.CharField(blank=True, db_column='transportationRating', max_length=1, null=True)),
                ('restaurantname', models.CharField(blank=True, db_column='restaurantName', max_length=1, null=True)),
                ('rtcountry', models.CharField(blank=True, db_column='rtCountry', max_length=1, null=True)),
                ('rtcity', models.CharField(blank=True, db_column='rtCity', max_length=1, null=True)),
                ('rtcuisine', models.CharField(blank=True, db_column='rtCuisine', max_length=1, null=True)),
                ('rtexpense', models.CharField(blank=True, db_column='rtExpense', max_length=1, null=True)),
                ('apilogo', models.CharField(blank=True, db_column='apiLogo', max_length=1, null=True)),
                ('hotelid', models.CharField(blank=True, db_column='hotelID', max_length=1, null=True)),
                ('hotelname', models.CharField(blank=True, db_column='hotelName', max_length=1, null=True)),
                ('hotelrating', models.IntegerField(blank=True, db_column='hotelRating', null=True)),
                ('hotelcountry', models.CharField(blank=True, db_column='hotelCountry', max_length=1, null=True)),
                ('hotelcity', models.CharField(blank=True, db_column='hotelCity', max_length=1, null=True)),
                ('accountry', models.CharField(blank=True, db_column='acCountry', max_length=1, null=True)),
                ('accity', models.CharField(blank=True, db_column='acCity', max_length=1, null=True)),
                ('acname', models.CharField(blank=True, db_column='acName', max_length=1, null=True)),
                ('actype', models.CharField(blank=True, db_column='acType', max_length=1, null=True)),
                ('acrating', models.CharField(blank=True, db_column='acRating', max_length=1, null=True)),
                ('rtrating', models.CharField(blank=True, db_column='rtRating', max_length=1, null=True)),
                ('hotelexpense', models.CharField(blank=True, db_column='hotelExpense', max_length=1, null=True)),
                ('transportationcost', models.IntegerField(blank=True, db_column='transportationCost', null=True)),
                ('startdate', models.DateTimeField(blank=True, db_column='startDate', null=True)),
                ('enddate', models.DateTimeField(blank=True, db_column='endDate', null=True)),
                ('maxexpense', models.CharField(blank=True, db_column='maxExpense', max_length=1, null=True)),
                ('minexpense', models.CharField(blank=True, db_column='minExpense', max_length=1, null=True)),
                ('activityid', models.ForeignKey(blank=True, db_column='activityID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblactivity')),
                ('apiid', models.ForeignKey(blank=True, db_column='apiID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblapi')),
                ('destinationcity', models.ForeignKey(blank=True, db_column='destinationCity', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_destinationcountry', to='main.Tblcity')),
                ('destinationcountry', models.ForeignKey(blank=True, db_column='destinationCountry', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_destinationcountry', to='main.Tblcountry')),
                ('destinylocation', models.ForeignKey(blank=True, db_column='destinyLocation', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_destinylocation', to='main.Tbllocation')),
            ],
            options={
                'db_table': 'tblOffer',
            },
        ),
        migrations.CreateModel(
            name='Tblorder',
            fields=[
                ('orderid', models.CharField(db_column='orderID', max_length=1, primary_key=True, serialize=False)),
                ('ordercost', models.IntegerField(blank=True, db_column='orderCost', null=True)),
                ('orderdate', models.DateField(blank=True, db_column='orderDate', null=True)),
            ],
            options={
                'db_table': 'tblOrder',
            },
        ),
        migrations.CreateModel(
            name='Tblpayment',
            fields=[
                ('paymentid', models.CharField(db_column='paymentID', max_length=1, primary_key=True, serialize=False)),
                ('paymentdate', models.DateField(blank=True, db_column='paymentDate', null=True)),
                ('paymenttype', models.CharField(blank=True, db_column='paymentType', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblPayment',
            },
        ),
        migrations.CreateModel(
            name='Tblport',
            fields=[
                ('portname', models.CharField(db_column='portName', max_length=1, primary_key=True, serialize=False)),
                ('portcode', models.CharField(blank=True, db_column='portCode', max_length=1, null=True)),
                ('portlocation', models.ForeignKey(blank=True, db_column='portLocation', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tbllocation')),
            ],
            options={
                'db_table': 'tblPort',
            },
        ),
        migrations.CreateModel(
            name='Tblpreference',
            fields=[
                ('preferenceid', models.CharField(db_column='preferenceID', max_length=1, primary_key=True, serialize=False)),
                ('preferencetype', models.CharField(blank=True, db_column='preferenceType', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblPreference',
            },
        ),
        migrations.CreateModel(
            name='Tblreservation',
            fields=[
                ('reservationid', models.CharField(db_column='reservationID', max_length=1, primary_key=True, serialize=False)),
                ('reservationtype', models.CharField(blank=True, db_column='reservationType', max_length=1, null=True)),
                ('hotelname', models.CharField(blank=True, db_column='hotelname', max_length=1, null=True)),
                ('hotelprice', models.CharField(blank=True, db_column='hotelprice', max_length=1, null=True)),
                ('hotelroomdescription', models.CharField(blank=True, db_column='hotelroomdescription', max_length=1, null=True)),
                ('hoteladdress', models.CharField(blank=True, db_column='hoteladdress', max_length=1, null=True)),
                ('actprice', models.CharField(blank=True, db_column='actprice', max_length=1, null=True)),
                ('actitinerary', models.CharField(blank=True, db_column='actitinerary', max_length=1, null=True)),
                ('transportationinfo', models.CharField(blank=True, db_column='transportationinfo', max_length=1, null=True)),
                ('origin', models.CharField(blank=True, db_column='origin', max_length=1, null=True)),
                ('destination', models.CharField(blank=True, db_column='destination', max_length=1, null=True)),
                ('user', models.CharField(blank=True, db_column='user', max_length=1, null=True)),
                ('startdate', models.CharField(blank=True, db_column='startdate', max_length=1, null=True)),
                ('enddate', models.CharField(blank=True, db_column='enddate', max_length=1, null=True)),
                ('preference', models.CharField(blank=True, db_column='preference', max_length=1, null=True)),
                ('rating', models.CharField(blank=True, db_column='rating', max_length=1, null=True)),
                ('budget', models.CharField(blank=True, db_column='budget', max_length=1, null=True)),
                ('adult', models.CharField(blank=True, db_column='adult', max_length=1, null=True)),
                ('children', models.CharField(blank=True, db_column='children', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblReservation',
            },
        ),
        migrations.CreateModel(
            name='Tblrestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurantid', models.CharField(db_column='restaurantID', max_length=1)),
                ('restaurantname', models.CharField(db_column='restaurantName', max_length=1)),
                ('rtphonenumber', models.CharField(blank=True, db_column='rtPhoneNumber', max_length=1, null=True)),
                ('rtcuisine', models.CharField(db_column='rtCuisine', max_length=1, null=True)),
                ('rtrating', models.CharField(db_column='rtRating', max_length=1, null=True)),
                ('cuisineid', models.ForeignKey(blank=True, db_column='cuisineID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblcuisine')),
                ('rtaddress', models.ForeignKey(blank=True, db_column='rtAddress', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tbllocation')),
                ('rtcity', models.ForeignKey(db_column='rtCity', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblcity')),
                ('rtcountry', models.ForeignKey(db_column='rtCountry', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblcountry')),
            ],
            options={
                'db_table': 'tblRestaurant',
            },
        ),
        migrations.CreateModel(
            name='Tbltransportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportationid', models.CharField(db_column='transportationID', max_length=1)),
                ('transportationtype', models.CharField(db_column='transportationType', max_length=1)),
                ('departureport', models.CharField(db_column='departurePort', max_length=1)),
                ('destinationport', models.CharField(db_column='destinationPort', max_length=1)),
                ('terminal', models.CharField(blank=True, max_length=1, null=True)),
                ('tripstatus', models.CharField(blank=True, db_column='tripStatus', max_length=1, null=True)),
                ('tripnumber', models.CharField(blank=True, db_column='tripNumber', max_length=1, null=True)),
                ('sitnumber', models.CharField(blank=True, db_column='sitNumber', max_length=1, null=True)),
                ('departuretime', models.DateTimeField(blank=True, db_column='departureTime', null=True)),
                ('arrivedtime', models.DateTimeField(blank=True, db_column='arrivedTime', null=True)),
            ],
            options={
                'db_table': 'tblTransportation',
            },
        ),
        migrations.CreateModel(
            name='Tbltransportationcompany',
            fields=[
                ('name', models.CharField(db_column='Name', max_length=1)),
                ('transportationcompanyid', models.CharField(db_column='transportationCompanyID', max_length=1, primary_key=True, serialize=False)),
                ('transportationCompanyType', models.CharField(db_column='transportationCompanyType', max_length=1)),
            ],
            options={
                'db_table': 'tbltransportationCompany',
            },
        ),
        migrations.CreateModel(
            name='Tbluser',
            fields=[
                ('userid', models.CharField(db_column='userID', max_length=1, primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=1, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=1, null=True)),
                ('useremail', models.CharField(blank=True, db_column='userEmail', max_length=1, null=True)),
                ('userphonenumber', models.CharField(blank=True, db_column='userPhoneNumber', max_length=1, null=True)),
                ('userbirthdate', models.DateField(blank=True, db_column='userBirthdate', null=True)),
                ('usergender', models.CharField(blank=True, db_column='userGender', max_length=1, null=True)),
                ('useraddress', models.IntegerField(blank=True, db_column='userAddress', null=True)),
                ('password', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'tblUser',
            },
        ),
        migrations.AddField(
            model_name='tbltransportation',
            name='companyid',
            field=models.ForeignKey(blank=True, db_column='companyID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tbltransportationcompany'),
        ),
        migrations.AddField(
            model_name='tbltransportation',
            name='portid',
            field=models.ForeignKey(blank=True, db_column='portID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblport'),
        ),
        migrations.AddField(
            model_name='tblorder',
            name='reservationid',
            field=models.ForeignKey(blank=True, db_column='reservationID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblreservation'),
        ),
        migrations.AddField(
            model_name='tblorder',
            name='userid',
            field=models.ForeignKey(blank=True, db_column='userID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tbluser'),
        ),
        migrations.AddField(
            model_name='tbloffer',
            name='restaurantid',
            field=models.ForeignKey(blank=True, db_column='restaurantID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblrestaurant'),
        ),
        migrations.AddField(
            model_name='tbloffer',
            name='sourcecity',
            field=models.ForeignKey(blank=True, db_column='sourceCity', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_sourcecity', to='main.Tblcity'),
        ),
        migrations.AddField(
            model_name='tbloffer',
            name='sourcecountry',
            field=models.ForeignKey(blank=True, db_column='sourceCountry', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_sourcecountry', to='main.Tblcountry'),
        ),
        migrations.AddField(
            model_name='tbloffer',
            name='sourcelocation',
            field=models.ForeignKey(blank=True, db_column='sourceLocation', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_sourcelocation', to='main.Tbllocation'),
        ),
        migrations.AddField(
            model_name='tbloffer',
            name='transportationid',
            field=models.ForeignKey(blank=True, db_column='transportationID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tbltransportation'),
        ),
        migrations.AddField(
            model_name='tblhotel',
            name='hoteladdress',
            field=models.ForeignKey(blank=True, db_column='hotelAddress', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tbllocation'),
        ),
        migrations.AddField(
            model_name='tblhotel',
            name='hotelcity',
            field=models.ForeignKey(db_column='hotelCity', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblcity'),
        ),
        migrations.AddField(
            model_name='tblhotel',
            name='hotelcountry',
            field=models.ForeignKey(db_column='hotelCountry', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblcountry'),
        ),
        migrations.AddField(
            model_name='tbldebitcard',
            name='debitcardowner',
            field=models.ForeignKey(blank=True, db_column='debitCardOwner', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tbluser'),
        ),
        migrations.AddField(
            model_name='tblcreditcard',
            name='creditcardowner',
            field=models.ForeignKey(blank=True, db_column='creditCardOwner', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tbluser'),
        ),
        migrations.AddField(
            model_name='tblcity',
            name='countryid',
            field=models.ForeignKey(blank=True, db_column='countryID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tblcountry'),
        ),
        migrations.AlterUniqueTogether(
            name='tblapi',
            unique_together=set([('apiid', 'apilogo')]),
        ),
        migrations.AddField(
            model_name='tblactivity',
            name='aclocation',
            field=models.ForeignKey(blank=True, db_column='activityAddress', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tbllocation'),
        ),
    ]
