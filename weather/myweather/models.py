from django.db import models

# Create your models here.
# print(json_response['main']['temp'])
# print(json_response['name'])
# print(json_response['weather'][0]['main'])
# print(json_response['weather'][0]['description'])
# print(json_response['weather'][0]['icon'])
#request_for_image = "http://openweathermap.org/img/wn/09d@2x.png"


class Weather(models.Model):
    temperature = models.FloatField(max_length=25)
    nameofcity = models.CharField(max_length=25)
    weather_name = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    icon = models.TextField(max_length=200)

    def __str__(self):
        return self.nameofcity
