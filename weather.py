import requests
import json
import pytemperature

api_key = "124a4574e6084fcea7cc82730121f077"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input('Enter a city: ')

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    temp = pytemperature.k2f(current_temperature)
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    print(" Temperature = " +
                    str(temp),"°F" + 
          "\n humidity = " +
                    str(current_humidity), "%" +
          "\n description = " +
                    str(weather_description))
  
else: 
    print(" City Not Found ") 
