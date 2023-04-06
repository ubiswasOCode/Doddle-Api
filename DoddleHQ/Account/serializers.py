from rest_framework import serializers
from Account.models import User,Project,Project_list,Card,Checklist,List_Table



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


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class Project_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_list
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = "__all__"


class List_TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = List_Table
        fields = "__all__"

