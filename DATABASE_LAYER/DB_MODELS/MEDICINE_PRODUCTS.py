import pandas as pd
from django.db import models
from django.utils.timezone import now, timedelta


# from DATABASE_LAYER.DB_MODELS.MEDICINE_PRODUCTS_PRICES import MEDICINE_PRODUCTS_PRICES_MODEL

class MEDICINE_PRODUCTS_MODEL(models.Model):
    MEDICINEPRODUCTS_INDEX_KEY = models.AutoField(primary_key=True)
    # FORIEGNKEY_MEDICINEPRODUCTSPRICES = models.ForeignKey(MEDICINE_PRODUCTS_PRICES_MODEL,on_delete=models.DO_NOTHING)
    MEDICINEPRODUCTS_ID = models.CharField(max_length=50, null=True, blank=True)
    MEDICINEPRODUCTS_MEDICINENAME = models.CharField(max_length=400, null=True, blank=True)
    MEDICINEPRODUCTS_MANUFACTURERNAME = models.CharField(max_length=400, null=True, blank=True)
    MEDICINEPRODUCTS_STRENGTH = models.CharField(max_length=400, null=True, blank=True)
    MEDICINEPRODUCTS_IMAGE = models.CharField(max_length=400, null=True, blank=True)
    MEDICINEPRODUCTS_SERVICEPROVIDER = models.CharField(max_length=400, null=True, blank=True)
    MEDICINEPRODUCTS_PRESCRIPTIONREQUIRED = models.CharField(max_length=400, null=True, blank=True)
    MEDICINEPRODUCTS_COMPOSITION = models.CharField(max_length=400, null=True, blank=True)
    MEDICINEPRODUCTSPRICES_MRP = models.CharField(max_length=400, null=True, blank=True)
    MEDICINEPRODUCTSPRICES_SALEPRICE = models.CharField(max_length=200, null=True, blank=True)
    MEDICINEPRODUCTSPRICES_DISCOUNT = models.CharField(max_length=30, null=True, blank=True)
    MEDICINEPRODUCTSPRICES_QUANTITY = models.CharField(max_length=15, null=True, blank=True)
    MEDICINEPRODUCTS_Create_Date = models.DateTimeField(default=now, editable=False)
    MEDICINEPRODUCTS_Update_Date = models.DateTimeField(default=(now() + timedelta(hours=24)), editable=False)
    MEDICINEPRODUCTS_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'MEDICINE_PRODUCTS'

    def INSERT_TO_TABLE(self, FK_OBJECT, ID, NAME, M_NAME, STRENGTH, IMAGE, SERVICEPROVIDER, RX_REQ, SALTS):
        try:
            OBJECT_TABLE = MEDICINE_PRODUCTS_MODEL(
                FORIEGNKEY_MEDICINEPRODUCTSPRICES=FK_OBJECT,
                MEDICINEPRODUCTS_ID=ID,
                MEDICINEPRODUCTS_MEDICINENAME=NAME,
                MEDICINEPRODUCTS_MANUFACTURERNAME=M_NAME,
                MEDICINEPRODUCTS_STRENGTH=STRENGTH,
                MEDICINEPRODUCTS_IMAGE=IMAGE,
                MEDICINEPRODUCTS_SERVICEPROVIDER=SERVICEPROVIDER,
                MEDICINEPRODUCTS_PRESCRIPTIONREQUIRED=RX_REQ,
                MEDICINEPRODUCTS_COMPOSITION=SALTS
            )
            OBJECT_TABLE.save()
            print("SAVED SUCCESSFULLY!")
        except:
            pass

    def SEED_DATABASE(self):
        df = pd.read_csv("COMBINED_MEDICINES.csv", low_memory=False)
        REC = []
        # for index,row in df.iterrows():
        #     REC.append(MEDICINE_PRODUCTS_PRICES_MODEL(
        #             MEDICINEPRODUCTSPRICES_MRP = row["MRP_PRICE"],
        #             MEDICINEPRODUCTSPRICES_SALEPRICE = row["OFFERED_PRICE"],
        #             MEDICINEPRODUCTSPRICES_DISCOUNT = row["DISCOUNT_OFFERED"],
        #             MEDICINEPRODUCTSPRICES_QUANTITY = row["PRODUCT_QUANTITY"],
        #             MEDICINEPRODUCTSPRICES_INDEX_ID = index
        #         ))
        # print("EXECUTION")
        # MEDICINE_PRODUCTS_PRICES_MODEL.objects.bulk_create(REC)

        for index, row in df.iterrows():
            REC.append(MEDICINE_PRODUCTS_MODEL(
                # FORIEGNKEY_MEDICINEPRODUCTSPRICES = MEDICINE_PRODUCTS_PRICES_MODEL.objects.get(MEDICINEPRODUCTSPRICES_INDEX_ID=index),
                MEDICINEPRODUCTS_ID=row["PRODUCT_ID"],
                MEDICINEPRODUCTS_MEDICINENAME=row["PRODUCT_NAME"],
                MEDICINEPRODUCTS_MANUFACTURERNAME=row["MANUFACTURER_NAME"],
                MEDICINEPRODUCTS_STRENGTH=row["PRODUCT_STRENGTH"],
                MEDICINEPRODUCTS_IMAGE=row["PRODUCT_IMAGE"],
                MEDICINEPRODUCTS_SERVICEPROVIDER=row["SERVICE_PROVIDER"],
                MEDICINEPRODUCTS_PRESCRIPTIONREQUIRED=row["PRESCCRIPTION_REQUIRED"],
                MEDICINEPRODUCTS_COMPOSITION=row["PRODUCT_SALTS"],
                MEDICINEPRODUCTSPRICES_MRP=row["MRP_PRICE"],
                MEDICINEPRODUCTSPRICES_SALEPRICE=row["OFFERED_PRICE"],
                MEDICINEPRODUCTSPRICES_DISCOUNT=row["DISCOUNT_OFFERED"],
                MEDICINEPRODUCTSPRICES_QUANTITY=row["PRODUCT_QUANTITY"]
            ))
        print("EXECUTION")
        MEDICINE_PRODUCTS_MODEL.objects.bulk_create(REC)
