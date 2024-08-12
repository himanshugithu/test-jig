# import smbus

# def scan_i2c_bus(bus_number=1):
#     bus = smbus.SMBus(bus_number)
#     devices = []
#     for address in range(0x03, 0x78):
#         try:
#             bus.write_quick(address)
#             devices.append(hex(address))
#         except OSError:
#             pass
#     return devices

# if __name__ == "__main__":
#     print(scan_i2c_bus())


# import spidev
# import time

# # Open SPI bus 0, device (CS) 0
# spi = spidev.SpiDev()
# spi.open(0, 0)

# # Set SPI speed and mode
# spi.max_speed_hz = 50000
# spi.mode = 0

# # Function to write data to SPI and read response
# def write_read(data):
#     response = spi.xfer2(data)
#     return response

# # Test data
# test_data = [0x01, 0x02, 0x03]

# # Send and receive data
# print("Sending data: ", test_data)
# response = write_read(test_data)
# print("Received data: ", response)

# # Close SPI connection
# spi.close()


# import time
# import board
# import busio
# from adafruit_ads1x15.ads1115 import ADS1115
# from adafruit_ads1x15.analog_in import AnalogIn

# i2c = busio.I2C(board.SCL, board.SDA)
# ads = ADS1115(i2c)
# chan = AnalogIn(ads, ADS1115.P0)
# print("{:>5}\t{:>5}".format('raw', 'v'))
# try:
#     while True:
#         print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Exiting program")
# finally:
#     print("Program terminated")
