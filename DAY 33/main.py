import requests
from datetime import datetime
import time

MY_LAT = 31.905070
MY_LNG = 34.813430


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (
        MY_LNG - 5 <= iss_longitude <= MY_LNG + 5
    ):
        return True


def currently_night():
    response = requests.get(
        url=f"http://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0"
    )
    response.raise_for_status()
    data = response.json()
    sunrise_hr = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunrise_min = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
    sunset_hr = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunset_min = int(data["results"]["sunset"].split("T")[1].split(":")[1])

    now_hr = datetime.now().hour
    now_min = datetime.now().minute

    if (
        (sunset_hr < now_hr < sunrise_hr)
        or ((now_hr == sunset_hr) and (now_min > sunset_min))
        or ((now_min == sunrise_min) and (now_min < sunrise_min))
    ):
        return True


while True:
    if currently_night() and iss_overhead():
        print("Look Up!")
    else:
        print("No luck!")
    time.sleep(60)
