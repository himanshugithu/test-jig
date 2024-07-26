import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import RPi.GPIO as GPIO
import csv
from lib.I2C.I2C import *
import board
from lib.I2C.i2c_oled import I2C_OLED
from lib.I2C.BH1750 import BH1750
from lib.I2C.mlx90614 import MLX90614
from lib.GPIO.led import LEDController
from lib.GPIO.button import ButtonController
from lib.GPIO.dht import DHTSensor
from lib.GPIO.ultrasonic import UltrasonicSensor
from lib.GPIO.DS18B20 import DS18B20
from lib.PWM.fade import LedFader
from lib.PWM.rgb import RGBLED
from lib.PWM.servo import ServoMotor
from lib.SPI.spi_oled import SPI_OLED
from lib.ADC.pot import Pot
from lib.ADC.ldr import LDRSensor 
from lib.ADC.tds import TDS_Sensor
from lib.pin_details import PIN_CONNECTION
from lib.UART.PM_Sensor import SDS011

class MyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TEST-JIG GUI")
        self.root.configure(bg='black')  # Set the background color of the main window to black

        # Set the default size of the window
        self.width = 1200
        self.height = 800
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.attributes('-fullscreen', True)
        
        # Bind the Escape key to exit fullscreen mode
        self.root.bind("<Escape>", self.exit_fullscreen)
        # Bind Control-Q to close the application
        self.root.bind("<Control-q>", self.close_application)

        # Define button width and font size as class attributes
        self.button_width = 10
        self.button_font = ("Helvetica", 14)

        # Read protocol devices from CSV
        self.protocol_devices = self.read_protocol_devices()

        # Create frames
        self.create_logo_frame()
        self.create_protocol_frame()
        self.create_io_frame()
        self.create_control_frame()

        # Update date and time every second
        self.update_datetime()

        # Initialize device object
        self.current_device = None
        self.stop_flag = False

    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
    
    def close_application(self, event=None):
        self.root.quit()

    def read_protocol_devices(self):
        protocol_devices = {}
        with open('protocol_devices.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                protocol = row['Protocol']
                device = row['Device']
                if protocol in protocol_devices:
                    protocol_devices[protocol].append(device)
                else:
                    protocol_devices[protocol] = [device]
        return protocol_devices

    def create_logo_frame(self):
        # Create frame for logo, project name, date, and time
        self.logo_frame = tk.Frame(self.root, bg='black')
        self.logo_frame.pack(side="top", fill="x", padx=20, pady=20)

        # Logo image
        logo_path = "city.png"  # Replace with your logo image path
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((150, 100), Image.LANCZOS)  # Resize logo image as needed
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        # Create image label
        self.image_label = tk.Label(self.logo_frame, image=self.logo_photo, bg='black')
        self.image_label.pack(side="left", padx=(20, 0))

        # Project name label
        project_name_label = tk.Label(self.logo_frame, text="TEST-JIG", fg="white", bg="black", font=("Helvetica", 24))
        project_name_label.pack(side="left", padx=(250, 20))

        # Date and Time label
        self.datetime_label = tk.Label(self.logo_frame, text="", fg="white", bg="black", font=("Helvetica", 14))
        self.datetime_label.pack(side="right", padx=(0, 20))

    def update_datetime(self):
        # Update date and time label every second
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.datetime_label.config(text=dt_string)
        self.root.after(1000, self.update_datetime)

    def create_protocol_frame(self):
        # Create frame for protocols buttons
        self.protocol_frame = tk.Frame(self.root, bg='black')
        self.protocol_frame.pack(side="left", fill="y", padx=10, pady=20)

        # Add label above the buttons
        protocol_label = tk.Label(self.protocol_frame, text="PROTOCOLS", fg="white", bg="black", font=("Helvetica", 16))
        protocol_label.pack(pady=(0, 10))

        # Create buttons for protocols
        protocols = ["I2C", "SPI", "UART", "PWM", "GPIO", "ADC"]
        for protocol in protocols:
            button = tk.Button(self.protocol_frame, text=protocol, width=self.button_width, fg="white", bg="grey", font=self.button_font, anchor="center", command=lambda p=protocol: self.populate_dropdown(p))
            button.pack(pady=5, fill="x")

    def populate_dropdown(self, protocol):
        # Clear existing items in dropdown
        self.dropdown['values'] = ()

        # Populate dropdown with devices for the selected protocol
        if protocol in self.protocol_devices:
            devices = self.protocol_devices[protocol]
            self.dropdown['values'] = devices
            self.dropdown.set("Select Device")  # Set default text

    def on_device_selected(self, event):
        selected_device = self.dropdown.get()
        pin = PIN_CONNECTION(selected_device)
        self.print_to_output(pin.pin_connections)

    def create_io_frame(self):
        # Create frame for input and output boxes
        self.io_frame = tk.Frame(self.root, bg='black')
        self.io_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Input frame
        input_frame = tk.Frame(self.io_frame, bg='black')
        input_frame.pack(side="top", fill="x")

        # Input box
        self.input_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=50)
        self.input_entry.pack(side="left", padx=(0, 10))

        # Send button
        send_button = tk.Button(input_frame, text="Send", width=self.button_width, fg="black", bg="white", font=self.button_font, anchor="center", command=self.send_data)
        send_button.pack(side="left")

        # Frame for output box and scrollbar
        output_frame = tk.Frame(self.io_frame, bg='black')
        output_frame.pack(pady=5, fill="both", expand=True)

        # Scrollbar for the output box
        scrollbar = tk.Scrollbar(output_frame)
        scrollbar.pack(side="right", fill="y")

        # Output box (Text widget)
        output_width = 1  # Adjust width as needed
        output_height = 10  # Adjust height as needed
        self.output_text = tk.Text(output_frame, height=output_height, width=output_width, font=("Helvetica", 15), state='disabled', yscrollcommand=scrollbar.set)
        self.output_text.pack(side="left", fill="both", expand=True)

        # Configure scrollbar
        scrollbar.config(command=self.output_text.yview)

        # Clear button
        clear_button = tk.Button(self.io_frame, text="Clear", width=self.button_width, fg="black", bg="white", font=self.button_font, anchor="center", command=self.clear_output)
        clear_button.pack(pady=(10, 0))

        # Download Log button
        download_button = tk.Button(self.io_frame, text="Store Log", width=self.button_width, fg="black", bg="white", font=self.button_font, anchor="center", command=self.download_log)
        download_button.pack(pady=(10, 0))

    def create_control_frame(self):
        # Create frame for dropdown and control buttons
        self.control_frame = tk.Frame(self.root, bg='black')
        self.control_frame.pack(side="right", fill="y", padx=20, pady=20)

        # Add label above dropdown box
        dropdown_label = tk.Label(self.control_frame, text="OPTIONS", fg="white", bg="black", font=("Helvetica", 16))
        dropdown_label.pack(pady=(0, 10))

        # Dropdown box
        self.dropdown = ttk.Combobox(self.control_frame, font=("Helvetica", 14))
        self.dropdown.pack(pady=5)
        self.dropdown.bind("<<ComboboxSelected>>", self.on_device_selected)

        # Start and stop buttons
        self.stop_button = tk.Button(self.control_frame, text="Stop", width=self.button_width, fg="black", bg="white", font=self.button_font, anchor="center", command=self.toggle_stop)
        self.stop_button.pack(side="bottom", pady=(20, 10))

        self.start_button = tk.Button(self.control_frame, text="Start", width=self.button_width, fg="black", bg="white", font=self.button_font, anchor="center", command=self.toggle_start)
        self.start_button.pack(side="bottom", pady=(10, 20))

        # Track button state
        self.start_button_active = False
        self.stop_button_active = False

    def toggle_start(self):
        selected_device = self.dropdown.get()
        if not self.start_button_active:
            self.start_button.config(bg='green')
            self.start_button_active = True
            self.clear_output()
            self.stop_flag = False
            self.current_device = selected_device
            self.print_data_continuously()
        else:
            self.start_button.config(bg='white')
            self.start_button_active = False
            self.stop_flag = True

        if self.stop_button_active:
            self.stop_button.config(bg='white')
            self.stop_button_active = False

    def toggle_stop(self):
        self.stop_flag = True
        if not self.stop_button_active:
            self.stop_button.config(bg='red')
            self.stop_button_active = True
        else:
            self.stop_button.config(bg='white')
            self.stop_button_active = False

        if self.start_button_active:
            self.start_button.config(bg='white')
            self.start_button_active = False

    def print_data_continuously(self):
        if self.stop_flag:
            return

        if self.current_device:
            self.display_device_data(self.current_device)
        self.root.after(1000, self.print_data_continuously)  # Adjust the interval as needed

    def display_device_data(self, device):
        print(device)
        #/////////////////////////I2C///////////////////////
        if device == "OLED":
            # self.print_to_output("OLED running")
            oled = I2C_OLED()
            oled.activate_gui()
            self.print_to_output(oled.check_device())
        elif device == "BH1750":
            bh1750 = BH1750()
            sensor_data = bh1750.activate_gui()
            self.print_to_output(sensor_data)
        elif device == "MXL90614":
            mxl90614 =MLX90614()
            sensor_data = mxl90614.activate_gui()
            self.print_to_output(sensor_data)    

        #/////////////////////////GPIO///////////////////////   
        elif device == "led":
            led_controller = LEDController(5)
            led_controller.activate_gui() 

        elif device == "button":
            button_controller = ButtonController(button_pin=6)
            data=button_controller.activate_gui()
            self.print_to_output(data)    

        elif device == "DHT11":
            sensor = DHTSensor(pin=board.D13)
            data = sensor.activate_gui()
            self.print_to_output(data)

        elif device == "ultrasonic sensor":
            sensor = UltrasonicSensor(trigger_pin=26, echo_pin=19)
            data = sensor.activate_gui()
            self.print_to_output(data)

        elif device == "DS18B20":
            ds18b20 = DS18B20()
            data = ds18b20.activate_gui()
            self.print_to_output(data)    

        #/////////////////////////SPI///////////////////////    
        elif device == "SPI OLED":
            spi_oled = SPI_OLED() 
            spi_oled.activate_gui(image_path="/home/test-jig/main/lib/SPI/c.bmp")   

        #/////////////////////////PWM///////////////////////     
        
        elif device == "servo motor":
            servo_motor = ServoMotor()        
            servo_motor.activate_gui()

        elif device == "RGB led":
            rgb=RGBLED()
            rgb.activate_gui()

        #////////////////////////ADC////////////////////////////
        elif device == "Potentiometer":
            pot = Pot()
            data = pot.activate_gui()
            self.print_to_output(data)

        elif device == "ldr":
            ldr = LDRSensor()
            data= ldr.activate_gui()
            self.print_to_output(data) 

        elif device == "tds":
            tds = TDS_Sensor()
            data= tds.activate_gui()
            self.print_to_output(data)       

        #////////////////////////UART////////////////////////////
        elif device == "PM Sensor":
            sensor = SDS011()
            data= sensor.activate_gui()
            self.print_to_output(data)  

    def print_to_output(self, data):
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, f"{data}\n")
        self.output_text.config(state='disabled')
        self.output_text.yview(tk.END)  # Auto-scroll to the end

    def send_data(self):
        # Get input data and append to output box
        input_data = self.input_entry.get()
        if input_data:
            self.print_to_output(input_data)
            self.input_entry.delete(0, tk.END)  # Clear input box after sending data

    def clear_output(self):
        # Clear the output box
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state='disabled')

    def download_log(self):
        # Get the content of the output box
        log_content = self.output_text.get("1.0", tk.END).strip()
        if log_content:
            # Create a log file and save the content
            with open(f"{self.current_device} log.txt", "w") as log_file:
                log_file.write(log_content)
            self.clear_output()   
            self.print_to_output(f"Log saved as {self.current_device} log.txt")
            

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = MyGUI(root)
    root.mainloop()
