import smbus2
import time

# SGP40 I2C address
SGP40_ADDR = 0x59

# SGP40 commands
SGP40_INIT = [0x20, 0x03]
SGP40_MEASURE = [0x20, 0x08]

def initialize_sgp40(bus_number=1):
    try:
        bus = smbus2.SMBus(bus_number)
        bus.write_i2c_block_data(SGP40_ADDR, 0x00, SGP40_INIT)
        time.sleep(0.1)
        return True
    except OSError as e:
        print(f"Error initializing SGP40 sensor: {e}")
        return False

def read_voc_index(bus_number=1):
    try:
        bus = smbus2.SMBus(bus_number)
        bus.write_i2c_block_data(SGP40_ADDR, 0x00, SGP40_MEASURE)
        time.sleep(0.1)
        raw_data = bus.read_i2c_block_data(SGP40_ADDR, 0x00, 3)
        voc_index = (raw_data[0] << 8) | raw_data[1]
        return voc_index
    except OSError as e:
        print(f"Error reading VOC index from SGP40 sensor: {e}")
        return None

if __name__ == "__main__":
    if initialize_sgp40():
        while True:
            voc_index = read_voc_index()
            if voc_index is not None:
                print(f"VOC Index: {voc_index}")
            time.sleep(1)  # Repeat every 1 second
