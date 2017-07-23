from gpiozero import LED, Button
from time import sleep
from random import uniform
from sys import exit
left_name = input('left player name is ') #Εισάγετε από το πληκτρολόγιο το όνομα του ενός παίκτη.
right_name = input('right player name is ') #Εισάγετε από το πληκτρολόγιο το όνομα του άλλου #παίκτη.

led = LED(4) #Δηλώνεται το Led στο pin 4
right_button = Button(15) #Δηλώνεται το ένα Button στο pin 15
left_button = Button(14) #Δηλώνεται το άλλο Button στο pin 14
led.on()
sleep(uniform(5, 10)) # Επιλέγεται ένας τυχαίος δεκαδικός ανάμεσα στο 5 και στο 10. Τόσα   #δευτερόλεπτα θα είναι αναμμένο το led.
led.off()  #Σβήσε το led
def pressed(button): # Ορίζεται η συνάρτηση που θα τυπώνει στην οθόνη το όνομα του παίκτη που πάτησε το Button και θα τερματίζει.
 
    if button.pin.number == 14: #Αρχή δομής ελέγχου
        print(left_name + ' won the game')
    else:
        print(right_name + ' won the game')
        #Τέλος δομής ελέγχου.
     exit () # Τερμάτισε το πρόγραμμα.
# Τέλος ορισμού συνάρτησης.
right_button.when_pressed = pressed  #Όταν πατηθεί το ένα Button καλείται η συνάρτηση.
left_button.when_pressed = pressed    #Όταν πατηθεί το άλλο Button καλείται η συνάρτηση.
