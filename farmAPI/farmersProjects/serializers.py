from rest_framework import serializers
from .models import Projects,Booking

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields ='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
