from django.shortcuts import render
from .models import Weather
import requests


# print(json_response['main']['temp'])
# print(json_response['name'])
# print(json_response['weather'][0]['main'])
# print(json_response['weather'][0]['description'])
# print(json_response['weather'][0]['icon'])


def home(request):
    request_for_data = "http://api.openweathermap.org/data/2.5/weather?q=New%20Delhi&appid=976535ec83c4aba2eae773b96f0c6986&units=metric"
    response = requests.get(request_for_data)
    note = 'No detail'
    if response.status_code == 200:
        print('Success')
        json_response = response.json()
        weather = Weather()
        weather.temperature = json_response['main']['temp']
        weather.nameofcity = json_response['name']
        weather.weather_name = json_response['weather'][0]['main']
        weather.description = json_response['weather'][0]['description']
        weather.icon = 'http://openweathermap.org/img/wn/' + \
            json_response['weather'][0]['icon'] + '@2x.png'
        weather.save()
        return render(request, 'home.html', {"weather": weather})

    else:
        note = 'Not found'
        print('Not Found.')
        return render(request, 'home.html', {'note': note})
