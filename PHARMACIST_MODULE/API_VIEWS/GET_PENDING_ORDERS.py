from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from DATABASE_LAYER.models import JWT_TOKEN_MODEL, PHARMACIST_USERS_MODEL, ORDERS_PLACED_MODEL


class PENDINGORDERS_PHARMACY_VIEW(APIView):
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

    def PLACE_ORDER(self, USER_OBJECT):
        RESULTANT = []
        ALLORDERS = ORDERS_PLACED_MODEL.objects.filter(
            ORDERSPLACED_BID_PROFILE__PHARMICISTBIDDING_PHARMACIST_PROFILE=USER_OBJECT).filter(
            ORDERSPLACED_DELIVERED=False)
        for singleorder in ALLORDERS:
            RESULTANT.append({
                "ORDER_ID": singleorder.ORDERSPLACED_INDEX_KEY,
                "REQUESTED_MEDICINE": singleorder.ORDERSPLACED_CONTRACT_PROFILE.CUSTOMERPHARMACIST_KEYWORD,
                "BID_MEDICINE_NAME": singleorder.ORDERSPLACED_BID_PROFILE.PHARMICISTBIDDING_BID_MEDICINENAME,
                "BID_MEDICINE_PRICE": singleorder.ORDERSPLACED_BID_PROFILE.PHARMICISTBIDDING_BID_PRICE,
                "PHARMACY_PROFILE": {
                    "NAME": singleorder.ORDERSPLACED_BID_PROFILE.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_FULLNAME,
                    "ADDRESS": singleorder.ORDERSPLACED_BID_PROFILE.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_SHOP_ADDRESS,
                    "LATITUDE": singleorder.ORDERSPLACED_BID_PROFILE.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_SHOP_LATITUDE,
                    "LONGITUDE": singleorder.ORDERSPLACED_BID_PROFILE.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_SHOP_LONGITUDE,
                    "CONTACT_INFO": singleorder.ORDERSPLACED_BID_PROFILE.PHARMICISTBIDDING_PHARMACIST_PROFILE.PHARMACISTUSERS_SHOP_CONTACT_INFO
                }
            })
        return RESULTANT

    def post(self, request, format=None):
        AUTH_TOKEN = request.headers.get('Authorization')
        USER_OBJECT = self.USER_AUTH_CHECK(AUTH_TOKEN)
        if (USER_OBJECT == None or not (isinstance(USER_OBJECT, PHARMACIST_USERS_MODEL))):
            return Response({"STATUS": "403", "MESSAGE": "UNAUTHORIZED"}, status=status.HTTP_200_OK)

        try:
            RESULTANT = self.PLACE_ORDER(USER_OBJECT)
            return Response(RESULTANT, status=status.HTTP_200_OK, )
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_200_OK)
