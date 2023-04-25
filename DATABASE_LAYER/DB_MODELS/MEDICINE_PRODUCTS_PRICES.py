from django.db import models
import pandas as pd
from django.utils.timezone import now, timedelta

class MEDICINE_PRODUCTS_PRICES_MODEL(models.Model):
    MEDICINEPRODUCTSPRICES_INDEX_KEY = models.AutoField(primary_key=True)
    MEDICINEPRODUCTSPRICES_INDEX_ID = models.IntegerField(null=True, blank=True)
    MEDICINEPRODUCTSPRICES_MRP = models.CharField(max_length=400, null=True, blank=True)
    MEDICINEPRODUCTSPRICES_SALEPRICE = models.CharField(max_length=200, null=True, blank=True)
    MEDICINEPRODUCTSPRICES_DISCOUNT = models.CharField(max_length=30, null=True, blank=True)
    MEDICINEPRODUCTSPRICES_QUANTITY = models.CharField(max_length=15, null=True, blank=True)
    MEDICINEPRODUCTSPRICES_Create_Date = models.DateTimeField(default=now, editable=False)
    MEDICINEPRODUCTSPRICES_Update_Date = models.DateTimeField(default=(now() + timedelta(hours=24)), editable=False)
    MEDICINEPRODUCTSPRICES_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'MEDICINE_PRODUCTS_PRICES'


