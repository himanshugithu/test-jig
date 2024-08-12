import time
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
chan = AnalogIn(ads, ADS1115.P0)
print("{:>5}\t{:>5}".format('raw', 'v'))
try:
    while True:
        print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting program")
finally:
    print("Program terminated")
