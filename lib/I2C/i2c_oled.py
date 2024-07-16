from smbus import SMBus
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep
import luma.core.error

class I2C_OLED:
    def __init__(self, bus_number=1, oled_address=0x3C):
        self.bus_number = bus_number
        self.oled_address = oled_address
        self.bus = SMBus(bus_number)
        self.device_present = False
        self.check_device()

    def check_device(self):
        """Check if the I2C device is present."""
        try:
            self.bus.write_quick(self.oled_address)
            self.device_present = True
            return(f"I2C device at address 0x{self.oled_address:02X} found.")
        except OSError:
            return(f"I2C device at address 0x{self.oled_address:02X} not found.")
    
    def clear_display(self):
        """Clear the OLED display."""
        if self.device_present:
            try:
                self.bus.write_byte(self.oled_address, 0x00)  # Example write operation to clear the display
            except OSError:
                print(f"Error: Failed to communicate with I2C device at address 0x{self.oled_address:02X}.")

    def activate_gui(self):
        if not self.device_present:
            return "I2C device not detected. Cannot activate OLED."
        
        try:
            serial = i2c(port=self.bus_number, address=self.oled_address)
            device = sh1106(serial)
            font_size = 42
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", font_size)
            with canvas(device) as draw:
                draw.text((40, 10), "OK", font=font, fill="white")
            sleep(1)
        
        except luma.core.error.DeviceNotFoundError as e:
            print(f"An error occurred: {e}")
            return f"An error occurred: {e}"
        
        finally:
            self.clear_display()

    def activate_cli(self):
        if not self.device_present:
            return "I2C device not detected. Cannot activate OLED."
        while True:
            try:
                serial = i2c(port=self.bus_number, address=self.oled_address)
                device = sh1106(serial)
                font_size = 42
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", font_size)
                with canvas(device) as draw:
                    draw.text((40, 10), "OK", font=font, fill="white")
                sleep(1)
            
            except luma.core.error.DeviceNotFoundError as e:
                print(f"An error occurred: {e}")
                return f"An error occurred: {e}"
            
            finally:
                self.clear_display()    
if __name__ == "__main__":
    manager = I2C_OLED()

    # Example: continuously attempt to activate OLED
    while True:
        manager.activate()
        sleep(3)  # Add a delay before reactivating the OLED
