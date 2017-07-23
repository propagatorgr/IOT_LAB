# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 19:40:01 2017

@author: sakis
"""
#Εισάγουμε τις απαραίτητες βιβλιοθήκες
from requests import get
import matplotlib.pyplot as plt
#import sys
from dateutil import parser


#Συνάρτηση που δημιουργεί dictionary από 2 λίστες
def create_dict(a, b):
    d = dict()
    if len(a)-len(b) != 0:
        for i in range(len(a)-len(b)):
            b.append(None)
    for j in range(len(a)):
        d[a[j]] = b[j]
    return d

def getWeather(url):
    weather=get(url).json()
    return weather

def plotting(time,temp,colour):
    plt.plot(time,temp,colour)
    plt.ylabel('Θερμοκρασία')
    plt.xlabel('Χρόνος')
    plt.show()
    
    
    
def printAllStations():
#Η διεύθυνση από την οποία θα αναζητήσουμε όλους τους σταθμούς
    stations="https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations"

#Φέρε τους σταθμούς
    allstations=get(stations).json()
#Λίστα με τα ονόματα των σταθμών
    names=[record['weather_stn_name'] for record in allstations['items']]
#Λίστα με τα ids των σταθμών
    ids=[record['weather_stn_id'] for record in allstations['items']]
#Κλήση της συνάρτησης συνένωσης των δύο λιστών σε ένα dictionary
    name_id=create_dict(names,ids)
#Τύπωσε τα ονόματα και τους σταθμούς
    print ("Οι σταθμοί από τους οποίους μπορείς να πάρεις δεδομένα είναι: "+str(len(names)))
    print(name_id)


def getRecords(id,colour):
    

#url στο οποίο θα αναζητήσουμε δεδομένα
    init_url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/'
    url_finale=init_url+id

#Φέρε τα δεδομένα και αποθήκευσέ τα στη μεταβλητή weather σε json μορφή.
    weather = getWeather(url_finale)


    if (len(weather["items"])==0) :
            print("Ο σταθμός είναι εκτός λειτουργίας!!!")
            return
    
#Αποθήκευσε κάθε θερμοκρασία στη λίστα temperatures για κάθε σταθμό
    tempes= [record['ambient_temp'] for record in weather['items']]
    times=[parser.parse(record['reading_timestamp']) for record in weather['items']]
    print("Δεδομένα από: "+weather["items"][0]["created_by"])
    print("Αριθμός εγγραφών: "+str(len(weather["items"])))
    plotting(times, tempes, colour)


answer=input("Θες να τυπώσω όλους τους σταθμούς? (y/n)")
if (answer=='y' or answer=='Y'):
    printAllStations()
else:
    print("Συνεχίζω χωρίς να τυπώσω.")
    
number=input("Από πόσους σταθμούς θες δεδομένα? ")    
for i in range (int(number)):
   stathmos=input("Δώσε το id του  σταθμού που θες: ")
   my_colour=input("Δώσε χρώμα για την γραφική παράσταση: ")
   getRecords(stathmos,my_colour)
   




