
# SCRC TEST-JIG

This project exploring and utilizing various hardware protocols to interface with different sensors and modules. The Raspberry Pi 3 supports several key communication protocols, each of which plays a crucial role in connecting and interacting with external components.

**General Purpose Input/Output (GPIO)** : is a fundamental protocol that allows the Raspberry Pi to read from and send signals to a wide range of external devices. GPIO pins can be configured as either input or output, making them versatile for various applications. For example, you might connect an LED to a GPIO pin and control its brightness or blink rate through programming, providing a simple yet effective way to test and visualize the functionality of GPIO.

**Inter-Integrated Circuit (I2C)** is a communication protocol that facilitates the connection of multiple devices using just two wires: one for data (SDA) and one for clock (SCL). This protocol is ideal for connecting sensors and modules that require minimal wiring. For instance, you could connect an I2C temperature sensor like the BMP180 to the Raspberry Pi to read temperature data. By using the I2C protocol, you can easily gather sensor information and integrate it into your project.

**Serial Peripheral Interface (SPI)** : is another communication protocol that supports high-speed data exchange between a master device and one or more slave devices. SPI requires four wires: Master Out Slave In (MOSI), Master In Slave Out (MISO), Serial Clock (SCK), and Slave Select (SS). An example application would be connecting an SPI-based display, such as an OLED screen, to the Raspberry Pi. This setup allows you to display text or graphical information, showcasing the capability of SPI in handling complex data transfers.

**Analog-to-Digital Converter (ADC)** : is essential for reading analog signals since the Raspberry Pi itself does not have built-in ADC functionality. By incorporating an external ADC module like the MCP3008, you can read varying voltage levels from components like a potentiometer. This conversion of analog signals to digital data enables you to monitor and process analog input accurately.

**Pulse Width Modulation (PWM)** : is used to simulate analog output through a digital signal by rapidly switching it on and off. This technique is useful for controlling devices such as motors or adjusting the brightness of LEDs. For example, you might use PWM to control the angle of a servo motor connected to the Raspberry Pi, allowing for precise adjustments and movements.

**Universal Asynchronous Receiver/Transmitter (UART)**: is a serial communication protocol designed for asynchronous data transmission. It is ideal for connecting devices that communicate via serial data streams, such as a GPS module. By using UART, you can receive location data from the GPS module and process it on the Raspberry Pi, demonstrating the protocol’s efficiency in handling serial data.

Through this project, you are gaining practical experience with these essential hardware protocols, testing various sensors and modules, and integrating their outputs into a cohesive system. Each protocol offers unique advantages and applications, providing a comprehensive understanding of the Raspberry Pi 3’s capabilities in interacting with external hardware.

---

### *I2C INITIALIZATION*
### Software Configuration
1. **Enable I2C Interface:**

- Open a terminal on your Raspberry Pi.
- Run `sudo raspi-config` to open the Raspberry Pi configuration tool.
- Navigate to Interface Options -> I2C and enable the I2C interface.
- Exit the configuration tool and reboot the Raspberry Pi to apply the changes.

2. **Install I2C Tools:**
- Update your package list and install the I2C tools by running
```bash
sudo apt-get update
sudo apt-get install -y i2c-tools
```
## Check Device Connection

1. Scan for I2C Devices:
  - After rebooting, open a terminal and run
```bash
sudo i2cdetect -y 1
```
- This command will scan the I2C bus (bus 1) and list the addresses of any connected I2C devices.
- If your I2C device is connected properly, you should see its address displayed in the output.

## Example Output

The output of the i2cdetect command will look something like this:

        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --     
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --     
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    70: -- -- -- -- -- -- -- --

After connecting I2C device Output it show output like this 

        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:                         -- -- -- -- -- -- -- -- 
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    20: -- -- -- 23 -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- -- 
    40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- 5a -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    70: -- -- -- -- -- -- -- -- 

Here i connect the four I2C device 
   - OLED (0x3c)
   - BH1750 (0x23)
   - MLX90614 (0x5a) 
   - ADS115 (0x48)
   
---

### install Python module for I2C

1. Ensure I2C Interface is Enabled:

- Confirm that the I2C interface is enabled as described in previous steps.

#### Install Python I2C Library:

- Install the smbus or smbus2 library, which provides access to the I2C bus:
```bash
sudo apt-get update
sudo apt-get install -y python3-smbus
```
<details>
  <summary>Try this Code</summary>
  
  ```python
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
#output : ['0x23', '0x3c', '0x48', '0x5a']      
```    
</details>

---

## *SPI INITIALIZATION*


### Software Configuration
Enable SPI Interface:

Open a terminal on your Raspberry Pi.
Run ```sudo raspi-config``` to open the Raspberry Pi configuration tool.
Navigate to Interface Options -> SPI and enable the SPI interface.
Exit the configuration tool and reboot the Raspberry Pi to apply the changes.

### Install SPI Tools:

- Update your package list and install the SPI tools by running:
```bash
sudo apt-get update
sudo apt-get install -y python3-spidev
```  



#### Check Device Connection

1. Verify SPI Module:

- After rebooting, check if the SPI module is loaded by running:
```bash
lsmod | grep spi
```

- You should see something like:
```bash
spi_bcm2835             20480  0
```
This confirms that the SPI driver is loaded.

- spi_bcm2835: The name of the SPI driver module.
- 20480: The size of the module in bytes.
- 0: The number of instances of this module currently in use.


#### To check the available SPI buses, you can list the devices under /dev/:

```bash
ls /dev/spidev*
```

You should see something like:

```bash
/dev/spidev0.0  /dev/spidev0.1
```
- /dev/spidev0.0: Represents SPI bus 0, chip select 0 (CE0).
- /dev/spidev0.1: Represents SPI bus 0, chip select 1 (CE1).

---
## UART INITIALIZATION
1. Enable UART on Raspberry Pi
#### Using raspi-config:

- Open a terminal and run:
```bash
sudo raspi-config
```
- Navigate to Interfacing Options -> Serial.
- When asked "Would you like a login shell to be accessible over serial?", select No.
- When asked "Would you like the serial port hardware to be enabled?", select Yes.
- Exit raspi-config and reboot the Raspberry Pi:
```bash
sudo reboot
```

#### Manually via config.txt:

- Open the boot configuration file:
```bash

sudo nano /boot/config.txt
```
Ensure the following line is present to enable UART if not add:
```bash
enable_uart=1
```

- Save and exit (Ctrl+X, Y, Enter).
- Reboot the Raspberry Pi:
```bash
sudo reboot
```

### 2. Install Python Serial Library
You'll need the pyserial library to communicate over UART in Python.

```bash
sudo apt-get update
sudo apt-get install -y python3-serial
```
