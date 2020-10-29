import requests
import datetime
from math import sin, cos, atan2, sqrt, radians

URL="https://www.folktandvardenstockholm.se/api/booking/lastminute?timeTypeId=7Adult"
r = requests.get(url=URL)
data=r.json()


# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
def GPSDist(coord1, coord2):
    earth_radius = 6373.0
    lon1 = radians(coord1[0])
    lat1 = radians(coord1[1])
    lon2 = radians(coord2[0])
    lat2 = radians(coord2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = earth_radius * c
    return distance

mycoords = (18.071518, 59.314501) # long, lat

for i, slot in enumerate(data["timeSlots"]):
    i += 1
    print(f"## Option {i} ##")
    # time
    start = slot["startTime"]
    start = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    end = slot["endTime"]
    end = datetime.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")
    duration = end - start
    print("Start:", start)
    print("End:", end)
    print("Duration:", duration)
    # place   
    print("Location:", slot["clinicName"])
    coords = (float(slot["longitude"]), float(slot["latitude"])) # long, lat
    print("Distance:", int(GPSDist(mycoords, coords)), "km")
    # price
    print("Price:", slot["price"])

