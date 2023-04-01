from django.shortcuts import render
import urllib.request
import json
from django.http import Http404

# Create your views here.
def index(request):
    try:
        if request.method =='POST':
            search = request.POST.get('search')
            search_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+search+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
            convert = json.loads(search_url) 

            #Converting fahrenheit  to celcuis 
            fahrenheit = int(convert['main']['temp'])
            celcuis = fahrenheit -273
            feels_like_fahrenheit = int(convert['main']['feels_like'])
            feels_like_celcuis = feels_like_fahrenheit -273

            #Converting mha into bar 
            pressure_hpa = int(convert['main']['pressure'])
            pressure_bar = pressure_hpa/ 1000
            
            #Converting 3 numbers to 1 number decimal | 10.000 into 10.0
            visibility_not_formated = int(convert['visibility']) 
            visibility = visibility_not_formated /1000

            context = {
                'country_code': str(search.capitalize()) + ' ' + str(convert['sys']['country']),
                'longitude':    str(convert['coord']['lon']),
                'latitude':     str(convert['coord']['lat']),
                "clouds":       str(convert['clouds']['all']) ,
                'wind_speed':   str(convert['wind']['speed']),
                'humidity':     str(convert['main']['humidity']) ,
                'temp':         str(celcuis) ,
                "visibility":visibility,
                'feels_like':   str(feels_like_celcuis) ,
                "pressure_bar":pressure_bar,
                "search":search.lower(),
            }
        return render(request,'index.html',context)
    # else:
    except:
        context = {

                 'country_code':" ",
                'longitude':    " ",
                'latitude':     " ",
                "clouds":       " ",
                'wind_speed':   " ",
                'humidity':     " ",
                'temp':         " ",
                'feels_like':   " ",
        }
        search = ''

    return render(request,'index.html',context)