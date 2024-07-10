import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import numpy as np

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
        
        # Polynomial coefficients from your calibration
        self.coefficients = np.array([200, -100, 0])  # Replace with your fitted coefficients
        self.polynomial = np.poly1d(self.coefficients)
    
    def read_tds(self):
        channel = AnalogIn(self.ads, ADS.P1)
        voltage = channel.voltage
        tds = self.convert_voltage_to_tds(voltage)
        return voltage, tds

    def convert_voltage_to_tds(self, voltage):
        # Use the polynomial to convert voltage to TDS
        tds = self.polynomial(voltage)
        if tds < 0:
            tds = 0
        return tds

if __name__ == "__main__":
    pot = Pot()
    tds_sensor = TDSSensor()
    
    while True:
        voltage, tds = tds_sensor.read_tds()

        print(f"TDS Voltage: {voltage:.2f}V, TDS Value: {tds:.2f} ppm")
        
        time.sleep(0.2)
