from luma.core.interface.serial import spi
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont, Image
import time

class SPI_OLED:
    def __init__(self, protocol='spi', spi_port=0, spi_device=0, gpio_DC=22, gpio_RST=27, gpio_CS=8):
        self.protocol = protocol
        self.spi_port = spi_port
        self.spi_device = spi_device
        self.gpio_DC = gpio_DC
        self.gpio_RST = gpio_RST
        self.gpio_CS = gpio_CS
        
        print("OLED initialized with protocol:", protocol)

    def clear_display(self, device):
        """Clear the OLED display."""
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="black", fill="black")

    def activate_gui(self, timeout=10, image_path=None):
        try:
            # Initialize based on the protocol
            if self.protocol == 'spi':
                serial = spi(port=self.spi_port, device=self.spi_device, gpio_DC=self.gpio_DC, gpio_RST=self.gpio_RST, gpio_CS=self.gpio_CS)
            else:
                raise ValueError("This code currently only supports SPI protocol for OLED.")
            device = sh1106(serial)
            
            if image_path:
                image = Image.open(image_path).convert("1")  # Convert to 1-bit color
                with canvas(device) as draw:
                    draw.bitmap((0, 0), image, fill="white")
                time.sleep(2)
            # else:
            #     # Predefined font sizes
            #     font_sizes = [16, 24, 32, 42]
            #     font_index = 0 
            #         # Get current font size
            #     font_size = font_sizes[font_index]
            #     # Load font with the current size
            #     font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", font_size)
            #     # Draw to display
            #     with canvas(device) as draw:
            #         draw.text((0, 25), "Hello", font=font, fill="white")
                
            #     # Move to the next font size
            #     font_index = (font_index + 1) % len(font_sizes)
                
            #     # Sleep for 1 second before updating
            #     time.sleep(1)
        
        except KeyboardInterrupt:
            print("Process interrupted by user")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.clear_display(device)
            print("OLED display cleared and reset")

    def activate_cli(self,image_path=None):
        try:
            while True:    
                try:
                    if self.protocol == 'spi':
                        serial = spi(port=self.spi_port, device=self.spi_device, gpio_DC=self.gpio_DC, gpio_RST=self.gpio_RST, gpio_CS=self.gpio_CS)
                    else:
                        raise ValueError("This code currently only supports SPI protocol for OLED.")
                    device = sh1106(serial)
                    image = Image.open(image_path).convert("1") 
                    with canvas(device) as draw:
                        draw.bitmap((0, 0), image, fill="white")
                    time.sleep(1)
                except Exception as e:
                    print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("Process interrupted by user")            
        finally:
            self.clear_display(device)
            print("OLED display cleared and reset")

if __name__ == "__main__":
    manager = SPI_OLED() 
    manager.activate(timeout=10,image_path="c.bmp")  # You can provide a path to an image file
