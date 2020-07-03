from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Bank.serializers import bankserializer,branchserializer
from Bank.models import Branch,banks

class BankList(APIView):
    def get(self, request):
        model = banks.objects.all()
        serializer = bankserializer(model, many=True)
        return Response(serializer.data)
    # def post(self,request):
    #     serializer = Userserializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Branchdata(APIView):
    def get(self,request):
        model = Branch.objects.all()
        serializer = branchserializer(model, many=True)
        return Response(serializer.data)

# class temperature_reading(APIView):
#     def post(self,request):
#         serializer = readingserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
