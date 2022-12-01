from django.shortcuts import render
import requests

def index(request):
    appid = '7f0d775f3fa2bd1bb790b2ec36dee211'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    city = 'Rechytsa'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"],
    }
    context = {
        'info': city_info
    }
    return render(request, 'main/index.html',context)

def new(request):

    appid = '7f0d775f3fa2bd1bb790b2ec36dee211'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Minsk'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"],
    }
    context = {
        'info': city_info
    }
    return render(request, 'main/new.html', context)