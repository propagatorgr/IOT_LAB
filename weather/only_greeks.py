# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:24:04 2017

@author: sakis
"""

from requests import get
import json
import folium
import os
import webbrowser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

all_stations = get(url).json()['items']
total_stations=len(all_stations)
greek_stations=[]

for station in all_stations:
    max_lat=41.739
    min_lat=34.800
    max_lon=28.247
    min_lon=19.128
    if (min_lat<station['weather_stn_lat']<max_lat):
        if (min_lon<station['weather_stn_long']<max_lon):
            greek_stations.append(station)
            
            
print ("Οι Ελληνικοί σταθμοί είναι: "+str(len(greek_stations))+" σε σύνολο "+str(total_stations))

map_ws = folium.Map(location=[37.983, 23.731], zoom_start=6)
CWD = os.getcwd()
for n in range(len(greek_stations)):
    folium.Marker([greek_stations[n]["weather_stn_lat"],
                greek_stations[n]["weather_stn_long"]],
                popup = greek_stations[n]["weather_stn_name"] +" id: "+str(greek_stations[n]["weather_stn_id"])).add_to(map_ws) 
map_ws.save('wsmap1.html')
webbrowser.open_new('file://'+CWD+'/'+'wsmap1.html')

           

