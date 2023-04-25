from django.db import models
import pandas as pd
from django.utils.timezone import now,timedelta
from DATABASE_LAYER.USER_MODELS.ADMIN_USER import ADMIN_USER_MODEL
from DATABASE_LAYER.USER_MODELS.PHARMACISTS_USER import PHARMACIST_USERS_MODEL
from DATABASE_LAYER.USER_MODELS.CUSTOMER_USER import CUSTOMER_USER_MODEL
from uuid import uuid4

class JWT_TOKEN_MODEL(models.Model):
    JWTTOKEN_INDEX_KEY = models.AutoField(primary_key=True)
    JWTTOKEN_TOKEN_VALUE = models.CharField(max_length=400, null=True, blank=True, default=uuid4())
    JWTTOKEN_FK_CUSTOMER = models.ForeignKey(CUSTOMER_USER_MODEL,null=True,blank=True,on_delete=models.DO_NOTHING)
    JWTTOKEN_FK_PHARMACIST = models.ForeignKey(PHARMACIST_USERS_MODEL,null=True,blank=True,on_delete=models.DO_NOTHING)
    JWTTOKEN_FK_ADMIN = models.ForeignKey(ADMIN_USER_MODEL,null=True,blank=True,on_delete=models.DO_NOTHING)
    JWTTOKEN_Create_Date = models.DateTimeField(default=now, editable=False)
    JWTTOKEN_Update_Date = models.DateTimeField(default=(now() + timedelta(hours=24)), editable=False)
    JWTTOKEN_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'JWT_TOKEN_MODEL'

    def JWT_LOGIN_USER(self,USERNAME,PASSWORD):
        try:
            USERNAME_CHECK = CUSTOMER_USER_MODEL.objects.filter(CUSTOMERUSER_USERNAME=USERNAME).filter(CUSTOMERUSER_PASSWORD=PASSWORD)
            if(len(USERNAME_CHECK) > 0):
                CHECK_USER_JWT = JWT_TOKEN_MODEL.objects.filter(JWTTOKEN_FK_CUSTOMER=USERNAME_CHECK[0])
                if(len(CHECK_USER_JWT) > 0):
                    return CHECK_USER_JWT[0]
                else:
                    TDO = JWT_TOKEN_MODEL(
                        JWTTOKEN_FK_CUSTOMER = USERNAME_CHECK[0]
                    )
                    TDO.save()
                    return TDO
            return 0
        except Exception as e:
            print(e)
            return 3

    def JWT_LOGIN_PHARMACIST(self,USERNAME,PASSWORD):
        try:
            USERNAME_CHECK = PHARMACIST_USERS_MODEL.objects.filter(PHARMACISTUSERS_USERNAME=USERNAME).filter(PHARMACISTUSERS_PASSWORD=PASSWORD)
            if(len(USERNAME_CHECK) > 0):
                CHECK_USER_JWT = JWT_TOKEN_MODEL.objects.filter(JWTTOKEN_FK_PHARMACIST=USERNAME_CHECK[0])
                if(len(CHECK_USER_JWT) > 0):
                    return CHECK_USER_JWT[0]
                else:
                    TDO = JWT_TOKEN_MODEL(
                        JWTTOKEN_FK_PHARMACIST = USERNAME_CHECK[0]
                    )
                    TDO.save()
                    return TDO
            return 0
        except Exception as e:
            print(e)
            return 3

    def JWT_LOGIN_ADMIN(self,USERNAME,PASSWORD):
        try:
            USERNAME_CHECK = ADMIN_USER_MODEL.objects.filter(ADMINUSER_USERNAME=USERNAME).filter(ADMINUSER_PASSWORD=PASSWORD)
            if(len(USERNAME_CHECK) > 0):
                CHECK_USER_JWT = JWT_TOKEN_MODEL.objects.filter(JWTTOKEN_FK_ADMIN=USERNAME_CHECK[0])
                if(len(CHECK_USER_JWT) > 0):
                    return CHECK_USER_JWT[0]
                else:
                    TDO = JWT_TOKEN_MODEL(
                        JWTTOKEN_FK_ADMIN = USERNAME_CHECK[0]
                    )
                    TDO.save()
                    return TDO
            return 0
        except Exception as e:
            print(e)
            return 3