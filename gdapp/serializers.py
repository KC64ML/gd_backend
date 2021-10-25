from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.settings import api_settings
from .models import Communicatewithpeople, Diary, Drugnotification, Game, Location, User
# JWT 사용을 위한 설정


class CommunicatewithpeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Communicatewithpeople
        fields = ['chattinghistory']


class DiarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diary
        fields = ['password', 'date', 'contents']


class DrugnotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drugnotification
        fields = ['approximately_time_remaining',
                  'drug_name']


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['gamerecord']


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['rarea', 'locationcol']



Userset = get_user_model()

class UserCreateSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'phonenumber',
                  'email', 'familyname', 'age', 'dateofonesbirth']

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    phonenumber = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    familyname = serializers.CharField(required=True)
    age = serializers.CharField(required=True)
    dateofonesbirth = serializers.CharField(required=True)

    def create(self, validated_data):
        # 저장시 한 번 더 확인
        user = Userset.objects.create(
            username=validated_data['username'],
            phonenumber=validated_data['phonenumber'],
            email=validated_data['email'],
            familyname=validated_data['familyname'],
            age=validated_data['age'],
            dateofonesbirth=validated_data['dateofonesbirth'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            return {
                'email': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload).decode('utf-8')  # 토큰 발행
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }
