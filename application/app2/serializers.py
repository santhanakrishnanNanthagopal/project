from .models import database
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = database
        fields = '__all__'
