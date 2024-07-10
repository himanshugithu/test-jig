import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class Pot:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
    
    def read_pot(self):
        channel = AnalogIn(self.ads, ADS.P0)
        return f"Analog Value: {channel.value}, Voltage: {channel.voltage:.2f}V"

class TDSSensor:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
    
    def read_tds(self):
        channel = AnalogIn(self.ads, ADS.P1)
        voltage = channel.voltage
        tds = self.convert_voltage_to_tds(voltage)-500
        return f"TDS Voltage: {voltage:.2f}V, TDS Value: {tds:.2f} ppm"

    def convert_voltage_to_tds(self, voltage):
        # Assuming a basic linear conversion
        # You may need to adjust this based on your sensor and calibration data
        tds = (voltage - 0.5) * 1000
        return tds

if __name__ == "__main__":
    tds_sensor = TDSSensor()
    
    while True:
        print(tds_sensor.read_tds())
        time.sleep(0.2)
