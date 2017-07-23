# My Python Program by ...
import os, time  #Εισαγωγή βιβλιοθηκών

def robot(text):   #εδώ ορίζουμε τη συνάρτηση
      os.system("espeak ' " + text + " ' ")

robot("Hello") #εδώ καλούμε τη συνάρτηση
time.sleep(1)  #παύση 1 δευτερόλεπτο
robot('What is your name?')
name = input('What is your name: ') # Ζητά την ηλικία μας
robot("Nice to meet you " + name)
time.sleep(1)
