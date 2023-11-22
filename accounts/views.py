from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer,UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.core.paginator import Paginator

# Create your views here.

class UserRegister(APIView):
    def post(self,request):
        srz_data = UserRegisterSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

class UserViewSets(viewsets.ViewSet):
    permission_classes = []
    queryset = User.objects.all()


    def list(self,request):
        page_number = self.request.query_params.get('page',1)
        page_size = self.request.query_params.get('limit',2)
        paginator = Paginator(self.queryset,page_size)
        srz_data = UserSerializer(paginator.page(page_number),many=True) 
        return Response(srz_data.data)

    def retrieve(self,request,pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        srz_data = UserSerializer(instance=user)
        return Response(srz_data.data)

    def destroy(self,request,pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        if user != request.user:
            return Response({'permission denied:you are not the owner'})
        user.is_active = False
        user.save()
        return Response({'message':'user deactivated'})

    def partial_update(self,request,pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        if user != request.user:
            return Response({'permission denied':'you are not the owner'})
        srz_data = UserSerializer(instance=user,data=request.POST,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(srz_data.errors)
    
class UserListApi(generics.ListAPIView):
    def get(self,request):
        queryset = User.objects.all()
        srz_class = UserSerializer(instance=queryset,many=True)
        return Response(srz_class.data)
