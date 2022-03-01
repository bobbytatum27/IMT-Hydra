import time as time
import signal
import sys
import RPi.GPIO as GPIO
BUTTON_GPIO = 16

# 1PPS Exploratory Code

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_pressed_callback(channel):
    print("Gpio 16 rising edge detected at %.8f" % time.time())

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, callback=button_pressed_callback)
    signal.signal(signal.SIGINT, signal_handler)
    i = 0
    while True:
        i += 1
        if i % 997 == 0:
            print("alksjdgl;jasldgjkaskljgdklsjgd")
