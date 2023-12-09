from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
# Create your views here.


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def user_list(request):
    if request.method == 'GET':
        user = AppUser.objects.all()
        serializer = AppUserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def knt_list(request):
    if request.method == 'GET':
        knt = KntKarty.objects.all()
        serializer = KntSerializer(knt, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def wizyty_list(request):
    if request.method == 'GET':
        wiz = Wizyta.objects.all()
        serializer = WizytaSerializer(wiz, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def wizyta(request, pk):
    if request.method == 'GET':
        try:
            wiz = Wizyta.objects.get(pk=pk)
            serializer = WizytaSerializer(wiz, many=False)
            return Response(serializer.data)
        except Wizyta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def knt_insert(request):
    if request.method == 'POST':
        serializer = KntSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def wizyta_insert(request):
    if request.method == 'POST':
        serializer = WizytaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def usr_insert(request):
    if request.method == 'POST':
        serializer = AppUserSerializer(AppUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def knt_update_delete(request, pk):
    try:
        knt = KntKarty.objects.get(pk=pk)
    except KntKarty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        knt = KntKarty.objects.get(pk=pk)
        serializer = KntSerializer(knt, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = KntSerializer(knt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        knt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
