from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DATABASE_LAYER.models import JWT_TOKEN_MODEL,CUSTOMER_PHARMACIST_ALERT_MODEL

class ALERT_LOCAL_PHARMICISTS_VIEW(APIView):
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

    def ALERT_LOCAL_PHARMACISTS(self,KEYWORD,USEROBJ,LAT,LONG):
        TDO = CUSTOMER_PHARMACIST_ALERT_MODEL(
            CUSTOMERPHARMACIST_KEYWORD = KEYWORD,
            CUSTOMERPHARMACIST_CUSTOMER_PROFILE = USEROBJ,
            CUSTOMERPHARMACIST_LAT = LAT,
            CUSTOMERPHARMACIST_LONG = LONG
        )
        TDO.save()
        return {"STATUS":"200","MESSAGE":"ALERT GENERATED SUCCESSFULLY!","DATA":{"ID":TDO.CUSTOMERPHARMACIST_INDEX_KEY}}

    def post(self, request, format=None):
        AUTH_TOKEN = request.headers.get('Authorization')
        USER_OBJECT = self.USER_AUTH_CHECK(AUTH_TOKEN)
        if(USER_OBJECT == None):
            return Response({"STATUS":"403","MESSAGE":"UNAUTHORIZED"}, status=status.HTTP_200_OK)

        try:
            KEYWORD = dict(request.data)["KEYWORD"][0]
            LAT = dict(request.data)["LAT"][0]
            LONG = dict(request.data)["LONG"][0]
            RESULTANT = self.ALERT_LOCAL_PHARMACISTS(KEYWORD, USER_OBJECT,LAT,LONG)
            return Response(RESULTANT, status=status.HTTP_200_OK, )
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_200_OK)

