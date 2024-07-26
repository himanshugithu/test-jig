import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins for RGB LED
RED_PIN = 18
GREEN_PIN = 23
BLUE_PIN = 24

# RGB LED Control Class
class RGBLED:
    def __init__(self):
        self.red_pwm = None
        self.green_pwm = None
        self.blue_pwm = None
        
    def init_rgb(self):
        GPIO.setup(RED_PIN, GPIO.OUT)
        GPIO.setup(GREEN_PIN, GPIO.OUT)
        GPIO.setup(BLUE_PIN, GPIO.OUT)
        self.red_pwm = GPIO.PWM(RED_PIN, 100)
        self.green_pwm = GPIO.PWM(GREEN_PIN, 100)
        self.blue_pwm = GPIO.PWM(BLUE_PIN, 100)
        self.red_pwm.start(0)
        self.green_pwm.start(0)
        self.blue_pwm.start(0)
    
    def set_color(self, r, g, b):
        if self.red_pwm and self.green_pwm and self.blue_pwm:
            self.red_pwm.ChangeDutyCycle(r / 255 * 100)
            self.green_pwm.ChangeDutyCycle(g / 255 * 100)
            self.blue_pwm.ChangeDutyCycle(b / 255 * 100)
    
    def turn_off(self):
        self.set_color(0, 0, 0)
    
    def cleanup_rgb(self):
        if self.red_pwm:
            self.red_pwm.stop()
        if self.green_pwm:
            self.green_pwm.stop()
        if self.blue_pwm:
            self.blue_pwm.stop()
        self.red_pwm = None
        self.green_pwm = None
        self.blue_pwm = None
        GPIO.cleanup([RED_PIN, GREEN_PIN, BLUE_PIN])

    def activate_cli(self):
        rgb_led = RGBLED()
        rgb_led.init_rgb()
        try:
            while True:
                try:
                    rgb_led.set_color(255, 0, 0)
                    time.sleep(1)  # Keep the LED on for 5 seconds
                    rgb_led.set_color(0, 255, 0)
                    time.sleep(1)  # Keep the LED on for 5 seconds
                    rgb_led.set_color(0, 0, 255)
                    time.sleep(1)  # Keep the LED on for 5 seconds
                # rgb_led.cleanup_rgb()
                except Exception as e:
                    print("EROOR")
        except KeyboardInterrupt:
            print("Interrupted by user. Exiting...")
        except Exception as e:
            print(f"An error occurred: {e}")

    def activate_gui(self):
        rgb_led = RGBLED()
        rgb_led.init_rgb()
        try:
            rgb_led.set_color(255, 0, 0)
            time.sleep(1)  # Keep the LED on for 5 seconds
            rgb_led.set_color(0, 255, 0)
            time.sleep(1)  # Keep the LED on for 5 seconds
            rgb_led.set_color(0, 0, 255)
            time.sleep(1)  # Keep the LED on for 5 seconds
        # rgb_led.cleanup_rgb()
        except Exception as e:
            print("EROOR")
    

if __name__ == "__main__":
    rgb_led = RGBLED()
    # rgb_led.init_rgb()
    
    # # Turn on RGB LED with specific color (e.g., red)
    # rgb_led.set_color(0, 0, 255)
    # time.sleep(5)  # Keep the LED on for 5 seconds
    
    # # Turn off the RGB LED
    # rgb_led.turn_off()
    
    # # Cleanup GPIO
    # rgb_led.cleanup_rgb()
    rgb_led.activate_cli()