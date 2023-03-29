from rest_framework import serializers
from Account.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password', 'last_name','first_name','phone_no')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],
                                        password = validated_data['password'],
                                        first_name = validated_data['first_name'],
                                        phone_no=validated_data['phone_no'],
                                        last_name=validated_data['last_name'],
                                    )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)


# from rest_framework import serializers
# from django.contrib.auth.models import User
# from rest_framework.exceptions import APIException
# from rest_framework import status
# from django.utils.encoding import force_str
# class CustomValidation(APIException):
#     status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#     default_detail = 'A server error occurred.'
#     def __init__(self, detail, field, detail2,field2,status_code):
#         if status_code is not None:self.status_code = status_code
#         if detail is not None:
#             self.detail = {field: force_str(detail),field2: int(force_str(detail2))}
#         else: self.detail = {'detail': force_str(self.default_detail)}
# class SignupSerializer(serializers.ModelSerializer):
#     def validate(self, value):
#         if User.objects.filter(email=value['email']):
#             raise CustomValidation('Email already exists.','msg',400,'status', status_code=status.HTTP_200_OK)
#         return value
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'password')
#         extra_kwargs = {'password':{'write_only':True}}
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['email'], validated_data['email'], validated_data['password'])
#         return user