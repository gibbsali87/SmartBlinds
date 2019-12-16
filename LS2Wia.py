import RPi.GPIO as GPIO
import time

from wia import Wia

wia = Wia()
wia.access_token = "d_sk_fm6TFc3vluFMTpA21MzJncs9"

GPIO.setmode(GPIO.BOARD)

# Variable to hold the input pin value
pin_to_circuit = 7

def rc_time(pin_to_circuit):
    count = 0

    # Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(10.0)

    # Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    # while loop to count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    return count

try:
    while True:
        if (rc_time(pin_to_circuit)) > 10000:
            action = "Blinds Closed"
            wia.Event.publish(name="Action", data=action)
        elif (rc_time(pin_to_circuit)) < 10000:
            action = "Blinds Opened"
            wia.Event.publish(name="Action", data=action)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
