# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:02:41 2017

@author: sakis
"""

from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

def getData(id):
    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/'
    url_finale=url+id
    weather = get(url_finale).json()
    data = weather['items']
    pages = 1
    print('Fetching {0}'.format(url_finale))
    print(len(data))
    while 'next' in weather and pages < 9:    
          url_finale = weather['next']['$ref']
          print('Fetching {0}'.format(url_finale))
          weather = get(url_finale).json()
          data += weather['items']
          print(len(data))
          pages += 1

    temps = [record['ambient_temp'] for record in data]
    times = [parser.parse(record['reading_timestamp']) for record in data]
    return times,temps


for n in range(2):
    
    stathmos_id=input("Δώσε το id του σταθμού που θες: ")
    color=input("Δώσε χρώμα για την γραφική παράσταση: ")
    
    timestamps, temperatures= getData(stathmos_id)
    plt.plot(timestamps, temperatures,color)
    
   
plt.ylabel('Temperature')
plt.xlabel('date and time')
plt.show()




