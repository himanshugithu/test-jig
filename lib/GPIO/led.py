import RPi.GPIO as GPIO
import time

class LEDController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  # Use BCM numbering
        GPIO.setup(self.pin, GPIO.OUT)  # Set the LED pin as an output

    def activate(self, status, interval, duration):
        end_time = time.time() + duration  # Calculate the end time
        gpio_status = GPIO.HIGH if status == "HIGH" else GPIO.LOW
        GPIO.output(self.pin, gpio_status)  # Set LED status
        time.sleep(interval)  # Wait for the specified interval
        GPIO.output(self.pin, not gpio_status)  # Toggle LED status
        time.sleep(interval)  # Wait for the specified interval
        GPIO.cleanup()  # Clean up GPIO settings before exiting

if __name__ == "__main__":
    led_controller = LEDController(5)
    while True:
        led_controller.activate(status="HIGH", interval=1, duration=10)  # Blink an LED on GPIO 5 every 1 second for 10 seconds
        
