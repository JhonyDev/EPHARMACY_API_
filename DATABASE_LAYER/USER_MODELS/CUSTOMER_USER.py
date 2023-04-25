from django.db import models
import pandas as pd
from django.utils.timezone import now,timedelta


class CUSTOMER_USER_MODEL(models.Model):
    CUSTOMERUSER_INDEX_KEY = models.AutoField(primary_key=True)
    CUSTOMERUSER_USERNAME = models.CharField(max_length=400, null=True, blank=True)
    CUSTOMERUSER_EMAIL = models.CharField(max_length=400, null=True, blank=True)
    CUSTOMERUSER_PHONE_NUMBER = models.CharField(max_length=400, null=True, blank=True)
    CUSTOMERUSER_FULLNAME = models.CharField(max_length=400, null=True, blank=True)
    CUSTOMERUSER_BILLING_ADDRESS = models.CharField(max_length=400, null=True, blank=True)
    CUSTOMERUSER_PASSWORD = models.CharField(max_length=400, null=True, blank=True)
    CUSTOMERUSER_Create_Date = models.DateTimeField(default=now, editable=False)
    CUSTOMERUSER_Update_Date = models.DateTimeField(default=(now() + timedelta(hours=24)), editable=False)
    CUSTOMERUSER_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'CUSTOMER_USER_MODEL'

    def CREATE_USER(self,USERNAME,EMAIL,PHONE_NUMBER,FULLNAME,BILLING_ADDRESS,PASSWORD):
        try:
            USERNAME_CHECK = CUSTOMER_USER_MODEL.objects.filter(CUSTOMERUSER_USERNAME=USERNAME)
            if(len(USERNAME_CHECK) > 0):
                return 0

            EMAIL_CHECK = CUSTOMER_USER_MODEL.objects.filter(CUSTOMERUSER_EMAIL=EMAIL)
            if (len(EMAIL_CHECK) > 0):
                return 1

            OBJECT_USER = CUSTOMER_USER_MODEL(
                CUSTOMERUSER_USERNAME = USERNAME,
                CUSTOMERUSER_EMAIL = EMAIL,
                CUSTOMERUSER_PHONE_NUMBER = PHONE_NUMBER,
                CUSTOMERUSER_FULLNAME = FULLNAME,
                CUSTOMERUSER_BILLING_ADDRESS = BILLING_ADDRESS,
                CUSTOMERUSER_PASSWORD = PASSWORD
            )
            OBJECT_USER.save()
            return 2
        except:
            return 3

    def LOGIN_USER(self,USERNAME,PASSWORD):
        try:
            USERNAME_CHECK = CUSTOMER_USER_MODEL.objects.filter(CUSTOMERUSER_USERNAME=USERNAME).filter(CUSTOMERUSER_PASSWORD=PASSWORD)
            if(len(USERNAME_CHECK) > 0):
                return USERNAME_CHECK[0]
            return 0
        except:
            return 3