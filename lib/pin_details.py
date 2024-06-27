class PIN_CONNECTION:
    def __init__(self, device=None):
        self.device = device
        self.pin_mappings = {
            "oled": self.i2c_pins,
            "bh1750": self.i2c_pins,
            "spi_oled": self.spi_oled_pins,
            "sd_card": self.sd_card_pins,
            "led": self.led,
            "button": self.button,
            "ultrasonic": self.ultrasonic_pins,
            "dht11": self.dht11,
            "rgb": self.rgb,
            "servo": self.servo
        }
        
        if self.device:
            self.display_pin_connections(self.device)
        else:
            print("Unknown device")

    def display_pin_connections(self, device):
        if device in self.pin_mappings:
            self.pin_mappings[device]()
        else:
            print("Unknown device: {}".format(device))


#//////////////////////////////////////////I2C PORT/////////////////////////////////////////
    def i2c_pins(self):
        print('''
{} pin | I2C port
"""""""""""""""""""""""
    VCC     |    Rpi VCC 
    GND     |    Rpi GND
    SCL     |    PIN 1 (I2C PORT)
    SDA     |    PIN 2 (I2C PORT)
        '''.format(self.device))

#//////////////////////////////////////////SPI PORT/////////////////////////////////////////

    def spi_oled_pins(self):
        print('''
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
        print('''
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
        print('''
{} pin | GPIO port
"""""""""""""""""""""""
    LED(+)  |    PIN 1 (GPIO PORT)
    GND     |    Rpi GND
        '''.format(self.device))

    def button(self):
        print('''
{} pin | GPIO port
"""""""""""""""""""""""
    Terminal 1  |    PIN 2 (GPIO PORT)
    Terminal 2  |    Rpi GND
        '''.format(self.device))

    def dht11(self):
        print('''
{} pin | GPIO port
"""""""""""""""""""""""
    VCC     |    Rpi VCC
    GND     |    Rpi GND
    DATA    |    PIN 3 (GPIO PORT)         
        '''.format(self.device))

    def ultrasonic_pins(self):
        print('''
{} pin | GPIO port
"""""""""""""""""""""""
    VCC     |    Rpi VCC 
    GND     |    Rpi GND
    Trigger |    PIN 6 (GPIO PORT)
    Echo    |    PIN 5 (GPIO PORT)
        '''.format(self.device))

#//////////////////////////////////////////PWM PORT/////////////////////////////////////////

    def rgb(self):
        print('''
{} pin | PWM port
"""""""""""""""""""""""
    R    |    PIN 1 (PWM PORT)
    B    |    PIN 2 (PWM PORT)
    G    |    PIN 3 (PWM PORT)
    GND  |    Rpi GND
        '''.format(self.device))

    def servo(self):
        print('''
{} pin | PWM port
"""""""""""""""""""""""
    VCC     |    Rpi VCC
    GND     |    Rpi GND
    Signal  |    PIN 4 (PWM PORT)
        '''.format(self.device))
        
#//////////////////////////////////////////ADC PORT//////////////////////////////////////////
#//////////////////////////////////////////UART PORT/////////////////////////////////////////
if __name__ == "__main__":
    pin = PIN_CONNECTION()
    print(pin.pin_mappings.keys())
    for i in pin.pin_mappings.keys():
        PIN_CONNECTION(i)


