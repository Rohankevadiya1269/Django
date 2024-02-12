from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import UserDetail

class PostEmployee(APIView):
# Create your views here.

    
    
    def post(self, request,**kwargs):
        employeeSerializerPost = EmployeeSerializer(data=request.data)
        if employeeSerializerPost.is_valid():
            try:
                employeeSerializerPost.save()
            except Exception as e:
                print(e)
            print(request.data,"----------------------------")
            return Response(employeeSerializerPost.data)
        else:
            return Response(employeeSerializerPost.errors)

class GetEmployee(APIView):
        def get(self,request) :
            queryset = UserDetail.objects.all()
            print(queryset,'-------->')
            employeeSerializerGet = EmployeeSerializer(queryset,many=True)
            print('************************************',employeeSerializerGet.data)
            return Response(employeeSerializerGet.data)
    