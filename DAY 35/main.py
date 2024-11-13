import requests

endpint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "fa0930c2503b4c63f311e2d2e2dbb59c"
lat = 31.905069
lon = 34.813431
response = requests.get(endpint, params={"lat": lat, "lon": lon, "appid": api_key})

forcast_slice = response.json()["list"][:4]
weather = []
will_rain = False
for i in forcast_slice:
    condition_code = i["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
else:
    print("There is no need for an umbrella")
