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

