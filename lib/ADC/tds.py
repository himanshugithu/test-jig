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
        self.chan = AnalogIn(self.ads, ADS.P0 + channel)  # Adjust the channel accordingly

    def read_voltage(self):
        return self.chan.voltage

    def read_tds(self):
        voltage = self.read_voltage()
        tds_value = (133.42 * voltage**3 - 255.86 * voltage**2 + 857.39 * voltage) * 0.5
        return tds_value

    def activate_gui(self):
        samples = []
        for _ in range(20):
            tds_value = self.read_tds()
            samples.append(tds_value)
            time.sleep(0.1)  # Delay between samples to allow stable readings
        max_tds_value = max(samples)
        return f"TDS Value: {max_tds_value:.2f} ppm"
    
    def activate_cli(self):
        try:
            while True:
                samples = []
                for _ in range(20):
                    tds_value = self.read_tds()
                    samples.append(tds_value)
                    time.sleep(0.1)  # Delay between samples to allow stable readings
                max_tds_value = max(samples)
                print(f"TDS Value: {max_tds_value:.2f} ppm")
        except KeyboardInterrupt:
            print("Interrupted by user. Exiting...")
        except Exception as e:
            print(f"An error occurred: {e}")    
            

if __name__ == "__main__":
    sensor = TDS_Sensor(channel=0)
    print(sensor.activate())
    time.sleep(1)
