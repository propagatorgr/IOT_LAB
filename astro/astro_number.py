import requests # Εισαγωγή βιβλιοθήκης αιτήσεων
url =” http://api.open-notify.org/astros.json “ # Δηλώνουμε την διεύθυνση άντλησης δεδομένων
r = requests.get(url) # Γίνεται η αίτηση άντλησης δεδομένων
j = r.json() # Δηλώνουμε πως θέλουμε τα δεδομένα σε μορφή JSON
n = j['number'] # Καταχωρούμε τον αριθμό των αστροναυτών στη μεταβλητή n.
print(n) # Τυπώνουμε το περιεχόμενο της μεταβλητής n
