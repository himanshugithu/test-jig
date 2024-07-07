import RPi.GPIO as GPIO
import time
import sys

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
    
    def wheel(self, pos):
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)
    
    def rainbow_cycle(self, wait):
        try:
            while True:
                for j in range(256):
                    for i in range(256):
                        color = self.wheel((i + j) & 255)
                        self.set_color(*color)
                        time.sleep(wait)
        except KeyboardInterrupt:
            print("Interrupted by user")
            return 1
        return 0
    
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

    def activate(self, duration=10):
            try:
                start_time = time.time()
                while time.time() - start_time < duration:
                    self.init_rgb()
                    self.rainbow_cycle(0.01)  # Adjust the delay to control the speed
                    self.cleanup_rgb()
                    time.sleep(0.5)  # Add a short delay between iterations if needed
            except KeyboardInterrupt:
                print("\nMeasurement stopped by User")
            finally:
                self.cleanup_rgb()


if __name__ == "__main__":
    rgb_led = RGBLED() 
    # rgb_led.init_rgb()
    # rgb_led.rainbow_cycle(0.01)  # Adjust the delay to control the speed
    # rgb_led.cleanup_rgb()       

    rgb_led.activate()