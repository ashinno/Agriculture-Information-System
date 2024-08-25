from django.contrib import admin
from .models import Farmer, Weather, Crop, MarketPrice, FarmingTip
# Register your models here.
admin.site.register(Farmer)
admin.site.register(Weather)
admin.site.register(Crop)
admin.site.register(MarketPrice)
admin.site.register(FarmingTip)
