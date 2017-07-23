# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:30:14 2017
Παρακολουθεί τα tweets του χρήστη @propagatorgr και ανάβει led
σε μια συγκεκριμένη φράση. 
@author: sakis
"""
from gpiozero import LED
from time import sleep
led = LED(17)
from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
         if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            if tweet=='stella':
              print("@%s: %s" % (username, tweet))
              led.on()
              sleep(3)
              led.off()
              self.disconnect()
    
    def on_error(self, status_code, data):
         print (status_code)
         self.disconnect()
        
stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
userID='420532725'
stream.statuses.filter(follow=userID)
