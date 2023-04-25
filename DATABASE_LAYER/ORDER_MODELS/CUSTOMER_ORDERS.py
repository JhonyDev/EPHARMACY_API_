from django.db import models
import pandas as pd
from django.utils.timezone import now,timedelta
from DATABASE_LAYER.models import PHARMICIST_BIDDING_MODEL,CUSTOMER_PHARMACIST_ALERT_MODEL

class ORDERS_PLACED_MODEL(models.Model):
    ORDERSPLACED_INDEX_KEY = models.AutoField(primary_key=True)
    ORDERSPLACED_CONTRACT_PROFILE = models.ForeignKey(CUSTOMER_PHARMACIST_ALERT_MODEL,null=True,blank=True,on_delete=models.DO_NOTHING)
    ORDERSPLACED_BID_PROFILE = models.ForeignKey(PHARMICIST_BIDDING_MODEL,null=True,blank=True,on_delete=models.DO_NOTHING)
    ORDERSPLACED_DELIVERED = models.BooleanField(default=False)
    ORDERSPLACED_Create_Date = models.DateTimeField(default=now, editable=False)
    ORDERSPLACED_Update_Date = models.DateTimeField(default=(now() + timedelta(hours=24)), editable=False)
    ORDERSPLACED_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'ORDERS_PLACED_MODEL'