from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class UserRegister(APIView):
    def post(self,request):
        srz_data = UserRegisterSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)