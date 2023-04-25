from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DATABASE_LAYER.models import MEDICINE_PRODUCTS_MODEL

class SEARCH_MEDICINE_BY_SALTS_VIEW(APIView):
    def MEDICINE_SEARCH_DB(self,keyword):
        RESULTANT = {}
        MEDICINES = MEDICINE_PRODUCTS_MODEL.objects.filter(MEDICINEPRODUCTS_COMPOSITION__icontains = keyword[0])
        for singlesalt in keyword:
            MEDICINES = MEDICINES.filter(MEDICINEPRODUCTS_COMPOSITION__icontains = singlesalt)

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

    def post(self, request, format=None):
        try:
            KEYWORD = dict(request.data)["INPUT"][0]
            ALLSALTS = KEYWORD.split(",")
        except:
            return Response({}, status=status.HTTP_200_OK)

        RESULTANT = self.MEDICINE_SEARCH_DB(ALLSALTS)
        return Response(RESULTANT, status=status.HTTP_200_OK, )
