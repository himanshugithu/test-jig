import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class Pot:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
    
    def activate(self):
        channel = AnalogIn(self.ads, ADS.P0)
        return f"Analog Value: {channel.value}, Voltage : {channel.voltage:.2f}"

if __name__ == "__main__":
    pot = Pot()
    while True:
        print(pot.activate())
        time.sleep(0.2)
