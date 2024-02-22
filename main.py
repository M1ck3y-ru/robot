#NILS JAUDON
#MEHDI FANDI
#CLEMENT GARCIA

import time
import engine
from machine import Pin, PWM

    
while True:
    engine.avancer(700) # allow you to move forward
    time.sleep_ms(500) #keep executing the command for 5 ms
    engine.tourner_droite(700) #allow you to turn right 
    time.sleep_ms(500) #keep executing the command for 5 ms
    engine.reculer(700) #allow you to turn backward 
    time.sleep_ms(700) #keep executing the command for 5 ms
    engine.arreter() #allow you to stop 
    time.sleep_ms(700) #keep executing the command for 5 ms
  
    
    
