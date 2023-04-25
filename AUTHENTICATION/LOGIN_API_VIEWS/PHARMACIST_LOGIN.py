from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DATABASE_LAYER.models import PHARMACIST_USERS_MODEL

class LOGIN_PHARMACIST_APIVIEW(APIView):
    def LOGIN_CHECK(self,USERNAME,PASSWORD):
        RESP = PHARMACIST_USERS_MODEL().LOGIN_USER(USERNAME,PASSWORD)
        if(isinstance(RESP,PHARMACIST_USERS_MODEL)):
            return {
                "STATUS": "200",
                "MESSAGE": "LOGGED IN SUCCESSFULLY!",
                "USER-DATA":{
                    "FULL NAME":RESP.PHARMACISTUSERS_FULLNAME,
                    "EMAIL":RESP.PHARMACISTUSERS_EMAIL,
                    "PHONE NUMBER":RESP.PHARMACISTUSERS_PHONE_NUMBER,
                    "ADDRESS":RESP.PHARMACISTUSERS_SHOP_ADDRESS,
                    "USERNAME":RESP.PHARMACISTUSERS_USERNAME,
                    "CONTACT INFO":RESP.PHARMACISTUSERS_SHOP_CONTACT_INFO
                }
            }
        elif(RESP == 0):
            return {
                "STATUS":"400",
                "MESSAGE":"INVALID PASSWORD/USERNAME"
            }
        else:
            return {
                "STATUS": "400",
                "MESSAGE": "ERROR OCCURED"
            }

    def post(self, request, format=None):
        try:
            USERNAME = dict(request.data)["USERNAME"][0]
            PASSWORD = dict(request.data)["PASSWORD"][0]
            RESULTANT = self.LOGIN_CHECK(USERNAME,PASSWORD)
            return Response(RESULTANT, status=status.HTTP_200_OK, )
        except:
            return Response({}, status=status.HTTP_200_OK)

        return Response({}, status=status.HTTP_200_OK, )
