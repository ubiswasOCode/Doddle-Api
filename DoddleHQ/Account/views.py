from django.shortcuts import render
from django.http import HttpResponse
from.models import *
from.serializers import *
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.hashers import check_password
# Create your views here.


def Index(request):


   return render(request,"Home.html")

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.",
        })



class LoginApi(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        email = data['email']
        password = data['password']
        try:
            user = User.objects.get(email = email)
            validate = check_password(password, user.password)
            if validate:
                token = str(RefreshToken.for_user(user))
                access = str(RefreshToken.for_user(user).access_token)
                return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "access": access,
                "refresh": token,
                })
            else:
                content = {"detail": "Password Do not Match"}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
        except:
            content = {"detail": "No active account found with the given credentials"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)




class ProjectCreateApi(generics.GenericAPIView):
    serializer_class = ProjectSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer,"-----dtaa")
        serializer.is_valid(raise_exception=True)
        project = serializer.save()
        return Response({
            "project": UserSerializer(project, context=self.get_serializer_context()).data,
            "message": "Project Created Successfully.",
        })




##------For Project
class ProjectiewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset =Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]



##----------For Project_list
class Projec_listviewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset =Project_list.objects.all()
    serializer_class = Project_listSerializer
    permission_classes = [IsAuthenticated]


##-------------Card
class Card_listviewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class Check_listviewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated]