# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 19:40:01 2017

@author: Brailas
Δημιουργεί GUI στο οποίο τυπώνονται όλοι οι σταθμοί
και μόλις εισάγεις ID, δεδομένα και χρώμα σου τυπώνει την γραφική παράσταση.
Για να δεις δεδομένα από άλλο σταθμό πρέπει να κλείσεις το 
παράθυρο της πρώτης γραφικής παράστασης.
"""
#Εισάγουμε τις απαραίτητες βιβλιοθήκες
from requests import get
import matplotlib.pyplot as plt
#import sys
from dateutil import parser
from appJar import gui

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


def plotting(time,y,colour,y_label):
    plt.plot(time,y,colour)
    plt.ylabel(y_label)
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
    return (name_id)


def getRecords(id,colour,data):
#url στο οποίο θα αναζητήσουμε δεδομένα
    init_url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/'
    url_finale=init_url+id

#Φέρε τα δεδομένα και αποθήκευσέ τα στη μεταβλητή weather σε json μορφή.
    weather = getWeather(url_finale)


    if (len(weather["items"])==0) :
            app.setMessage("mess","Ο σταθμός είναι εκτός λειτουργίας!!!")
            return
    
#Αποθήκευσε κάθε θερμοκρασία στη λίστα temperatures για κάθε σταθμό
    label=data
    yaxe= [record[data] for record in weather['items']]
    times=[parser.parse(record['reading_timestamp']) for record in weather['items']]
    app.setMessage("mess","Δεδομένα από: "+weather["items"][0]["created_by"]+" Αριθμός εγγραφών: "+str(len(weather["items"])))
    
    plotting(times, yaxe, colour, label)


def gets(btn):
    stathmos=str(app.getEntry("Station ID: "))
    my_colour=app.getOptionBox("Colors")
    data_tograph=app.getOptionBox("Data")
    getRecords(stathmos,my_colour,data_tograph)

#Εδώ ορίζεται το GUI
app=gui()

app.addLabel("l1", "Διαθέσιμοι σταθμοί")
app.setLabelBg("l1", "darkviolet")
text_stations=printAllStations()
app.addHorizontalSeparator(2,0,colour="darkviolet")
app.addScrolledTextArea("t1")
app.setTextArea("t1",text_stations,callFunction=False)
app.addLabel("l2", "Δώσε το ID του σταθμού που θες")
app.setLabelBg("l2", "darkviolet")
app.addLabelEntry("Station ID: ")
app.setFont(20)
app.addLabelOptionBox("Data", ["ambient_temp", "ground_temp",
                        "air_quality", "air_pressure", "humidity", "wind_direction", "wind_speed",
                        "wind_gust_speed", "rainfall"])
app.addLabelOptionBox("Colors", ["blue","green","red","cyan","magenta","yellow","black","lightblue","darkolivegreen","darkblue","crimson","salmon"])
app.addMessage("mess", """Αποτελέσματα
               
               """)
app.setMessageBg("mess","darkviolet")
app.addButton("GET", gets)

app.go()





