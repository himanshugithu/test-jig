import textwrap

class PIN_CONNECTION:
    def __init__(self, device=None):
        self.device = device
        self.pin_mappings = {
            "OLED"    :self.i2c_pins,
            "BH1750"  :self.i2c_pins,
            "MXL90614":self.i2c_pins,

            "SPI OLED": self.spi_oled_pins,
            "SD CARD": self.sd_card_pins,

            "led": self.led,
            "button": self.button,
            "ultrasonic sensor": self.ultrasonic_pins,
            "DHT11": self.dht11,
            "DS18B20":self.ds18b20,

            "RGB led": self.RGB,
            "servo motor": self.servo,
            "LED_FADE": self.led_fade,

            "PM Sensor": self.pm_sensor,

            "Potentiometer": self.pot,
            "ldr": self.ldr,
            "tds": self.tds
        }
        
        if self.device:
            self.pin_connections = self.display_pin_connections(self.device)
        else:
            self.pin_connections = "Unknown device"

    def display_pin_connections(self, device):
        if device in self.pin_mappings:
            return self.pin_mappings[device]()
        else:
            return "Unknown device: {}".format(device)

    # I2C Port
    def i2c_pins(self):
        return textwrap.dedent(f'''
        {self.device} pin    |    I2C port
        """""""""""""""""""""""""
            VCC     |    Rpi VCC 
            GND     |    Rpi GND
            SCL     |    PIN 1 (I2C PORT)
            SDA     |    PIN 2 (I2C PORT)
        ''')

    # SPI Port
    def spi_oled_pins(self):
        return textwrap.dedent(f'''
        {self.device} pin | SPI port
        """""""""""""""""""""""""
            VCC     |    Rpi VCC 
            GND     |    Rpi GND
            SCK     |    PIN 3 (SPI PORT)
            SDA     |    PIN 2 (SPI PORT)
            RES     |    PIN 6 (SPI PORT)
            DC      |    PIN 5 (SPI PORT)
            CS      |    PIN 4 (SPI PORT)
        ''')

    def sd_card_pins(self):
        return textwrap.dedent(f'''
        {self.device} pin | SPI port
        """""""""""""""""""""""""
            VCC     |    Rpi VCC 
            GND     |    Rpi GND
            MISO    |    PIN X (SPI PORT)
            MOSI    |    PIN Y (SPI PORT)
            SCK     |    PIN Z (SPI PORT)
            CS      |    PIN W (SPI PORT)
        ''')

    # GPIO Port
    def led(self):
        return textwrap.dedent(f'''
        {self.device} pin | GPIO port
        """""""""""""""""""""""""
            LED(+)  |    PIN 2 (GPIO PORT)
            GND     |    Rpi GND
        ''')

    def button(self):
        return textwrap.dedent(f'''
        {self.device} pin | GPIO port
        """""""""""""""""""""""""
            Terminal 1  |    PIN 3 (GPIO PORT)
            Terminal 2  |    Rpi GND
        ''')

    def dht11(self):
        return textwrap.dedent(f'''
        {self.device} pin | GPIO port
        """""""""""""""""""""""""
            VCC     |    Rpi VCC
            GND     |    Rpi GND
            DATA    |    PIN 4 (GPIO PORT)         
        ''')

    def ultrasonic_pins(self):
        return textwrap.dedent(f'''
        {self.device} pin | GPIO port
        """""""""""""""""""""""""
            VCC     |    Rpi VCC 
            GND     |    Rpi GND
            Trigger |    PIN 6 (GPIO PORT)
            Echo    |    PIN 5 (GPIO PORT)
        ''')
    def ds18b20(self):
        return textwrap.dedent(f'''
        {self.device} pin | GPIO port
        """""""""""""""""""""""""
            VCC     |    Rpi VCC 
            GND     |    Rpi GND
            signal  |    PIN 1 (GPIO PORT)
        ''') 

    # PWM Port
    def led_fade(self):
        return textwrap.dedent(f'''
        {self.device} pin | PWM port
        """""""""""""""""""""""""
            LED  |    PIN 1 (PWM PORT)
            GND  |    Rpi GND
        ''')

    def RGB(self):
        return textwrap.dedent(f'''
        {self.device} pin | PWM port
        """""""""""""""""""""""""
                R    |    PIN 1 (PWM PORT)
                B    |    PIN 2 (PWM PORT)
                G    |    PIN 3 (PWM PORT)
            GND    |    Rpi GND
        ''')

    def servo(self):
        return textwrap.dedent(f'''
        {self.device} pin | PWM port
        """""""""""""""""""""""""
            VCC     |    Rpi VCC
            GND     |    Rpi GND
            Signal  |    PIN 4 (PWM PORT)
        ''')

    # ADC Port
    def pot(self):
        return textwrap.dedent(f'''
        {self.device} pin | ADC port
        """""""""""""""""""""""""
            VCC      |    Rpi VCC
            GND      |    Rpi GND
            DATA PIN |    PIN 1 (ADC PORT)
        ''')

    def ldr(self):
        return textwrap.dedent(f'''
        {self.device} pin | ADC port
        """""""""""""""""""""""""
            VCC      |    Rpi VCC
            GND      |    Rpi GND
            DATA PIN |    PIN 1 (ADC PORT)
        ''')

    def tds(self):
        return textwrap.dedent(f'''
        {self.device} pin | ADC port
        """""""""""""""""""""""""
            VCC      |    Rpi VCC
            GND      |    Rpi GND
            DATA PIN |    PIN 1 (ADC PORT)
        ''')

    # UART Port
    def pm_sensor(self):
        return textwrap.dedent(f'''
        {self.device} pin | UART port
        """""""""""""""""""""""""
            VCC     |    Rpi VCC
            GND     |    Rpi GND
            RX      |    PIN 1 (UART PORT )
            TX      |    PIN 2 (UART PORT )
        ''')

if __name__ == "__main__":
    pin = PIN_CONNECTION("oled".upper())
    print(pin.pin_connections)
