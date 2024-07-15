from w1thermsensor import W1ThermSensor
import os
import time
import RPi.GPIO as GPIO

class TemperatureSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.sensor_id = self.detect_sensor_id()
        if self.sensor_id:
            self.sensor = W1ThermSensor(sensor_id=self.sensor_id)
        else:
            raise Exception("No DS18B20 sensor found.")

    def detect_sensor_id(self):
        try:
            base_dir = '/sys/bus/w1/devices/'
            sensor_folder = glob(base_dir + '28*')[0]
            return os.path.basename(sensor_folder)
        except IndexError:
            return None

    def read_temperature(self):
        temperature = self.sensor.get_temperature()
        return temperature

if __name__ == "__main__":
    try:
        temp_sensor = TemperatureSensor()
        
        while True:
            temperature = temp_sensor.read_temperature()
            print(f"Temperature: {temperature:.2f} °C")
            time.sleep(1)
    
    except Exception as e:
        print(f"Error: {str(e)}")
