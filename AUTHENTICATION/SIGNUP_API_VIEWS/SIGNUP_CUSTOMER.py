from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DATABASE_LAYER.models import CUSTOMER_USER_MODEL

class SIGNUP_CUSTOMER_APIVIEW(APIView):

    def CREATE_USER(self,USERNAME,EMAIL,PHONE_NUMBER,FULLNAME,BILLING_ADDRESS,PASSWORD):
        RESP = CUSTOMER_USER_MODEL().CREATE_USER(USERNAME,EMAIL,PHONE_NUMBER,FULLNAME,BILLING_ADDRESS,PASSWORD)
        if(RESP == 0):
            return {
                "STATUS":"400",
                "MESSAGE":"USERNAME ALREADY REGISTERED"
            }
        elif(RESP == 1):
            return {
                "STATUS": "400",
                "MESSAGE": "EMAIL ALREADY REGISTERED"
            }
        elif (RESP == 2):
            return {
                "STATUS": "200",
                "MESSAGE": "SUCCESSFULLY REGISTERED"
            }
        else:
            return {
                "STATUS": "400",
                "MESSAGE": "ERROR OCCURED"
            }

    def post(self, request, format=None):
        try:
            USERNAME = dict(request.data)["USERNAME"][0]
            EMAIL = dict(request.data)["EMAIL"][0]
            PHONE_NUMBER = dict(request.data)["PHONE_NUMBER"][0]
            FULLNAME = dict(request.data)["FULLNAME"][0]
            BILLING_ADDRESS = dict(request.data)["BILLING_ADDRESS"][0]
            PASSWORD = dict(request.data)["PASSWORD"][0]
            RESULTANT = self.CREATE_USER(USERNAME,EMAIL,PHONE_NUMBER,FULLNAME,BILLING_ADDRESS,PASSWORD)
            return Response(RESULTANT, status=status.HTTP_200_OK, )
        except:
            return Response({}, status=status.HTTP_200_OK)

        return Response({}, status=status.HTTP_200_OK, )
