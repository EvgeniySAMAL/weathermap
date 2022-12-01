from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '7f0d775f3fa2bd1bb790b2ec36dee211'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    if request.method =='POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()

    all_cityes =[]
    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }
        print(res)
        all_cityes.append(city_info)
    context = {
        'all_info': all_cityes,
        'form':form
        }

    return render(request, 'main/index.html',context,)

def new(request):

    appid = '7f0d775f3fa2bd1bb790b2ec36dee211'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()

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