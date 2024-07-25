
# SCRC TEST-JIG

This project exploring and utilizing various hardware protocols to interface with different sensors and modules. The Raspberry Pi 3 supports several key communication protocols, each of which plays a crucial role in connecting and interacting with external components.

**General Purpose Input/Output (GPIO)** : is a fundamental protocol that allows the Raspberry Pi to read from and send signals to a wide range of external devices. GPIO pins can be configured as either input or output, making them versatile for various applications. For example, you might connect an LED to a GPIO pin and control its brightness or blink rate through programming, providing a simple yet effective way to test and visualize the functionality of GPIO.

**Inter-Integrated Circuit (I2C)** is a communication protocol that facilitates the connection of multiple devices using just two wires: one for data (SDA) and one for clock (SCL). This protocol is ideal for connecting sensors and modules that require minimal wiring. For instance, you could connect an I2C temperature sensor like the BMP180 to the Raspberry Pi to read temperature data. By using the I2C protocol, you can easily gather sensor information and integrate it into your project.

**Serial Peripheral Interface (SPI)** : is another communication protocol that supports high-speed data exchange between a master device and one or more slave devices. SPI requires four wires: Master Out Slave In (MOSI), Master In Slave Out (MISO), Serial Clock (SCK), and Slave Select (SS). An example application would be connecting an SPI-based display, such as an OLED screen, to the Raspberry Pi. This setup allows you to display text or graphical information, showcasing the capability of SPI in handling complex data transfers.

**Analog-to-Digital Converter (ADC)** : is essential for reading analog signals since the Raspberry Pi itself does not have built-in ADC functionality. By incorporating an external ADC module like the MCP3008, you can read varying voltage levels from components like a potentiometer. This conversion of analog signals to digital data enables you to monitor and process analog input accurately.

**Pulse Width Modulation (PWM)** : is used to simulate analog output through a digital signal by rapidly switching it on and off. This technique is useful for controlling devices such as motors or adjusting the brightness of LEDs. For example, you might use PWM to control the angle of a servo motor connected to the Raspberry Pi, allowing for precise adjustments and movements.

**Universal Asynchronous Receiver/Transmitter (UART)**: is a serial communication protocol designed for asynchronous data transmission. It is ideal for connecting devices that communicate via serial data streams, such as a GPS module. By using UART, you can receive location data from the GPS module and process it on the Raspberry Pi, demonstrating the protocol’s efficiency in handling serial data.

Through this project, you are gaining practical experience with these essential hardware protocols, testing various sensors and modules, and integrating their outputs into a cohesive system. Each protocol offers unique advantages and applications, providing a comprehensive understanding of the Raspberry Pi 3’s capabilities in interacting with external hardware.

span style="font-size:1.5em; font-weight:bold;"> **Inter-Integrated Circuit (I2C)**
Enable I2C Interface: 
