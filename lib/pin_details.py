class PIN_CONNECTION:
    def __init__(self, device=None):
        self.device = device
        self.pin_mappings = {
            "OLED": self.i2c_pins,
            "BH1750": self.i2c_pins,
            "SPI OLED": self.spi_oled_pins,
            "SD CARD": self.sd_card_pins,
            "LED": self.led,
            "BUTTON": self.button,
            "ULTRASONIC": self.ultrasonic_pins,
            "DHT11": self.dht11,
            "RGB led": self.RGB,
            "SERVO": self.servo,
            "LED_FADE":self.led_fade
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

#//////////////////////////////////////////I2C PORT/////////////////////////////////////////
    def i2c_pins(self):
        return ('''
{} pin | I2C port
"""""""""""""""""""""""
    VCC     |    Rpi VCC 
    GND     |    Rpi GND
    SCL     |    PIN 1 (I2C PORT)
    SDA     |    PIN 2 (I2C PORT)
        '''.format(self.device))

#//////////////////////////////////////////SPI PORT/////////////////////////////////////////

    def spi_oled_pins(self):
        return ('''
{} pin | SPI port
"""""""""""""""""""""""
    VCC     |    Rpi VCC 
    GND     |    Rpi GND
    SCK     |    PIN 3 (SPI PORT)
    SDA     |    PIN 2 (SPI PORT)
    RES     |    PIN 6 (SPI PORT)
    DC      |    PIN 5 (SPI PORT)
    CS      |    PIN 4 (SPI PORT)
        '''.format(self.device))

    def sd_card_pins(self):
        return ('''
{} pin | SPI port
"""""""""""""""""""""""
    VCC     |    Rpi VCC 
    GND     |    Rpi GND
    MISO    |    PIN X (SPI PORT)
    MOSI    |    PIN Y (SPI PORT)
    SCK     |    PIN Z (SPI PORT)
    CS      |    PIN W (SPI PORT)
        '''.format(self.device))

#//////////////////////////////////////////GPIO PORT/////////////////////////////////////////

    def led(self):
        return ('''
{} pin | GPIO port
"""""""""""""""""""""""
    LED(+)  |    PIN 1 (GPIO PORT)
    GND     |    Rpi GND
        '''.format(self.device))

    def button(self):
        return ('''
{} pin | GPIO port
"""""""""""""""""""""""
    Terminal 1  |    PIN 2 (GPIO PORT)
    Terminal 2  |    Rpi GND
        '''.format(self.device))

    def dht11(self):
        return ('''
{} pin | GPIO port
"""""""""""""""""""""""
    VCC     |    Rpi VCC
    GND     |    Rpi GND
    DATA    |    PIN 3 (GPIO PORT)         
        '''.format(self.device))

    def ultrasonic_pins(self):
        return ('''
{} pin | GPIO port
"""""""""""""""""""""""
    VCC     |    Rpi VCC 
    GND     |    Rpi GND
    Trigger |    PIN 6 (GPIO PORT)
    Echo    |    PIN 5 (GPIO PORT)
        '''.format(self.device))

#//////////////////////////////////////////PWM PORT/////////////////////////////////////////
    def led_fade(self):
        return ('''
{} pin | PWM port
"""""""""""""""""""""""
    LED  |    PIN 1 (PWM PORT)
    GND  |    Rpi GND
        '''.format(self.device))



    def RGB(self):
        return ('''
{} pin | PWM port
"""""""""""""""""""""""
    R    |    PIN 1 (PWM PORT)
    B    |    PIN 2 (PWM PORT)
    G    |    PIN 3 (PWM PORT)
    GND  |    Rpi GND
        '''.format(self.device))

    def servo(self):
        return ('''
{} pin | PWM port
"""""""""""""""""""""""
    VCC     |    Rpi VCC
    GND     |    Rpi GND
    Signal  |    PIN 4 (PWM PORT)
        '''.format(self.device))
        
#//////////////////////////////////////////ADC PORT//////////////////////////////////////////
#//////////////////////////////////////////UART PORT/////////////////////////////////////////
if __name__ == "__main__":
    pin = PIN_CONNECTION("oled".upper())
    print(pin.pin_connections)
