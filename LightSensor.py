import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Variable to hold the input pin value
pin_to_circuit = 7


def rc_time(pin_to_circuit):
    count = 0

    # Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    # while loop to count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    return count

try:
    while True:
        if (rc_time(pin_to_circuit)) > 10000:
            print("It's Dark")
        elif (rc_time(pin_to_circuit)) < 10000:
            print("It's Light")

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()