# Generated by Django 3.1.14 on 2023-04-25 07:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('DATABASE_LAYER', '0005_auto_20230205_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_user_model',
            name='ADMINUSER_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 7, 30, 26, 863110, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='customer_pharmacist_alert_model',
            name='CUSTOMERPHARMACIST_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 7, 30, 26, 908374, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='customer_user_model',
            name='CUSTOMERUSER_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 7, 30, 26, 893082, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='jwt_token_model',
            name='JWTTOKEN_TOKEN_VALUE',
            field=models.CharField(blank=True, default=uuid.UUID('9d71b8e2-e59a-42b9-b8b8-e70b0fd50a78'), max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='jwt_token_model',
            name='JWTTOKEN_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 7, 30, 26, 896164, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='medicine_products_model',
            name='MEDICINEPRODUCTS_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 7, 30, 26, 900847, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='medicine_products_prices_model',
            name='MEDICINEPRODUCTSPRICES_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 7, 30, 26, 903949, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='orders_placed_model',
            name='ORDERSPLACED_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 7, 30, 26, 913885, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='pharmacist_users_model',
            name='PHARMACISTUSERS_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 7, 30, 26, 891087, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='pharmicist_bidding_model',
            name='CUSTOMERPHARMACIST_Update_Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 7, 30, 26, 910894, tzinfo=utc), editable=False),
        ),
    ]
