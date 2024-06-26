import RPi.GPIO as GPIO
import adafruit_dht
import board

class DHTSensor:
    def __init__(self, pin):
        self.pin = pin
        self.dht_device = adafruit_dht.DHT11(self.pin, use_pulseio=False)

    def Activate(self):
        try:
            temperature = self.dht_device.temperature
            humidity = self.dht_device.humidity
            if humidity is not None and temperature is not None:
                print(f'Temperature: {temperature:.1f}°C\nHumidity: {humidity:.1f}%')
            else:
                print('Failed to get reading. Try again!')
        except RuntimeError as error:
            print(error.args[0])
            print('Failed to get reading. Try again!')

    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        sensor = DHTSensor(pin=board.D13)
        sensor.Activate()
    except KeyboardInterrupt:
        print("\nExiting program")
    finally:
        sensor.cleanup()
