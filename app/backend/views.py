from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import DemoModel
from api.serializers import DemoSerializer

# Create your views here.
def home(req):
    return render(req,'index.html')

