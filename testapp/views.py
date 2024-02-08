from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# third party library imports
from rest_framework.views import APIView 
from rest_framework.response import Response
# the apiview is an repo that allows api request methods such as get, post and etc


class TestView (APIView):
    def get(self,request):
      data ={
        "name": "Rohan",
        "age": 22
    }  
      return Response(data)

# def testView(request):
#     data ={
#         "name": "Rohan",
#         "age": 22
#     }
#     return JsonResponse(data)