#Importing libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#setting pins
BUZZER = 40
TRIG = 11
ECHO = 7

#setting GPIO direction
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

pwm = GPIO.PWM(BUZZER, 100)
pwm.start(0)

#distance function
def dist():
    
    startT = time.time()
    stopT = time.time()
    
    GPIO.output(TRIG, True) #setting trigger to High
    time.sleep(0.0001) #set the trigger to 0.1ms
    GPIO.output(TRIG, False)
    
    
    while GPIO.input(ECHO) == 0:
        startT = time.time() #start time
        
    while GPIO.input(ECHO) == 1:
        stopT = time.time()

    totTime =stopT - startT #time difference
    
    dist = (totTime * 34300) / 2
    
    return dist

try:
    while True:
        distance = dist()
        
        if (distance <= 50):
            pwm.ChangeFrequency(6 - distance/10)
            pwm.ChangeDutyCycle(50)
            
            time.sleep(0.5)
        else :
            pwm.ChangeDutyCycle(0)
        time.sleep(1)
except KeyboardInterrupt:  
    
    GPIO.cleanup()  
        