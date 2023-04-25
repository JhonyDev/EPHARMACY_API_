from django.db import models
import pandas as pd
from django.utils.timezone import now,timedelta
from DATABASE_LAYER.models import CUSTOMER_USER_MODEL

class CUSTOMER_PHARMACIST_ALERT_MODEL(models.Model):
    CUSTOMERPHARMACIST_INDEX_KEY = models.AutoField(primary_key=True)
    CUSTOMERPHARMACIST_KEYWORD = models.CharField(max_length=400, null=True, blank=True)
    CUSTOMERPHARMACIST_LAT = models.CharField(max_length=400, null=True, blank=True)
    CUSTOMERPHARMACIST_LONG = models.CharField(max_length=400, null=True, blank=True)
    CUSTOMERPHARMACIST_CUSTOMER_PROFILE = models.ForeignKey(CUSTOMER_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING)
    CUSTOMERPHARMACIST_Create_Date = models.DateTimeField(default=now, editable=False)
    CUSTOMERPHARMACIST_Update_Date = models.DateTimeField(default=(now() + timedelta(hours=24)), editable=False)
    CUSTOMERPHARMACIST_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'CUSTOMER_PHARMACIST_ALERT_MODEL'

