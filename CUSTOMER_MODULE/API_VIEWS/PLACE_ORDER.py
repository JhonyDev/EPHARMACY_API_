from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DATABASE_LAYER.models import JWT_TOKEN_MODEL,CUSTOMER_USER_MODEL,PHARMICIST_BIDDING_MODEL,ORDERS_PLACED_MODEL

class ORDER_PLACED_VIEW(APIView):
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

    def PLACE_ORDER(self,CONTRACT_ID, USER_OBJECT):
        BID = PHARMICIST_BIDDING_MODEL.objects.filter(PHARMICISTBIDDING_INDEX_KEY=CONTRACT_ID)
        if(len(BID) > 0):
            ORDERS_OLD_CHECK = ORDERS_PLACED_MODEL.objects.filter(ORDERSPLACED_BID_PROFILE=BID[0])
            if(len(ORDERS_OLD_CHECK) > 0):
                return {"STATUS": "200", "MESSAGE": "ALREADY SUCCESSFUL"}

            TDO = ORDERS_PLACED_MODEL(
                ORDERSPLACED_BID_PROFILE = BID[0],
                ORDERSPLACED_CONTRACT_PROFILE = BID[0].PHARMICISTBIDDING_CONTRACT_PROFILE,
            )
            TDO.save()

            CLOSE_CONTRACT = BID[0]
            CLOSE_CONTRACT.PHARMICISTBIDDING_CONTRACT_PROFILE.CUSTOMERPHARMACIST_isActive = False
            CLOSE_CONTRACT.save()
            return {"STATUS": "200", "MESSAGE": "SUCCESSFUL"}
        else:
            return {"STATUS": "403", "MESSAGE": "UNSUCCESSFUL"}

    def post(self, request, format=None):
        AUTH_TOKEN = request.headers.get('Authorization')
        USER_OBJECT = self.USER_AUTH_CHECK(AUTH_TOKEN)
        if (USER_OBJECT == None or not (isinstance(USER_OBJECT, CUSTOMER_USER_MODEL))):
            return Response({"STATUS": "403", "MESSAGE": "UNAUTHORIZED"}, status=status.HTTP_200_OK)

        try:
            CONTRACT_ID = dict(request.data)["ID"][0]
            RESULTANT = self.PLACE_ORDER(CONTRACT_ID, USER_OBJECT)
            return Response(RESULTANT, status=status.HTTP_200_OK, )
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_200_OK)

