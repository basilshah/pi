import RPi.GPIO as GPIO
from time import sleepGPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(25, GPIO.OUT)
pwm=GPIO.PWM(25, 50)
pwm.start(0)


def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)
while True:
    x = int(input("enter the angle"))
    SetAngle(x)
    

