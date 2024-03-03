from django.shortcuts import render, HttpResponse
import requests
import datetime
from django.contrib import messages


def home(request):
    if "city" in request.POST:
        city = request.POST["city"]
    else:
        city = "indore"

    # this is the API url from OpenWeatherMap    
    url = " "
    PARAMS = {"units": "metric"} #this parameter is used to get temperature as celcius

    try:
        data = requests.get(url, params=PARAMS).json()
        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        temp = data["main"]["temp"]
        date = datetime.date.today()

        return render(
            request,
            "index.html",
            {
                "description": description,
                "icon": icon,
                "city": city,
                "temp": temp,
                "date": date,
            },
        )
    except KeyError:
        exception_occurred = True
        messages.error(request, "Entered city is not available")
        date = datetime.date.today

        return render(
            request,
            "index.html",
            {
                "description": "clear sky",
                "icon": "01d",
                "temp": 25,
                "date": date,
                "city": "indore",
                "exception_occurred": exception_occurred,
            },
        )


# Create your views here.
