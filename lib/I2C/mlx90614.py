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

    def activate_gui(self):
        try:
            object_temp = self.read_temperature()
            if object_temp is not None:
                return(f"Object Temperature: {object_temp:.2f} C")
                time.sleep(1)
            else:
                return("Failed to read temperature")
                time.sleep(1)
        except Exception as e:
            return(f"Error reading MLX90614 sensor: {e}")
            time.sleep(1)  # Wait for 1 second before the next read
    
    def activate_cli(self):
        try:
            while True:
                try:
                    object_temp = self.read_temperature()
                    if object_temp is not None:
                        print(f"Object Temperature: {object_temp:.2f} C")
                        time.sleep(1)
                    else:
                        print("Failed to read temperature")
                        time.sleep(1)
                except Exception as e:
                    print(f"Error reading MLX90614 sensor: {e}")
                    time.sleep(1)  # Wait for 1 second before the next read
        except KeyboardInterrupt:
            print("Interrupted by user. Exiting...")
        except Exception as e:
            print(f"An error occurred: {e}")
            
if __name__ == "__main__":
    obj = MLX90614()
    print(obj.activate())
