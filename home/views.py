from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from .models import Person
from .serializers import PersonSerializer

# Create your views here.

class Home(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        person = Person.objects.all()
        srz_data = PersonSerializer(instance=person,many=True)
        return Response(data=srz_data.data)

    def post(self,request):
        name = request.data['name']
        return Response({'name':name})