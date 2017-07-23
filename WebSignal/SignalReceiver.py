import os
import signal
import time
from gpiozero import LED

led=LED(23)

fh=open("processid.txt","w")
fh.write(str(os.getpid())) #get current process id and store in file
fh.close()

def handUSR1(signum,frame):
    print('led is on',signum)
    led.on()
	

def handUSR2(signum,frame):
    print('led is off',signum)
    led.off()

signal.signal(signal.SIGUSR1,handUSR1)
signal.signal(signal.SIGUSR2,handUSR2)

while(True):
    time.sleep(1)
    print("Waiting for signal")
    
