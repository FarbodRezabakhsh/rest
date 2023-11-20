from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from .models import Person,Question,Answer
from .serializers import PersonSerializer,QuestionSerializer,AnswerSerializer
from rest_framework import status
from permissions import IsOwnerOrReadOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle


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


class QuestionListView(APIView):
    def get(self,request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions,many=True)
        return Response(srz_data.data,status=status.HTTP_200_OK)

class QuestionCreateView(APIView):
    """
    Create new Question.
    """
    serializer_class = QuestionSerializer

    permission_classes = [IsAuthenticated]
    def post(self,request):
        srz_data = QuestionSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def put(self,request,pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        srz_data = QuestionSerializer(instance=question,data=request.POST,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def delete(self,request,pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message':'question deleted'},status=status.HTTP_200_OK)