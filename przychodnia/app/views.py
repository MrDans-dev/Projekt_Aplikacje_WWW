from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
# Create your views here.


@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        user = AppUser.objects.all()
        serializer = AppUserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def wizyty_list(request):
    if request.method == 'GET':
        wiz = Wizyta.objects.all()
        serializer = WizytaSerializer(wiz, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def knt_insert(request):
    if request.method == 'POST':
        serializer = KntSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def usr_insert(request):
    if request.method == 'POST':
        serializer = AppUserSerializer(AppUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

