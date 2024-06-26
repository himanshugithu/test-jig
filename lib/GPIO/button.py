import RPi.GPIO as GPIO
import time

class ButtonController:
    def __init__(self, button_pin):
        self.button_pin = button_pin
        self.setup_button()

    def setup_button(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def button_pressed(self):
        input_state = GPIO.input(self.button_pin)
        return input_state == False

    def Activate(self):
        try:
            while True:
                if self.button_pressed():
                    print('Button Pressed')
                    # Your additional code here
                    time.sleep(0.2)  # debounce delay
        
        except KeyboardInterrupt:
            print("\nExiting program")
        
        finally:
            GPIO.cleanup()

if __name__ == '__main__':
    button_controller = ButtonController(button_pin=5)
    button_controller.Activate()
