from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DemoModel
from .serializers import DemoSerializer

@api_view(['GET'])
def get(req):
    obj = DemoModel.objects.all()
    serializer = DemoSerializer(obj, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add(req):
    serializer = DemoSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
