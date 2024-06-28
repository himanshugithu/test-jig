import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import csv

class MyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Four Frame GUI")
        self.root.configure(bg='black')  # Set the background color of the main window to black

        # Set the default size of the window
        self.width = 1200
        self.height = 800
        self.root.geometry(f"{self.width}x{self.height}")

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
        project_name_label.pack(side="left", padx=(340, 20))

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
        self.protocol_frame.pack(side="left", fill="y", padx=20, pady=100)

        # Add label above the buttons
        protocol_label = tk.Label(self.protocol_frame, text="PROTOCOLS", fg="white", bg="black", font=("Helvetica", 16))
        protocol_label.pack(pady=(0, 10))

        # Create buttons for protocols
        protocols = ["I2C", "SPI", "UART", "PWM", "GPIO", "ADC"]
        for protocol in protocols:
            button = tk.Button(self.protocol_frame, text=protocol, width=self.button_width, fg="white", bg="grey", font=self.button_font, anchor="center", command=lambda p=protocol: self.populate_dropdown(p))
            button.pack(pady=5)

    def populate_dropdown(self, protocol):
        # Clear existing items in dropdown
        self.dropdown['values'] = ()

        # Populate dropdown with devices for the selected protocol
        if protocol in self.protocol_devices:
            devices = self.protocol_devices[protocol]
            self.dropdown['values'] = devices
            self.dropdown.set("Select a Device")  # Set default text

    def create_io_frame(self):
        # Create frame for input and output boxes
        self.io_frame = tk.Frame(self.root, bg='black')
        self.io_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # Input frame
        input_frame = tk.Frame(self.io_frame, bg='black')
        input_frame.pack(side="top", fill="x")

        # Input box
        self.input_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=50)
        self.input_entry.pack(side="left", padx=(0, 10))

        # Send button
        send_button = tk.Button(input_frame, text="Send", width=self.button_width, fg="black", bg="white", font=self.button_font, anchor="center", command=self.send_data)
        send_button.pack(side="left")

        # Output box (Text widget)
        output_width = 20  # Adjust width as needed
        output_height = 10  # Adjust height as needed
        self.output_text = tk.Text(self.io_frame, height=output_height, width=output_width, font=("Helvetica", 12), state='disabled')
        self.output_text.pack(pady=5, fill="both", expand=True)

        # Clear button
        clear_button = tk.Button(self.io_frame, text="Clear", width=self.button_width, fg="black", bg="white", font=self.button_font, anchor="center", command=self.clear_output)
        clear_button.pack(pady=(10, 0))

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

        # Start and stop buttons
        self.stop_button = tk.Button(self.control_frame, text="Stop", width=self.button_width, fg="black", bg="white", font=self.button_font, anchor="center", command=self.toggle_stop)
        self.stop_button.pack(side="bottom", pady=(20, 10))

        self.start_button = tk.Button(self.control_frame, text="Start", width=self.button_width, fg="black", bg="white", font=self.button_font, anchor="center", command=self.toggle_start)
        self.start_button.pack(side="bottom", pady=(10, 20))

        # Track button state
        self.start_button_active = False
        self.stop_button_active = False

    def toggle_start(self):
        if not self.start_button_active:
            self.start_button.config(bg='green')
            self.start_button_active = True
        else:
            self.start_button.config(bg='white')
            self.start_button_active = False

        if self.stop_button_active:
            self.stop_button.config(bg='white')
            self.stop_button_active = False

    def toggle_stop(self):
        if not self.stop_button_active:
            self.stop_button.config(bg='red')
            self.stop_button_active = True
        else:
            self.stop_button.config(bg='white')
            self.stop_button_active = False

        if self.start_button_active:
            self.start_button.config(bg='white')
            self.start_button_active = False

    def on_enter_start(self, event):
        self.start_button.config(bg='green')

    def on_leave_start(self, event):
        if not self.start_button_active:
            self.start_button.config(bg='white')

    def on_enter_stop(self, event):
        self.stop_button.config(bg='red')

    def on_leave_stop(self, event):
        if not self.stop_button_active:
            self.stop_button.config(bg='white')

    def send_data(self):
        # Get input data and append to output box
        input_data = self.input_entry.get()
        if input_data:
            self.output_text.config(state='normal')
            self.output_text.insert(tk.END, f"{input_data}\n")
            self.output_text.config(state='disabled')
            self.input_entry.delete(0, tk.END)  # Clear input box after sending data

    def clear_output(self):
        # Clear the output box
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = MyGUI(root)
    root.mainloop()
