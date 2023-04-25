from django.db import models
from django.utils.timezone import now, timedelta


class ADMIN_USER_MODEL(models.Model):
    ADMINUSER_INDEX_KEY = models.AutoField(primary_key=True)
    ADMINUSER_USERNAME = models.CharField(max_length=400, null=True, blank=True)
    ADMINUSER_EMAIL = models.CharField(max_length=400, null=True, blank=True)
    ADMINUSER_PHONE_NUMBER = models.CharField(max_length=400, null=True, blank=True)
    ADMINUSER_FULLNAME = models.CharField(max_length=400, null=True, blank=True)
    ADMINUSER_BILLING_ADDRESS = models.CharField(max_length=400, null=True, blank=True)
    ADMINUSER_PASSWORD = models.CharField(max_length=400, null=True, blank=True)
    ADMINUSER_Create_Date = models.DateTimeField(default=now, editable=False)
    ADMINUSER_Update_Date = models.DateTimeField(default=(now() + timedelta(hours=24)), editable=False)
    ADMINUSER_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'ADMIN_USER_MODEL'

    def CREATE_USER(self, USERNAME, EMAIL, PHONE_NUMBER, FULLNAME, BILLING_ADDRESS, PASSWORD):
        try:
            USERNAME_CHECK = ADMIN_USER_MODEL.objects.filter(ADMINUSER_USERNAME=USERNAME)
            if (len(USERNAME_CHECK) > 0):
                return 0

            EMAIL_CHECK = ADMIN_USER_MODEL.objects.filter(ADMINUSER_EMAIL=EMAIL)
            if (len(EMAIL_CHECK) > 0):
                return 1

            OBJECT_USER = ADMIN_USER_MODEL(
                ADMINUSER_USERNAME=USERNAME,
                ADMINUSER_EMAIL=EMAIL,
                ADMINUSER_PHONE_NUMBER=PHONE_NUMBER,
                ADMINUSER_FULLNAME=FULLNAME,
                ADMINUSER_BILLING_ADDRESS=BILLING_ADDRESS,
                ADMINUSER_PASSWORD=PASSWORD
            )
            OBJECT_USER.save()
            return 2
        except:
            return 3

    def LOGIN_USER(self, USERNAME, PASSWORD):
        try:
            USERNAME_CHECK = ADMIN_USER_MODEL.objects.filter(ADMINUSER_USERNAME=USERNAME).filter(
                ADMINUSER_PASSWORD=PASSWORD)
            if (len(USERNAME_CHECK) > 0):
                return USERNAME_CHECK[0]
            return 0
        except:
            return 3


