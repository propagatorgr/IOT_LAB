#Εισάγουμε τις απαραίτητες βιβλιοθήκες
from requests import get
import matplotlib.pyplot as plt
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

stathmos=input("Δώσε το id του σταθμού που θες: ")
#url στο οποίο θα αναζητήσουμε δεδομένα
init_url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/'
url=init_url+stathmos
#Φέρε τα δεδομένα και αποθήκευσέ τα στη μεταβλητή weather σε json μορφή.
weather = get(url).json()
if len(weather["items"])==0:
    print("Ο σταθμός είναι εκτός λειτουργίας!!!")
    quit
#Τύπωσε το όνομα του σταθμού
print("Δεδομένα από: "+weather["items"][0]["created_by"])
#Αποθήκευσε κάθε θερμοκρασία στη λίστα temperatures
temperatures = [record['ambient_temp'] for record in weather['items']]
#Αποθήκευσε κάθε ημερομηνία στη λίστα timestamps
#αφού πρώτα τη φέρεις σε μορφή που θα μπορεί να διαβάσει η Python
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]
#Εκτύπωσε το διάγραμμα
plt.plot(timestamps, temperatures)
## Τύπωσε ετικέτα για κάθε άξονα
plt.ylabel('Θερμοκρασία')
plt.xlabel('Χρόνος')
plt.show()
