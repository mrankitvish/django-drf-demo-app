# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import DemoModel
 
# Create a model serializer
class DemoSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = DemoModel
        fields = '__all__'