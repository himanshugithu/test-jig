import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class Pot:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
    
    def activate_gui(self):
        channel = AnalogIn(self.ads, ADS.P0)
        return f"Analog Value: {channel.value}, Voltage : {channel.voltage:.2f}"
    
    def activate_cli(self):
        try:
            while True:
                channel = AnalogIn(self.ads, ADS.P0)
                print(f"Analog Value: {channel.value}, Voltage : {channel.voltage:.2f}")
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("Existing..") 
        except Exception as e:
            print("error")

if __name__ == "__main__":
    pot = Pot()
    while True:
        print(pot.activate_cli())
        time.sleep(0.2)
