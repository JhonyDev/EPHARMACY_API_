# Generated by Django 3.2.4 on 2023-02-05 07:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MEDICINE_PRODUCTS_MODEL',
            fields=[
                ('MEDICINEPRODUCTS_INDEX_KEY', models.AutoField(primary_key=True, serialize=False)),
                ('MEDICINEPRODUCTS_ID', models.CharField(blank=True, max_length=50, null=True)),
                ('MEDICINEPRODUCTS_MEDICINENAME', models.CharField(blank=True, max_length=400, null=True)),
                ('MEDICINEPRODUCTS_MANUFACTURERNAME', models.CharField(blank=True, max_length=400, null=True)),
                ('MEDICINEPRODUCTS_STRENGTH', models.CharField(blank=True, max_length=400, null=True)),
                ('MEDICINEPRODUCTS_IMAGE', models.CharField(blank=True, max_length=400, null=True)),
                ('MEDICINEPRODUCTS_SERVICEPROVIDER', models.CharField(blank=True, max_length=400, null=True)),
                ('MEDICINEPRODUCTS_PRESCRIPTIONREQUIRED', models.CharField(blank=True, max_length=400, null=True)),
                ('MEDICINEPRODUCTS_COMPOSITION', models.CharField(blank=True, max_length=400, null=True)),
                ('MEDICINEPRODUCTSPRICES_MRP', models.CharField(blank=True, max_length=400, null=True)),
                ('MEDICINEPRODUCTSPRICES_SALEPRICE', models.CharField(blank=True, max_length=200, null=True)),
                ('MEDICINEPRODUCTSPRICES_DISCOUNT', models.CharField(blank=True, max_length=30, null=True)),
                ('MEDICINEPRODUCTSPRICES_QUANTITY', models.CharField(blank=True, max_length=15, null=True)),
                ('MEDICINEPRODUCTS_Create_Date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('MEDICINEPRODUCTS_Update_Date', models.DateTimeField(default=datetime.datetime(2023, 2, 6, 7, 57, 45, 290677, tzinfo=utc), editable=False)),
                ('MEDICINEPRODUCTS_isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'MEDICINE_PRODUCTS',
            },
        ),
        migrations.CreateModel(
            name='MEDICINE_PRODUCTS_PRICES_MODEL',
            fields=[
                ('MEDICINEPRODUCTSPRICES_INDEX_KEY', models.AutoField(primary_key=True, serialize=False)),
                ('MEDICINEPRODUCTSPRICES_INDEX_ID', models.IntegerField(blank=True, null=True)),
                ('MEDICINEPRODUCTSPRICES_MRP', models.CharField(blank=True, max_length=400, null=True)),
                ('MEDICINEPRODUCTSPRICES_SALEPRICE', models.CharField(blank=True, max_length=200, null=True)),
                ('MEDICINEPRODUCTSPRICES_DISCOUNT', models.CharField(blank=True, max_length=30, null=True)),
                ('MEDICINEPRODUCTSPRICES_QUANTITY', models.CharField(blank=True, max_length=15, null=True)),
                ('MEDICINEPRODUCTSPRICES_Create_Date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('MEDICINEPRODUCTSPRICES_Update_Date', models.DateTimeField(default=datetime.datetime(2023, 2, 6, 7, 57, 45, 321684, tzinfo=utc), editable=False)),
                ('MEDICINEPRODUCTSPRICES_isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'MEDICINE_PRODUCTS_PRICES',
            },
        ),
    ]