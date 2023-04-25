from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DATABASE_LAYER.models import JWT_TOKEN_MODEL,CUSTOMER_PHARMACIST_ALERT_MODEL,PHARMACIST_USERS_MODEL
from DATABASE_LAYER.models import MEDICINE_PRODUCTS_MODEL

class PENDING_ALERTS_LOCAL_PHARMICISTS_VIEW(APIView):
    def USER_AUTH_CHECK(self,TOKEN):
        USER_OBJECT = JWT_TOKEN_MODEL.objects.filter(JWTTOKEN_TOKEN_VALUE=TOKEN)
        if(len(USER_OBJECT) > 0):
            if(USER_OBJECT[0].JWTTOKEN_FK_ADMIN == None and USER_OBJECT[0].JWTTOKEN_FK_PHARMACIST == None):
                return USER_OBJECT[0].JWTTOKEN_FK_CUSTOMER
            elif(USER_OBJECT[0].JWTTOKEN_FK_ADMIN == None and USER_OBJECT[0].JWTTOKEN_FK_CUSTOMER == None):
                return USER_OBJECT[0].JWTTOKEN_FK_PHARMACIST
            else:
                return USER_OBJECT[0].JWTTOKEN_FK_ADMIN

        return None

    def MEDICINE_SEARCH_DB(self,keyword):
        RESULTANT = {}
        MEDICINES = MEDICINE_PRODUCTS_MODEL.objects.filter(MEDICINEPRODUCTS_MEDICINENAME__icontains = keyword)
        RESULTANT["COUNT"] = str(len(MEDICINES))
        RESULTANT["MEDICINES"] = []
        for singlemedicine in MEDICINES:
            RESULTANT["MEDICINES"].append({
                "NAME":singlemedicine.MEDICINEPRODUCTS_MEDICINENAME,
                "MANUFACTURER":singlemedicine.MEDICINEPRODUCTS_MANUFACTURERNAME,
                "PRESCRIPTION_REQUIRED": singlemedicine.MEDICINEPRODUCTS_PRESCRIPTIONREQUIRED,
                "COMPOSITION": singlemedicine.MEDICINEPRODUCTS_COMPOSITION,
                "MRP":singlemedicine.MEDICINEPRODUCTSPRICES_MRP,
                "SALE_PRICE":singlemedicine.MEDICINEPRODUCTSPRICES_SALEPRICE,
                "DISCOUNT": singlemedicine.MEDICINEPRODUCTSPRICES_DISCOUNT,
                "SERVICE_PROVIDER": singlemedicine.MEDICINEPRODUCTS_SERVICEPROVIDER,
            })

        return RESULTANT

    def PRICE_RECOMMENDATIONS(self,keyword):
        PRICE_RECOM = {}
        TOP_10_PRICES = []
        MEDICINES = self.MEDICINE_SEARCH_DB(keyword)
        newlist = sorted(MEDICINES["MEDICINES"], key=lambda d: float(d['SALE_PRICE']), reverse=False)
        if(len(newlist) > 30):
            for i in range(0,11):
                TOP_10_PRICES.append(float(newlist[i]["SALE_PRICE"]))
            PRICE_RECOM["FIRST_SLOT"] = sum(TOP_10_PRICES) / len(TOP_10_PRICES)
            # print(PRICE_RECOM)

            TOP_10_PRICES = []
            for i in range(11,21):
                TOP_10_PRICES.append(float(newlist[i]["SALE_PRICE"]))
            PRICE_RECOM["SECOND_SLOT"] = sum(TOP_10_PRICES) / len(TOP_10_PRICES)
            # print(PRICE_RECOM)

            TOP_10_PRICES = []
            for i in range(21, 31):
                TOP_10_PRICES.append(float(newlist[i]["SALE_PRICE"]))
            PRICE_RECOM["THIRD_SLOT"] = sum(TOP_10_PRICES) / len(TOP_10_PRICES)
            # print(PRICE_RECOM)
        else:
            for i in range(0,11):
                TOP_10_PRICES.append(float(newlist[i]["SALE_PRICE"]))
            PRICE_RECOM["FIRST_SLOT"] = sum(TOP_10_PRICES) / len(TOP_10_PRICES)
        return PRICE_RECOM

    def ALERT_LOCAL_PHARMACISTS(self):
        RESULTANT = []
        TDO = CUSTOMER_PHARMACIST_ALERT_MODEL.objects.filter(CUSTOMERPHARMACIST_isActive=True)
        for singlealert in TDO:
            PRICE_RECOMMENDATIONS = self.PRICE_RECOMMENDATIONS(singlealert.CUSTOMERPHARMACIST_KEYWORD)
            RESULTANT.append({
                "KEYWORD":singlealert.CUSTOMERPHARMACIST_KEYWORD,
                "LAT": singlealert.CUSTOMERPHARMACIST_LAT,
                "LONG": singlealert.CUSTOMERPHARMACIST_LONG,
                "CREATED_DATE": singlealert.CUSTOMERPHARMACIST_Create_Date,
                "ID": singlealert.CUSTOMERPHARMACIST_INDEX_KEY,
                "PRICE_SUGGESTION":PRICE_RECOMMENDATIONS
            })
        return {"STATUS":"200","MESSAGE":RESULTANT}

    def post(self, request, format=None):
        AUTH_TOKEN = request.headers.get('Authorization')
        USER_OBJECT = self.USER_AUTH_CHECK(AUTH_TOKEN)
        if(USER_OBJECT == None or not(isinstance(USER_OBJECT,PHARMACIST_USERS_MODEL))):
            return Response({"STATUS":"403","MESSAGE":"UNAUTHORIZED"}, status=status.HTTP_200_OK)

        try:
            RESULTANT = self.ALERT_LOCAL_PHARMACISTS()
            return Response(RESULTANT, status=status.HTTP_200_OK, )
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_200_OK)

