# Libraries
import RPi.GPIO as GPIO
import time
import os

from LongPress import LongPress


# Pin mapping
LED_PIN = 12
BUTTON_BLACK_PIN = 7
BUTTON_RED_PIN = 16

def black_button_interrupt():
	print("Black button pressed")
	os.system("sudo shutdown -r now")

black_button_longpress = LongPress(BUTTON_BLACK_PIN, black_button_interrupt)

# Pin configuration
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)


# Main code: LED heartbeat
try:
	while True:
		GPIO.output(LED_PIN,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(LED_PIN,GPIO.LOW)
		time.sleep(0.1)
		GPIO.output(LED_PIN,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(LED_PIN,GPIO.LOW)
		time.sleep(2)



# Cleanup if script exits
finally:
        GPIO.cleanup()



