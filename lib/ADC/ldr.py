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

    def activate(self):
        voltage = self.channel.voltage
        raw_value = self.channel.value
        return f"analog value {raw_value}, Voltage: {voltage:.2f} V"

if __name__ == "__main__":
    ldr_sensor = LDRSensor()

    while True:
        raw_value= ldr_sensor.activate()
        print(raw_value)
