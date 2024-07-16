import smbus
import time

class MLX90614:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.address = 0x5A

    def read_temperature(self):
        # Read two bytes of data from the object temperature register (0x07)
        data = self.bus.read_i2c_block_data(self.address, 0x07, 2)
        # Convert the data
        temp = (data[1] << 8 | data[0])
        temp = temp * 0.02 - 273.15  # Convert to Celsius
        return temp

    def activate(self):
        
        object_temp = self.read_temperature()
        return(f"Object Temperature: {object_temp:.2f} C")
            
if __name__ == "__main__":
    obj = MLX90614()
    print(obj.activate())
