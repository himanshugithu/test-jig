from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from time import sleep, time
from PIL import ImageFont
import smbus

class OLED:
    def __init__(self, bus_number=1, oled_address=0x3C):
        self.bus_number = bus_number
        self.oled_address = oled_address
        self.bus = smbus.SMBus(bus_number)
        print("OLED")
    
    def scan_oled(self):
        devices = []
        for address in range(0x03, 0x78):
            try:
                self.bus.write_quick(address)
                devices.append(f"OLED : {hex(address)}")
            except OSError:
                pass
        return devices

    def activate(self, timeout=10):
        try:
            # Port type and address
            serial = i2c(port=self.bus_number, address=self.oled_address)
            
            # Device type
            device = sh1106(serial)
            
            # Predefined font sizes
            font_sizes = [16, 24, 32, 42]
            font_index = 0
            
            start_time = time()  # Get current time
            while time() - start_time < timeout:
                # Get current font size
                font_size = font_sizes[font_index]
                
                # Load font with the current size
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", font_size)
                
                # Draw to display
                with canvas(device) as draw:
                    draw.text((0, 25), "Hello", font=font, fill="white")
                
                # Move to the next font size
                font_index = (font_index + 1) % len(font_sizes)
                
                # Sleep for 1 second before updating
                sleep(1)
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    manager = OLED()
    print(manager.scan_oled())
    manager.activate(timeout=10)
