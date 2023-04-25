from django.db import models
import pandas as pd
from django.utils.timezone import now,timedelta
from DATABASE_LAYER.models import PHARMACIST_USERS_MODEL,CUSTOMER_PHARMACIST_ALERT_MODEL

class PHARMICIST_BIDDING_MODEL(models.Model):
    PHARMICISTBIDDING_INDEX_KEY = models.AutoField(primary_key=True)
    PHARMICISTBIDDING_BID_MEDICINENAME = models.CharField(max_length=400, null=True, blank=True)
    PHARMICISTBIDDING_BID_PRICE = models.CharField(max_length=400, null=True, blank=True)
    PHARMICISTBIDDING_PHARMACIST_PROFILE = models.ForeignKey(PHARMACIST_USERS_MODEL,null=True,blank=True,on_delete=models.DO_NOTHING)
    PHARMICISTBIDDING_CONTRACT_PROFILE = models.ForeignKey(CUSTOMER_PHARMACIST_ALERT_MODEL, null=True, blank=True,on_delete=models.DO_NOTHING)
    CUSTOMERPHARMACIST_Create_Date = models.DateTimeField(default=now, editable=False)
    CUSTOMERPHARMACIST_Update_Date = models.DateTimeField(default=(now() + timedelta(hours=24)), editable=False)
    CUSTOMERPHARMACIST_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'PHARMICIST_BIDDING_MODEL'