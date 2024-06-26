import smbus

def scan_i2c_bus(bus_number=1):
    bus = smbus.SMBus(bus_number)
    devices = []
    for address in range(0x03, 0x78):
        try:
            bus.write_quick(address)
            devices.append(hex(address))
        except OSError:
            pass
    return devices

if __name__ == "__main__":
    print(scan_i2c_bus())
