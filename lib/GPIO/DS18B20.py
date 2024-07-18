import os
import glob
import time

class DS18B20:
    def __init__(self, base_dir='/sys/bus/w1/devices/'):
        self.base_dir = base_dir
        self.device_folder = self.get_device_folder()
        self.device_file = self.device_folder + '/w1_slave'
        self.initialize_sensor()

    def initialize_sensor(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

    def get_device_folder(self):
        device_folders = glob.glob(self.base_dir + '28*')
        if not device_folders:
            raise FileNotFoundError("No DS18B20 sensor found.")
        return device_folders[0]

    def read_temp_raw(self):
        with open(self.device_file, 'r') as f:
            lines = f.readlines()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        # print(lines[0])
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
        else:
            raise ValueError("Could not read temperature.")
        
    def activate_gui(self):
        try:
            temperature = self.read_temp()
            return(f"Temperature: {temperature:.2f}°C")
        except Exception as e:
            return(f"Error: {e}")

    def activate_cli(self):
        try:
            while True:
                temperature = self.read_temp()
                print(f"Temperature: {temperature:.2f}°C")
        except Exception as e:
            return(f"Error: {e}")
        except KeyboardInterrupt:
            print("exiting")
            
if __name__ == "__main__":
    sensor = DS18B20()
    sensor.activate()
    time.sleep(1)
