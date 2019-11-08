from django.shortcuts import render , redirect
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
import requests
from .models import City
from .forms import CityForm

# Create your views here.

def WeatherView(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3b340d3098271526ffe2574e950fd570'
    err_msg = ''
    message = ''
    message_class = ''

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CityForm(request.POST)

            if form.is_valid():
                new_city = form.cleaned_data['name']
                existing_city_count = City.objects.filter(name=new_city).count()

                if existing_city_count == 0:
                    r = requests.get(url.format(new_city)).json()
                    if r['cod'] == 200:
                        newsave = City(name=new_city, user=request.user)
                        newsave.save()
                    else:
                        err_msg = 'City does not exist!'
                else:
                    err_msg = "City already exists in the database"
            if err_msg:
                message = err_msg
                message_class = 'is-danger'
            else:
                message = 'City Added Successfully!'
                message_class = 'is-success'
        form = CityForm()

        cities = City.objects.all().filter(user_id=request.user.id)
        weather_data = []
        for city in cities:
            r = requests.get(url.format(city)).json()
            city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)

        context = {
            'weather_data': weather_data,
            'form': form,
            'message': message,
            'message_class': message_class,
        }

        return render(request, 'weather/weather.html', context)
    else:
        return HttpResponseRedirect('/login')

class DeleteView(View):
    def get(self,request,city_name):
        City.objects.get(name=city_name).delete()
        return redirect('/weather')

