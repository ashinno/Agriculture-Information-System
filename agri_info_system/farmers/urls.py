from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmerViewSet, WeatherViewSet, CropViewSet, MarketPriceViewSet, FarmingTipViewSet, weather_view

router = DefaultRouter()
router.register(r'farmers', FarmerViewSet)
router.register(r'weather', WeatherViewSet)
router.register(r'crops', CropViewSet)
router.register(r'market-prices', MarketPriceViewSet)
router.register(r'farming-tips', FarmingTipViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/weather/<str:region>/', weather_view, name='weather'),
]