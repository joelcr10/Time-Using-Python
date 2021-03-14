#!/usr/bin/env python3
import time
from playsound import playsound
from datetime import datetime
import sys

t=int(input("Enter timer in seconds: "))
counter = 66600
mp3file = "beep-01a.mp3"
while(t+1):
    tt = datetime.fromtimestamp(counter)
    string = tt.strftime("%H: %M: %S: ")
    sys.stdout.write('\r'+string)
    counter+=1

    t=t-1
    time.sleep(1)
playsound(mp3file)
print("\nTime out")

