import time
import RPi.GPIO as GPIO


class LongPress:

    min_press_time = 0.5
    was_pressed = False
    press_time = time.time()


    def interrupt_routine(self, channel):


        currently_pressed = not GPIO.input(self.pin)

        if(not currently_pressed == self.was_pressed):

            if currently_pressed:
                self.press_time = time.time()

            else:
                release_time = time.time()
                pressed_time = release_time - self.press_time

                if pressed_time > self.min_press_time:
                    self.callback()

        self.was_pressed = currently_pressed


    def __init__(self, pin, callback):

        self.pin = pin
        self.callback = callback

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.interrupt_routine)
