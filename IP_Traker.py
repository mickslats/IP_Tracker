import requests
import folium
import time
import webbrowser
import pyttsx3
from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder

## single ip request
# response = requests.get("http://ip-api.com/json/24.48.0.1").json()
#
# print(response['lat'])
# print(response['lon'])

# batch ip request

ipadressrequesr = input("What IP do you wish to trace: ")

response = requests.post("http://ip-api.com/batch", json=[
  {"query": ipadressrequesr},
]).json()

for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")

num1 = input("First number of  the longitude: ")
num2 = input("Secound number of  the longitude: ")
reader = pyttsx3.init()
reader.say("Loading the map")
print("Map is Loading...")
reader.runAndWait()


m = folium.Map(location=[num1, num2], tiles="Stamen Toner", zoom_start=13)

folium.Circle(
    radius=4000,
    location=[num1, num2],
    popup="Here",
    color="blue",
    fill=True,
).add_to(m)


m.save("Map.html")

webbrowser.open("Map.html")
