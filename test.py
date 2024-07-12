import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class TDS_Sensor:
    def __init__(self, channel=0):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.channel = channel

        if channel == 0:
            self.chan = AnalogIn(self.ads, ADS.P0)
        elif channel == 1:
            self.chan = AnalogIn(self.ads, ADS.P1)
        elif channel == 2:
            self.chan = AnalogIn(self.ads, ADS.P2)
        elif channel == 3:
            self.chan = AnalogIn(self.ads, ADS.P3)
        else:
            raise ValueError("Channel must be 0, 1, 2, or 3")

    def read_voltage(self):
        return self.chan.voltage

    def read_tds(self):
        voltage = self.read_voltage()
        tds_value = (133.42 * voltage**3 - 255.86 * voltage**2 + 857.39 * voltage) * 0.5
        return tds_value

    def activate(self):
        sensor = TDS_Sensor(channel=0)
        tds_value = sensor.read_tds()
        return(f"TDS Value: {tds_value:.2f} ppm")


if __name__ == "__main__":
    sensor = TDS_Sensor(channel=0)
    print(sensor.activate())
    time.sleep(1)
        
