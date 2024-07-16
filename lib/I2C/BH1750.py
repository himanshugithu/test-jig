import smbus2
import time
import smbus

class BH1750:
    BH1750_ADDR = 0x23
    POWER_DOWN = 0x00
    POWER_ON = 0x01
    RESET = 0x07

    # Measurement modes
    CONTINUOUS_HIGH_RES_MODE = 0x10  # Start measurement at 1 lx resolution. Measurement Time is typically 120ms.
    CONTINUOUS_HIGH_RES_MODE_2 = 0x11  # Start measurement at 0.5 lx resolution. Measurement Time is typically 120ms.
    CONTINUOUS_LOW_RES_MODE = 0x13  # Start measurement at 4 lx resolution. Measurement Time is typically 16ms.
    ONE_TIME_HIGH_RES_MODE = 0x20  # Start measurement at 1 lx resolution. Measurement Time is typically 120ms.
    ONE_TIME_HIGH_RES_MODE_2 = 0x21  # Start measurement at 0.5 lx resolution. Measurement Time is typically 120ms.
    ONE_TIME_LOW_RES_MODE = 0x23  # Start measurement at 4 lx resolution. Measurement Time is typically 16ms.

    def __init__(self, bus_number=1):
        self.bus_number = bus_number
        self.bus = smbus.SMBus(bus_number)

    def scan_i2c_bus(self):
        devices = []
        for address in range(0x03, 0x78):
            try:
                self.bus.write_quick(address)
                devices.append(f"Device: {hex(address)}")
            except OSError:
                pass
        return devices

    def convert_to_lux(self, data):
        # Convert data to lux according to sensor documentation
        return ((data[1] + (256 * data[0])) / 1.2)

    def activate_gui(self, mode=ONE_TIME_HIGH_RES_MODE):
        try:
            bus = smbus2.SMBus(self.bus_number)  # Open /dev/i2c-1
            try:
                bus.write_byte(self.BH1750_ADDR, mode)  # Change mode as you like
                time.sleep(0.2)  # Wait for measurement
                data = bus.read_i2c_block_data(self.BH1750_ADDR, 0x00, 2)  # Read data
                lux = self.convert_to_lux(data)
                return(f"Light level: {lux:.2f} lx")
            except Exception as e:
                return(f"Error reading BH1750 sensor: {e}")
                time.sleep(1)  # Wait for 1 second before the next read
        except KeyboardInterrupt:
            print("Interrupted by user. Exiting...")
        except Exception as e:
            print(f"An error occurred: {e}")
    def activate_cli(self, mode=ONE_TIME_HIGH_RES_MODE):
        try:
            bus = smbus2.SMBus(self.bus_number)  # Open /dev/i2c-1
            while True:
                try:
                    bus.write_byte(self.BH1750_ADDR, mode)  # Change mode as you like
                    time.sleep(0.2)  # Wait for measurement
                    data = bus.read_i2c_block_data(self.BH1750_ADDR, 0x00, 2)  # Read data
                    lux = self.convert_to_lux(data)
                    print(f"Light level: {lux:.2f} lx")
                except Exception as e:
                    print(f"Error reading BH1750 sensor: {e}")
                    time.sleep(1)  # Wait for 1 second before the next read
        except KeyboardInterrupt:
            print("Interrupted by user. Exiting...")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    sensor = BH1750()
    lux = sensor.activate()
    if lux is not None:
        print(lux)