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

# Turn led ON
GPIO.output(LED_PIN,GPIO.HIGH)



# Main code: Nothing
try:
	while True:
		time.sleep(60)


# Cleanup if script exits
finally:
        GPIO.cleanup()



