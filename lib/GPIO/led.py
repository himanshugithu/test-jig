import RPi.GPIO as GPIO
import time

class LEDController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  # Use BCM numbering
        GPIO.setup(self.pin, GPIO.OUT)  # Set the LED pin as an output

    def Activate(self, interval, duration):
        end_time = time.time() + duration  # Calculate the end time  
        try:
            while time.time() < end_time:
                GPIO.output(self.pin, GPIO.HIGH)  # Turn LED on
                time.sleep(interval)  # Wait for the specified interval
                GPIO.output(self.pin, GPIO.LOW)  # Turn LED off
                time.sleep(interval)  # Wait for the specified interval
        except KeyboardInterrupt:
            pass  # Exit the loop when Ctrl+C is pressed
        finally:
            GPIO.cleanup()  # Clean up GPIO settings before exiting

if __name__ == "__main__":
    led_controller = LEDController(6)
    led_controller.blink(interval=1, duration=10)  # Blink an LED on GPIO 6 every 1 second for 10 seconds
