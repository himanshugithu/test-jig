import RPi.GPIO as GPIO
import time

class LedFader:
    def __init__(self, pin, frequency=1000):
        self.pin = pin
        self.frequency = frequency
        
        # Set up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
        
        # Set up PWM
        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.pwm.start(0)  # Start PWM with 0% duty cycle (off)

    def fade_in(self, speed=0.02):
        for duty_cycle in range(0, 101, 1):
            self.pwm.ChangeDutyCycle(duty_cycle)
            print(f"duty cycle :{duty_cycle}%")
            time.sleep(speed)

    def fade_out(self, speed=0.02):
        for duty_cycle in range(100, -1, -1):
            self.pwm.ChangeDutyCycle(duty_cycle)
            print(f"duty cycle :{duty_cycle}%")
            time.sleep(speed)

    def activate_gui(self, speed=0.05):
        try:
            while True:
                self.fade_in(speed)
                self.fade_out(speed)
        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup()

    def activate_cli(self, speed=0.05):
        try:
            while True:
                self.fade_in(speed)
                self.fade_out(speed)
        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup()
    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()

# Example usage
if __name__ == "__main__":
    led_pin = 18  # Change this to your desired GPIO pin
    fader = LedFader(led_pin)
    fader.activate()
