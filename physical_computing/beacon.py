from gpiozero import LED # Εισαγωγή βιβλιοθήκης ελέγχου Led
 from time import sleep # Εισαγωγή βιβλιοθήκης χρονοδιακόπτη
    
 led = LED(17) # Δηλώνει το Led στο pin 17
    
 while True: # Ξεκινά μια δομή επανάληψης που δεν τελειώνει ποτέ.
     led.on() # Άναψε 
     sleep(1) # Αναμονή ενός δευτερολέπτου
     led.off() # Σβήσε 
     sleep(1) # Αναμονή ενός δευτερολέπτου