import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device (CS) 0
spi.max_speed_hz = 50000  # Set SPI speed (adjust if necessary)

def check_sd_card():
    try:
        # Send CMD0 to reset SD card
        cmd0 = [0x40, 0x00, 0x00, 0x00, 0x00, 0x95]  # Corrected CMD0 command byte
        spi.xfer2(cmd0)
        time.sleep(0.1)
        response = spi.readbytes(1)
        print("CMD0 Response:", response)

        # Send CMD8 to check SD card voltage range (for SDHC/SDXC)
        cmd8 = [0x48, 0x00, 0x00, 0x01, 0xAA, 0x87]
        spi.xfer2(cmd8)
        time.sleep(0.1)
        response = spi.readbytes(5)  # Adjust response length as necessary
        print("CMD8 Response:", response)
        
        if response[0] == 0x01:
            print("SD card initialized and ready.")
        else:
            print("SD card initialization failed.")
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        spi.close()

# Execute the check function
check_sd_card()
