from gpiozero import Button, LED
from time import sleep
import random

led = LED(4)

player_1 = Button(15)
name_1=input('Player 1 name is  ')
player_2 = Button(14)
name_2=input('Player 2 name is  ')
names=[name_1,name_2]
def ledon():
    time = random.uniform(2, 7)
    sleep(time)
    led.on()

ledon()
score1=0
score2=0
while True:
    if player_1.is_pressed:
        score1+=1
        print(names[0]+ ' wins! '+names[0]+ ' has '+str(score1)+ ' points.')
        led.off()
        ledon()
    if player_2.is_pressed:
        score2+=1
        print(names[1]+ ' wins! '+names[1]+ ' has '+str(score2)+ ' points.')
        led.off()
        ledon()

    

