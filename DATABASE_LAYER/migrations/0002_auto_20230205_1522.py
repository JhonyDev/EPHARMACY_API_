# Generated by Django 3.2.4 on 2023-02-05 10:22

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('DATABASE_LAYER', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADMIN_USER_MODEL',
            fields=[
                ('ADMINUSER_INDEX_KEY', models.AutoField(primary_key=True, serialize=False)),
                ('ADMINUSER_USERNAME', models.CharField(blank=True, max_length=400, null=True)),
                ('ADMINUSER_EMAIL', models.CharField(blank=True, max_length=400, null=True)),
                ('ADMINUSER_PHONE_NUMBER', models.CharField(blank=True, max_length=400, null=True)),
                ('ADMINUSER_FULLNAME', models.CharField(blank=True, max_length=400, null=True)),
                ('ADMINUSER_BILLING_ADDRESS', models.CharField(blank=True, max_length=400, null=True)),
                ('ADMINUSER_PASSWORD', models.CharField(blank=True, max_length=400, null=True)),
                ('ADMINUSER_Create_Date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('ADMINUSER_Update_Date', models.DateTimeField(default=datetime.datetime(2023, 2, 6, 10, 22, 7, 845285, tzinfo=utc), editable=False)),
                ('ADMINUSER_isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'ADMIN_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='CUSTOMER_USER_MODEL',
            fields=[
                ('CUSTOMERUSER_INDEX_KEY', models.AutoField(primary_key=True, serialize=False)),
                ('CUSTOMERUSER_USERNAME', models.CharField(blank=True, max_length=400, null=True)),
                ('CUSTOMERUSER_EMAIL', models.CharField(blank=True, max_length=400, null=True)),
                ('CUSTOMERUSER_PHONE_NUMBER', models.CharField(blank=True, max_length=400, null=True)),
                ('CUSTOMERUSER_FULLNAME', models.CharField(blank=True, max_length=400, null=True)),
                ('CUSTOMERUSER_BILLING_ADDRESS', models.CharField(blank=True, max_length=400, null=True)),
                ('CUSTOMERUSER_PASSWORD', models.CharField(blank=True, max_length=400, null=True)),
                ('CUSTOMERUSER_Create_Date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('CUSTOMERUSER_Update_Date', models.DateTimeField(default=datetime.datetime(2023, 2, 6, 10, 22, 7, 878292, tzinfo=utc), editable=False)),
                ('CUSTOMERUSER_isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'CUSTOMER_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='PHARMACIST_USERS_MODEL',
            fields=[
                ('PHARMACISTUSERS_INDEX_KEY', models.AutoField(primary_key=True, serialize=False)),
                ('PHARMACISTUSERS_USERNAME', models.CharField(blank=True, max_length=400, null=True)),
                ('PHARMACISTUSERS_EMAIL', models.CharField(blank=True, max_length=400, null=True)),
                ('PHARMACISTUSERS_PHONE_NUMBER', models.CharField(blank=True, max_length=400, null=True)),
                ('PHARMACISTUSERS_FULLNAME', models.CharField(blank=True, max_length=400, null=True)),
                ('PHARMACISTUSERS_SHOP_ADDRESS', models.CharField(blank=True, max_length=400, null=True)),
                ('PHARMACISTUSERS_SHOP_LATITUDE', models.CharField(blank=True, max_length=400, null=True)),
                ('PHARMACISTUSERS_SHOP_LONGITUDE', models.CharField(blank=True, max_length=400, null=True)),
                ('PHARMACISTUSERS_SHOP_CONTACT_INFO', models.CharField(blank=True, max_length=400, null=True)),
                ('PHARMACISTUSERS_PASSWORD', models.CharField(blank=True, max_length=400, null=True)),
                ('PHARMACISTUSERS_Create_Date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('PHARMACISTUSERS_Update_Date', models.DateTimeField(default=datetime.datetime(2023, 2, 6, 10, 22, 7, 877292, tzinfo=utc), editable=False)),
                ('PHARMACISTUSERS_isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'PHARMACIST_USERS_MODEL',
            },
        ),
        migrations.AlterField(
            model_name='medicine_products_model',
            name='MEDICINEPRODUCTS_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 6, 10, 22, 7, 880292, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='medicine_products_prices_model',
            name='MEDICINEPRODUCTSPRICES_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 6, 10, 22, 7, 881293, tzinfo=utc), editable=False),
        ),
        migrations.CreateModel(
            name='JWT_TOKEN_MODEL',
            fields=[
                ('JWTTOKEN_INDEX_KEY', models.AutoField(primary_key=True, serialize=False)),
                ('JWTTOKEN_TOKEN_VALUE', models.CharField(blank=True, default=uuid.UUID('9d691320-6b51-4050-9e38-4153aa3ab2fd'), max_length=400, null=True)),
                ('JWTTOKEN_Create_Date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('JWTTOKEN_Update_Date', models.DateTimeField(default=datetime.datetime(2023, 2, 6, 10, 22, 7, 878292, tzinfo=utc), editable=False)),
                ('JWTTOKEN_isActive', models.BooleanField(default=True)),
                ('JWTTOKEN_FK_ADMIN', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DATABASE_LAYER.admin_user_model')),
                ('JWTTOKEN_FK_CUSTOMER', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DATABASE_LAYER.customer_user_model')),
                ('JWTTOKEN_FK_PHARMACIST', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DATABASE_LAYER.pharmacist_users_model')),
            ],
            options={
                'verbose_name': 'JWT_TOKEN_MODEL',
            },
        ),
    ]
