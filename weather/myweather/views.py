from django.shortcuts import render,redirect
from .models import Weather
from .forms import CityForm
import requests
from django.http import HttpResponse


# print(json_response['main']['temp'])
# print(json_response['name'])
# print(json_response['weather'][0]['main'])
# print(json_response['weather'][0]['description'])
# print(json_response['weather'][0]['icon'])


def home(request):
    weather_list = []
    city = CityForm()
    if request.method == 'POST':
        city = CityForm(request.POST)
        if city.is_valid():
            request_for_data = "http://api.openweathermap.org/data/2.5/weather?q="+ \
            city.cleaned_data['cityname'] \
            +"&appid=976535ec83c4aba2eae773b96f0c6986&units=metric"
            response = requests.get(request_for_data)
            if response.status_code == 200:
                print('Success')
                json_response = response.json()
                try:
                    weather = Weather.objects.get(nameofcity=json_response['name'])
                    print("Cityalreadypresent")
                    weather_list = Weather.objects.all()
                    city = CityForm()
                    msg = 'City already exists'
                    msgcls = 'alert-dark'
                    return render(request, 'home.html', {"weather_list": weather_list,'city':city ,'msg':msg,'msgcls':msgcls})
                except Weather.DoesNotExist:
                    weather = Weather()
                    weather.temperature = json_response['main']['temp']
                    weather.nameofcity = json_response['name']
                    weather.weather_name = json_response['weather'][0]['main']
                    weather.description = json_response['weather'][0]['description']
                    weather.icon = 'http://openweathermap.org/img/wn/' + \
                        json_response['weather'][0]['icon'] + '@2x.png'
                    weather.save()
                    print("Newcitysaved")
                    weather_list = Weather.objects.all()
                    city = CityForm()
                    msg = 'New city added'
                    msgcls = 'alert-light'
                    return render(request, 'home.html', {"weather_list": weather_list,'city':city ,'msg':msg,'msgcls':msgcls})
             #else1
            else:
                return HttpResponse("City Not found.")

      
        #else2
        else:
            return HttpResponse("City Not found.")
    #else3
    else:
        weather_list = Weather.objects.all()
        return render(request, 'home.html', {"weather_list": weather_list,'city':city })

def delete(request,cityname):
    Weather.objects.get(nameofcity=cityname).delete()
    return redirect("home")   
   