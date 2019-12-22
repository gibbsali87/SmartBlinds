import blynklib
import RPi.GPIO as GPIO
import time

BLYNK_AUTH = 'txbM-LjJOrPMp3Beh-Ts1RBYGFMJ3Ahp'

blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

blindPin = 13  # RPI Board pin 13
blindPin1 = 11  # RPI Board pin 11

@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))

    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(blindPin, GPIO.OUT)  # Set blindPin's mode is output
    GPIO.output(blindPin, GPIO.LOW)
    GPIO.setup(blindPin1, GPIO.OUT)  # Set blindPin1's mode is output
    GPIO.output(blindPin1, GPIO.LOW)

    if value == [u'1']:     # check for Virtual piv value
        GPIO.output(blindPin, GPIO.HIGH)
        print("Blind Opened")
        time.sleep(2)
        GPIO.output(blindPin, GPIO.LOW)
        destroy()

    elif value == [u'0']:

        GPIO.output(blindPin1, GPIO.HIGH)
        print("Blinds Closed")
        time.sleep(2)
        GPIO.output(blindPin1, GPIO.LOW)
        destroy()

def destroy():
    GPIO.output(blindPin, GPIO.LOW)
    GPIO.output(blindPin1, GPIO.LOW)
    GPIO.cleanup()


while True:
    blynk.run()

