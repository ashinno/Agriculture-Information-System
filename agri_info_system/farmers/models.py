from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Weather(models.Model):
    region = models.CharField(max_length=100)
    date = models.DateField()
    temperature = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.region} - {self.date}"

class Crop(models.Model):
    name = models.CharField(max_length=100)
    growing_season = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class MarketPrice(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.crop.name} - {self.region} - {self.date}"

class FarmingTip(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
