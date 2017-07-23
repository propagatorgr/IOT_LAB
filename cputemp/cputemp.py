from gpiozero import CPUTemperature #Εισαγωγή βιβλιοθήκης για τη μέτρηση της θερμοκρασίας της CPU
from time import sleep, strftime, time #Εισαγωγή βιβλιοθήκης χειρισμού χρόνου, συμβολοσειρών
import matplotlib.pyplot as plt #Εισαγωγή βιβλιοθήκης γραφικών απεικονίσεων

plt.ion() #Κάνε την γραφική παράσταση αλληλεπιδραστική
x = []
y = []        
cpu=CPUTemperature()
with open("cpu_temp.csv", "a") as log: #Δημιουργία αρχείου καταγραφών
    while True:
        temp = cpu.temperature #Καταχώρησε την τιμή της θερμοκρασίας στη μεταβλητή temp
        y.append(temp) #Καταχώρησε στις τιμές του άξονα y την τρέχουσα θερμοκρασία
        x.append(time())#Καταχώρησε στις τιμές του άξονα x την τρέχουσα ημερομηνία/ώρα
        plt.clf()
        plt.scatter(x,y)
        plt.plot(x,y)
        plt.draw()
        log.write("{0},{1}\n".format(strftime("%d-%m-%Y %H:%M:%S"),str(temp)))#Γράψε στο αρχείο καταγραφών τα ζεύγη ημερομηνίας/ώρας-θερμοκρασίας
        sleep(1)#Περίμενε 1 δευτερόλεπτο για την επόμενη καταγραφή
        
        

