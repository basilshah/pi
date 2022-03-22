from gpiozero import Servo
from time import sleep

servo = Servo(25)


print("strt")
servo.min()
sleep(5)
servo.mid()
sleep(0.5)
servo.max()
sleep(0.5)

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
    

