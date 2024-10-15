from rest_framework import serializers

from .models import Api

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ['id','name', 'age']