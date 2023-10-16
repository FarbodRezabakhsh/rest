from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer

# Create your views here.

class UserRegister(APIView):
    def post(self,request):
        srz_data = UserRegisterSerializer(data=request.POST)
        if srz_data.is_valid():
            User.objects.create_user(
                username=srz_data.validated_data['username'],
                email=srz_data.validated_data['email'],
                password=srz_data.validated_data['password']
            )
            return Response(srz_data.data)
        return Response(srz_data.errors)