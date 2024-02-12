from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# third party library imports
from rest_framework.views import APIView 
from rest_framework.response import Response
# the apiview is an repo that allows api request methods such as get, post and etc
from .serializers import PostSerializer
from .models import Post

class TestView (APIView):
    def get(self,request):
      qs  = Post.objects.all()
      serializer = PostSerializer(qs, many = True) 
      return Response(serializer.data)

    def post(self,request,*args,**kwargs):
          serializer = PostSerializer(data=request.data)
          if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
          else:
                return Response(serializer.errors)

 
# def testView(request):
#     data ={
#         "name": "Rohan",
#         "age": 22
#     }
#     return JsonResponse(data)