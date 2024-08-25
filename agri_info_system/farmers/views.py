from rest_framework import viewsets
from .models import Farmer, Weather, Crop, MarketPrice, FarmingTip
from .serializers import FarmerSerializer, WeatherSerializer, CropSerializer, MarketPriceSerializer, FarmingTipSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import get_weather_data

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class MarketPriceViewSet(viewsets.ModelViewSet):
    queryset = MarketPrice.objects.all()
    serializer_class = MarketPriceSerializer

class FarmingTipViewSet(viewsets.ModelViewSet):
    queryset = FarmingTip.objects.all()
    serializer_class = FarmingTipSerializer


@api_view(['GET'])
def weather_view(request, region):
    data = get_weather_data(region)
    if data:
        return Response(data)
    else:
        return Response({'error': 'Could not retrieve weather data'}, status=400)
