from django.shortcuts import render


from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework.serializers import Serializer
from .models import Communicatewithpeople, Diary, Drugnotification, Game, Location, User
from .serializers import CommunicatewithpeopleSerializer, DiarySerializer, DrugnotificationSerializer, GameSerializer, LocationSerializer, UserCreateSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.

# 데코레이터를 사용해서 리팩토링 사용


class CommunicatewithpeopleViewSet(viewsets.ModelViewSet):
    queryset = Communicatewithpeople.objects.all()
    serializer_class = CommunicatewithpeopleSerializer


class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class DrugnotificationViewSet(viewsets.ModelViewSet):
    queryset = Drugnotification.objects.all()
    serializer_class = DrugnotificationSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    @csrf_exempt
    @api_view(['POST'])
    @permission_classes([])
    def signup(request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()  # DB 저장
            return Response(serializer.data, status=201)


@csrf_exempt
@api_view(['POST'])
@permission_classes([])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":  # email required
            return Response({'message': 'fail'}, status=status.HTTP_202_ACCEPTED)

        response = {
            'success': True,
            'token': serializer.data['token']  # 시리얼라이저에서 받은 토큰 전달
        }

        return Response(response, status=status.HTTP_200_OK)
