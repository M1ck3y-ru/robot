from machine import Pin, PWM
import time

# Définir les broches pour le contrôle des moteurs
pin_motor_left_forward = Pin(16, Pin.OUT)
pin_motor_left_backward = Pin(17, Pin.OUT)
pin_motor_right_forward = Pin(22, Pin.OUT)
pin_motor_right_backward = Pin(23, Pin.OUT)

# Initialiser les broches pour le contrôle PWM (pour ajuster la vitesse des moteurs)
pwm_motor_left = PWM(Pin(18), freq=5000, duty=0)
pwm_motor_right = PWM(Pin(21), freq=5000, duty=0)


    
    


def avancer(vitesse):
    pwm_motor_left.duty(vitesse) # permet de donner l'impulsion (fréquence)
    pwm_motor_right.duty(vitesse) # permet de donner l'impulsion (fréquence)
    pin_motor_left_forward.on() 
    pin_motor_left_backward.off()
    pin_motor_right_forward.on()
    pin_motor_right_backward.off()

def reculer(vitesse):
    pwm_motor_left.duty(vitesse)
    pwm_motor_right.duty(vitesse)
    pin_motor_left_forward.off()
    pin_motor_left_backward.on()
    pin_motor_right_forward.off()
    pin_motor_right_backward.on()

def tourner_gauche(vitesse):
    
    pwm_motor_left.duty(vitesse)
    pwm_motor_right.duty(vitesse)
    pin_motor_left_forward.off()
    pin_motor_left_backward.on()
    pin_motor_right_forward.on()
    pin_motor_right_backward.off()

def tourner_droite(vitesse):
    
    pwm_motor_left.duty(vitesse)
    pwm_motor_right.duty(vitesse)
    pin_motor_left_forward.on()
    pin_motor_left_backward.off()
    pin_motor_right_forward.off()
    pin_motor_right_backward.on()

def arreter():
    
    pwm_motor_left.duty(0)
    pwm_motor_right.duty(0)
    pin_motor_left_forward.off()
    pin_motor_left_backward.off()
    pin_motor_right_forward.off()
    pin_motor_right_backward.off()