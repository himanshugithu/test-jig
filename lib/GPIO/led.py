import RPi.GPIO as GPIO
import time

class LEDController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  # Use BCM numbering
        GPIO.setup(self.pin, GPIO.OUT)  # Set the LED pin as an output

    def activate_gui(self): # Calculate the end time
        GPIO.output(self.pin, GPIO.HIGH)  # Turn LED on
        time.sleep(1)  # Delay for 1 second
        GPIO.output(self.pin, GPIO.LOW)  # Turn LED off
        time.sleep(0.5)   # Clean up GPIO settings before exiting

    def activate_cli(self): # Calculate the end time
        GPIO.output(self.pin, GPIO.HIGH)  # Turn LED on
        time.sleep(1)  # Delay for 1 second
        GPIO.output(self.pin, GPIO.LOW)  # Turn LED off
        time.sleep(0.5)   # Clean up GPIO settings before exiting    

if __name__ == "__main__":
    led_controller = LEDController(5)
    while True:
        led_controller.activate_cli()  # Blink an LED on GPIO 5 every 1 second for 10 seconds
        
