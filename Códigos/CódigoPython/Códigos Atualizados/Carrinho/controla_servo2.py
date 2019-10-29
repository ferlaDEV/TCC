import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 50)

p.start(7.5)

try:
        while True:
                p.ChangeDutyCycle(7.5)
                time.sleep(0.05)
                p.ChangeDutyCycle(12.5)
                time.sleep(1)
                p.ChangeDutyCycle(2.5)
                time.sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()