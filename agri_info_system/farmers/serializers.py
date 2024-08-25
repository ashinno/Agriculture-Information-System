from rest_framework import serializers
from .models import Farmer, Weather, Crop, MarketPrice, FarmingTip

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class MarketPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPrice
        fields = '__all__'

class FarmingTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmingTip
        fields = '__all__'
