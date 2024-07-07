from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import Image, ImageFont
from time import sleep, time
import smbus

class I2C_OLED:
    def __init__(self, bus_number=1, oled_address=0x3C):
        self.bus_number = bus_number
        self.oled_address = oled_address
        self.bus = smbus.SMBus(bus_number)
        print("OLED initialized")
    
    def scan_oled(self):
        devices = []
        for address in range(0x03, 0x78):
            try:
                self.bus.write_quick(address)
                devices.append(f"OLED : {hex(address)}")
            except OSError:
                pass
        return devices

    def clear_display(self, device):
        """Clear the OLED display."""
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="black", fill="black")

    def activate(self, timeout=10, image_path=None):
        try:
            # Port type and address
            serial = i2c(port=self.bus_number, address=self.oled_address)
            
            # Device type
            device = sh1106(serial)
            
            start_time = time()  # Get current time
            while time() - start_time < timeout:
                if image_path:
                    # Load and display image
                    image = Image.open(image_path).convert("1")  # Convert to 1-bit color
                    with canvas(device) as draw:
                        draw.bitmap((0, 0), image, fill="white")
                else:
                    # Predefined font sizes
                    font_sizes = [42]
                    font_index = 0

                    # Get current font size
                    font_size = font_sizes[font_index]

                    # Load font with the current size
                    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", font_size)

                    # Draw text to display
                    with canvas(device) as draw:
                        draw.text((40, 10), "OK", font=font, fill="white")

                    # Move to the next font size
                    font_index = (font_index + 1) % len(font_sizes)

                # Sleep for 1 second before updating
                sleep(1)
        
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.clear_display(device)
            print("OLED display cleared and reset")

if __name__ == "__main__":
    manager = I2C_OLED()
    print(manager.scan_oled())
    manager.activate(timeout=10)