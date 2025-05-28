from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Avenger
from . serializers import AvengerSerializer
# Create your views here.

@api_view(['GET','POST'])
def avenger(request):
    '''Hi avengers'''               # This will include in description part
    if request.method == 'GET':
        
        avenger= Avenger.objects.all()
        serializer = AvengerSerializer(avenger,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AvengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def avenger_update(request,pk):
    try:
        avenger = Avenger.objects.get(pk=pk)
    except Avenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = AvengerSerializer(avenger)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AvengerSerializer(avenger,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        avenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)