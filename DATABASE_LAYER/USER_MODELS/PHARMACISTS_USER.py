from django.db import models
import pandas as pd
from django.utils.timezone import now,timedelta

class PHARMACIST_USERS_MODEL(models.Model):
    PHARMACISTUSERS_INDEX_KEY = models.AutoField(primary_key=True)
    PHARMACISTUSERS_USERNAME = models.CharField(max_length=400, null=True, blank=True)
    PHARMACISTUSERS_EMAIL = models.CharField(max_length=400, null=True, blank=True)
    PHARMACISTUSERS_PHONE_NUMBER = models.CharField(max_length=400, null=True, blank=True)
    PHARMACISTUSERS_FULLNAME = models.CharField(max_length=400, null=True, blank=True)
    PHARMACISTUSERS_SHOP_ADDRESS = models.CharField(max_length=400, null=True, blank=True)
    PHARMACISTUSERS_SHOP_LATITUDE = models.CharField(max_length=400, null=True, blank=True)
    PHARMACISTUSERS_SHOP_LONGITUDE = models.CharField(max_length=400, null=True, blank=True)
    PHARMACISTUSERS_SHOP_CONTACT_INFO = models.CharField(max_length=400, null=True, blank=True)
    PHARMACISTUSERS_PASSWORD = models.CharField(max_length=400, null=True, blank=True)
    PHARMACISTUSERS_Create_Date = models.DateTimeField(default=now, editable=False)
    PHARMACISTUSERS_Update_Date = models.DateTimeField(default=(now() + timedelta(hours=24)), editable=False)
    PHARMACISTUSERS_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'PHARMACIST_USERS_MODEL'

    def CREATE_USER(self,USERNAME,EMAIL,PHONE_NUMBER,FULLNAME,BILLING_ADDRESS,LAT,LONG,CONTACT_INFO,PASSWORD):
        try:
            USERNAME_CHECK = PHARMACIST_USERS_MODEL.objects.filter(PHARMACISTUSERS_USERNAME=USERNAME)
            if(len(USERNAME_CHECK) > 0):
                return 0

            EMAIL_CHECK = PHARMACIST_USERS_MODEL.objects.filter(PHARMACISTUSERS_EMAIL=EMAIL)
            if (len(EMAIL_CHECK) > 0):
                return 1

            OBJECT_USER = PHARMACIST_USERS_MODEL(
                PHARMACISTUSERS_USERNAME = USERNAME,
                PHARMACISTUSERS_EMAIL = EMAIL,
                PHARMACISTUSERS_PHONE_NUMBER = PHONE_NUMBER,
                PHARMACISTUSERS_FULLNAME = FULLNAME,
                PHARMACISTUSERS_SHOP_ADDRESS = BILLING_ADDRESS,
                PHARMACISTUSERS_SHOP_LATITUDE = LAT,
                PHARMACISTUSERS_SHOP_LONGITUDE = LONG,
                PHARMACISTUSERS_SHOP_CONTACT_INFO = CONTACT_INFO,
                PHARMACISTUSERS_PASSWORD = PASSWORD
            )
            OBJECT_USER.save()
            return 2
        except:
            return 3

    def LOGIN_USER(self,USERNAME,PASSWORD):
        try:
            USERNAME_CHECK = PHARMACIST_USERS_MODEL.objects.filter(PHARMACISTUSERS_USERNAME=USERNAME).filter(PHARMACISTUSERS_PASSWORD=PASSWORD)
            if(len(USERNAME_CHECK) > 0):
                return USERNAME_CHECK[0]
            return 0
        except:
            return 3