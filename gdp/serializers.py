from rest_framework import serializers
from .models import Gdp
class GdpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gdp
        fields = '__all__'

