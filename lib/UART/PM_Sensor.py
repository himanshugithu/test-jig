import serial
import struct
import time

class SDS011:
    def __init__(self, port='/dev/ttyS0'):
        try:
            self.ser = serial.Serial(port, baudrate=9600, timeout=2)
            self.ser.flush()
            # print("Sensor connected successfully.")
        except serial.SerialException:
            self.ser = None
            # print("Failed to connect to sensor. Please check the connection.")

    def read(self):
        if self.ser is None:
            return (None, None)
        
        byte = 0
        while byte != b'\xaa':
            byte = self.ser.read(size=1)
            if byte == b'':
                print("No data received from sensor.")
                return (None, None)

        data = self.ser.read(size=9)
        if len(data) != 9:
            print("Incomplete data received from sensor.")
            return (None, None)
            
        if data[0] == 0xc0:
            pm25 = struct.unpack('<H', data[2:4])[0] / 10.0
            pm10 = struct.unpack('<H', data[4:6])[0] / 10.0
            return (pm25, pm10)
        return (None, None)

    def close(self):
        if self.ser:
            self.ser.close()
    def activate_gui(self):
        sensor = SDS011()
        pm25, pm10 = sensor.read()
        if pm25 is not None and pm10 is not None:
            return(f"PM2.5: {pm25} µg/m³, PM10: {pm10} µg/m³")
        else:
            return "data is not valid"

    def activate_cli(self):
        sensor = SDS011()
        try:
            while True:
                try:
                    pm25, pm10 = sensor.read()
                    if pm25 is not None and pm10 is not None:
                        print(f"PM2.5: {pm25} µg/m³, PM10: {pm10} µg/m³")
                    else:
                        print("data is not valid") 
                except Exception as e:
                    print(f"Error reading pm sensor sensor: {e}")
                    time.sleep(1)        
        except KeyboardInterrupt:
            print("Interrupted by user. Exiting...")        


if __name__ == "__main__":
    sensor = SDS011()
    try:
        while True:
            print(sensor.activate())
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        sensor.close()
