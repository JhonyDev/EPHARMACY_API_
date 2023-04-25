from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DATABASE_LAYER.models import JWT_TOKEN_MODEL,CUSTOMER_PHARMACIST_ALERT_MODEL,PHARMACIST_USERS_MODEL,PHARMICIST_BIDDING_MODEL

class BID_CONTRACT_PHARMACIST_VIEW(APIView):
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

    def BID_PHARMACISTS(self,CONTRACT_ID, DESCRIPTION,PRICE, USER_OBJECT):
        CONTRACT_DETAILS = CUSTOMER_PHARMACIST_ALERT_MODEL.objects.filter(CUSTOMERPHARMACIST_INDEX_KEY=CONTRACT_ID)
        if(len(CONTRACT_DETAILS) > 0):
            CONTRACT_DETAILS = CONTRACT_DETAILS[0]
            TDO = PHARMICIST_BIDDING_MODEL(
                PHARMICISTBIDDING_BID_MEDICINENAME = DESCRIPTION,
                PHARMICISTBIDDING_BID_PRICE = PRICE,
                PHARMICISTBIDDING_CONTRACT_PROFILE = CONTRACT_DETAILS,
                PHARMICISTBIDDING_PHARMACIST_PROFILE = USER_OBJECT
            )
            TDO.save()
            return {"STATUS": "200", "MESSAGE": "BID SUCCESSFUL!"}
        else:
            return {"STATUS": "400", "MESSAGE": "BID UNSUCCESSFUL!"}

    def post(self, request, format=None):
        AUTH_TOKEN = request.headers.get('Authorization')
        USER_OBJECT = self.USER_AUTH_CHECK(AUTH_TOKEN)
        if (USER_OBJECT == None or not (isinstance(USER_OBJECT, PHARMACIST_USERS_MODEL))):
            return Response({"STATUS": "403", "MESSAGE": "UNAUTHORIZED"}, status=status.HTTP_200_OK)

        try:
            CONTRACT_ID = dict(request.data)["CONTRACT_ID"][0]
            DESCRIPTION = dict(request.data)["MEDICINE_DESCRIPTION"][0]
            PRICE = dict(request.data)["PRICE"][0]
            RESULTANT = self.BID_PHARMACISTS(CONTRACT_ID, DESCRIPTION,PRICE, USER_OBJECT)
            return Response(RESULTANT, status=status.HTTP_200_OK, )
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_200_OK)

