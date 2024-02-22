from machine import Pin, PWM
import machine
import time

trig_pin = Pin(4, Pin.OUT)
echo_pin = Pin(5, Pin.IN)

# Vitesse du son dans l'air
SOUND_SPEED = 340
TRIG_PULSE_DURATION_US = 10

ultrason_duration = 0
distance_cm = 0

motor1_in1 = Pin(16, Pin.OUT)
motor1_in2 = Pin(17, Pin.OUT)
motor2_in1 = Pin(19, Pin.OUT)
motor2_in2 = Pin(21, Pin.OUT)

motor1_pwm = PWM(Pin(22))
motor2_pwm = PWM(Pin(23))

def setup():
    global motor1_pwm, motor2_pwm
    motor1_pwm.freq(1000)
    motor2_pwm.freq(1000)
    motor1_pwm.duty(0)
    motor2_pwm.duty(0)

def move_forward():
    motor1_in1.on()
    motor1_in2.off()
    motor2_in1.on()
    motor2_in2.off()
    motor1_pwm.duty(1023)
    motor2_pwm.duty(1023)

def move_backward():
    motor1_in1.off()
    motor1_in2.on()
    motor2_in1.off()
    motor2_in2.on()
    motor1_pwm.duty(1023)
    motor2_pwm.duty(1023)

def stop_motors():
    motor1_pwm.duty(0)
    motor2_pwm.duty(0)

def loop():
    global ultrason_duration, distance_cm
    while True:
        # Préparation du signal
        print("préparation du siginal")
        trig_pin.off()
        time.sleep_us(2)
        # Création d'une impulsion de 10 µs
        trig_pin.on()
        time.sleep_us(TRIG_PULSE_DURATION_US)
        trig_pin.off()
        print("impulsion crée")

        # Mesure de la durée de propagation de l'onde (en µs)
        ultrason_duration = machine.time_pulse_us(echo_pin, 1)
        print("impulsion en cours")

        # Calcul de la distance
        distance_cm = ultrason_duration * SOUND_SPEED / 2 * 0.0001

        # Affichage de la distance
        print("Distance (cm):", distance_cm)

        # Contrôle des moteurs en fonction de la distance
        if distance_cm < 10:  # Si la distance est inférieure à 10 cm
            stop_motors()
        else:
            move_forward()

        time.sleep(1)  # Attendre 1 seconde avant la prochaine mesure
#