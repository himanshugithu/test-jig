import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

class LDRSensor:
    def __init__(self):
        # Initialize I2C bus and ADS1115 ADC
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        # Create single-ended input on channel 0
        self.channel = AnalogIn(self.ads, ADS.P0)

    def activate_gui(self):
        voltage = self.channel.voltage
        raw_value = self.channel.value
        return f"analog value {raw_value}, Voltage: {voltage:.2f} V"
    
    
    def activate_cli(self):
        try:
            while True:
                voltage = self.channel.voltage
                raw_value = self.channel.value
                print(f"analog value {raw_value}, Voltage: {voltage:.2f} V")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Interrupted by user. Exiting...")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    ldr_sensor = LDRSensor()
    while True:
        # raw_value= ldr_sensor.activate()
        print(ldr_sensor.activate_cli())
