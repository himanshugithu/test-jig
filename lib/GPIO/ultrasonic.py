import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.setwarnings(False)
    
    def measure_distance(self, timeout=1.0):
        # Ensure the trigger pin is set low initially
        GPIO.output(self.trigger_pin, GPIO.LOW)
        time.sleep(2)  # Allow sensor to settle
        
        # Send a 10us pulse to the trigger pin
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)  # 10 microseconds
        GPIO.output(self.trigger_pin, GPIO.LOW)
        
        # Wait for the echo pin to go high and record the start time
        start_time = time.time()
        while GPIO.input(self.echo_pin) == GPIO.LOW:
            start_time = time.time()
        
        # Wait for the echo pin to go low and record the end time
        end_time = time.time()
        while GPIO.input(self.echo_pin) == GPIO.HIGH:
            end_time = time.time()
            if end_time - start_time > timeout:
                print("Timeout")
                return None  # Timeout occurred
        
        # Calculate the distance based on the duration of the echo pulse
        duration = end_time - start_time
        distance = (duration * 34300) / 2  # Speed of sound is 34300 cm/s
        
        return distance
    
    def cleanup(self):
        GPIO.cleanup()

    def activate_gui(self):
        try:
            while True:
                distance = self.measure_distance()
                if distance is not None:
                    return(f"Distance: {distance:.2f} cm")
                else:
                    return("Failed to measure distance")
                time.sleep(0.3)  # Wait for 0.3 seconds before the next measurement
        except KeyboardInterrupt:
            print("\nMeasurement stopped by User")
        finally:
            self.cleanup()

    def activate_cli(self):
        try:
            while True:
                distance = self.measure_distance()
                if distance is not None:
                    print(f"Distance: {distance:.2f} cm")
                else:
                    print("Failed to measure distance")
                time.sleep(0.3)  # Wait for 0.3 seconds before the next measurement
        except KeyboardInterrupt:
            print("\nMeasurement stopped by User")
        finally:
            self.cleanup()            

if __name__ == "__main__":
    sensor = UltrasonicSensor(trigger_pin=26, echo_pin=19)
    print(sensor.activate())
