from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from DATABASE_LAYER.models import JWT_TOKEN_MODEL, CUSTOMER_PHARMACIST_ALERT_MODEL, CUSTOMER_USER_MODEL, \
    PHARMICIST_BIDDING_MODEL


class GET_BIDS_CONTRACT_VIEW(APIView):
    def USER_AUTH_CHECK(self, TOKEN):
        USER_OBJECT = JWT_TOKEN_MODEL.objects.filter(JWTTOKEN_TOKEN_VALUE=TOKEN)
        if (len(USER_OBJECT) > 0):
            if (USER_OBJECT[0].JWTTOKEN_FK_ADMIN == None and USER_OBJECT[0].JWTTOKEN_FK_PHARMACIST == None):
                return USER_OBJECT[0].JWTTOKEN_FK_CUSTOMER
            elif (USER_OBJECT[0].JWTTOKEN_FK_ADMIN == None and USER_OBJECT[0].JWTTOKEN_FK_CUSTOMER == None):
                return USER_OBJECT[0].JWTTOKEN_FK_PHARMACIST
            else:
                return USER_OBJECT[0].JWTTOKEN_FK_ADMIN

        return None

    def BID_PHARMACISTS(self, CONTRACT_ID, USER_OBJECT):
        CONTRACT_DETAILS = CUSTOMER_PHARMACIST_ALERT_MODEL.objects.filter(CUSTOMERPHARMACIST_INDEX_KEY=CONTRACT_ID)
        if (len(CONTRACT_DETAILS) > 0):
            CONTRACT_DETAILS = CONTRACT_DETAILS[0]
            TDO = PHARMICIST_BIDDING_MODEL.objects.filter(PHARMICISTBIDDING_CONTRACT_PROFILE=CONTRACT_DETAILS)
            DATA = []
            for singlebid in TDO:
                DATA.append({
                    "ID": singlebid.PHARMICISTBIDDING_INDEX_KEY,
                    "MEDICINE_DESCRIPTION": singlebid.PHARMICISTBIDDING_BID_MEDICINENAME,
                    "BID_PRICE": singlebid.PHARMICISTBIDDING_BID_PRICE,
                    "SHOP_CONTACT_INFO": singlebid.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_SHOP_CONTACT_INFO,
                    "PHARMACY_NAME": singlebid.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_FULLNAME,
                    "PHARMACY_ADDRESS": singlebid.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_SHOP_ADDRESS,
                    "PHARMACY_SHOP_LAT": singlebid.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_SHOP_LATITUDE,
                    "PHARMACY_SHOP_LONG": singlebid.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_SHOP_LONGITUDE
                })
            return {"STATUS": "200", "MESSAGE": "SUCCESSFUL", "DATA": DATA}
        else:
            return {"STATUS": "400", "MESSAGE": "BID UNSUCCESSFUL!"}

    def post(self, request, format=None):
        AUTH_TOKEN = request.headers.get('Authorization')
        USER_OBJECT = self.USER_AUTH_CHECK(AUTH_TOKEN)
        if (USER_OBJECT == None or not (isinstance(USER_OBJECT, CUSTOMER_USER_MODEL))):
            return Response({"STATUS": "403", "MESSAGE": "UNAUTHORIZED"}, status=status.HTTP_200_OK)

        try:
            CONTRACT_ID = dict(request.data)["CONTRACT_ID"][0]
            RESULTANT = self.BID_PHARMACISTS(CONTRACT_ID, USER_OBJECT)
            return Response(RESULTANT, status=status.HTTP_200_OK, )
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_200_OK)
