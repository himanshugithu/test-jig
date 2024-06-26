import RPi.GPIO as GPIO
import time

# Set up the GPIO pin for the PIR sensor
PIR_PIN = 17  # GPIO pin 17

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print("PIR Sensor is warming up...")
    time.sleep(2)  # Give the sensor some time to calibrate

    print("Ready")

    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
        else:
            print("No Motion")
        time.sleep(1)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
