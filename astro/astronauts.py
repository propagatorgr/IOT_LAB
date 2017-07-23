import requests
from gpiozero import LED
from time import sleep
while True:
   url = "http://api.open-notify.org/astros.json"
   r = requests.get(url)
   j = r.json()
   n = j['number'] # Ο αριθμός των αστροναυτών.
   astronauts = j['people'] #Λίστα με τα ονόματα των αστροναυτών
   pins = [2, 3, 4, 14, 15, 17, 18, 27, 22, 23] # Δηλώνουμε τα pins των Led σε μια λίστα.
   leds = [LED(pin) for pin in pins] # Αντιστοιχούμε σε κάθε pin από ένα led.
   for i, led in enumerate(leds):#Διαδικασία επανάληψης που ανάβει τόσα led όσοι είναι οι αστροναύτες
       if n > i:
          led.on()
          print(astronauts[i]['name'])
          sleep(1)
      else:
          led.off()
   # Τέλος διαδικασίας επανάληψης
   sleep(60) # Περίμενε ένα λεπτό μέχρι να ξαναρχίσεις τη διαδικασία
