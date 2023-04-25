from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DATABASE_LAYER.models import JWT_TOKEN_MODEL

class JWT_ADMIN_APIVIEW(APIView):
    def LOGIN_CHECK(self,USERNAME,PASSWORD):
        RESP = JWT_TOKEN_MODEL().JWT_LOGIN_ADMIN(USERNAME,PASSWORD)
        if(isinstance(RESP,JWT_TOKEN_MODEL)):
            return {
                "STATUS": "200",
                "MESSAGE": "LOGGED IN SUCCESSFULLY!",
                "USER-DATA":{
                    "AUTH-TOKEN":RESP.JWTTOKEN_TOKEN_VALUE,
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
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_200_OK)

        return Response({}, status=status.HTTP_200_OK, )
