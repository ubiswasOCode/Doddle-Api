from django.shortcuts import render
from django.http import HttpResponse
from.models import *
from.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
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


# class CurrentUserView(APIView):
#     def get(self, request):
#         data=User.objects.all().values()
#         serializer = UserShortDetail(data, many=True)
#         return Response(serializer.data)




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


# class SignupAPI(generics.GenericAPIView):
#     serializer_class = SignupSerializer
#     def post(self, request, *args, **kwargs):#,exception):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "status":200,
#         "msg":'Sign Up Successfully'
#         })