class PIN_CONNECTION:
    def __init__(self,device):
        self.device = device
        print(self.device)

        if self.device == "oled" or "bh1750":
            print(f'''
{self.device} pin | I2C port
"""""""""""""""""""""""
    VCC     |    Rpi VCC 
    GND     |    Rpi GND
    SCL     |    pin 1 (I2C PORT)
    SDA     |    pin 2 (I2C PORT)
                    ''')

        if self.device == "ultrasonic":
            print(f'''
{self.device} pin | GPIO port
"""""""""""""""""""""""
    VCC     |    Rpi VCC 
    GND     |    Rpi GND
    trigger |    6
    echo    |    5
                    ''')            
            
        
        



if __name__ == "__main__":
    pin = PIN_CONNECTION("bh1750")
    pin = PIN_CONNECTION("oled")