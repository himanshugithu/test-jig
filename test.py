import serial
import time

# Initialize UART communication on Raspberry Pi
try:
    uart = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)
    print("Serial port opened successfully.")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)

def read_distance():
    try:
        # Send the command to the JSN-SR04T sensor to measure distance
        command = b'\x55'  # Example command, adjust based on your sensor's documentation
        print(f"Sending command: {command}")
        uart.write(command)
        time.sleep(0.1)  # Wait for the sensor to respond

        # Read the response from the sensor
        response = uart.read(4)  # Adjust based on expected response length
        print(f"Raw response: {response}")

        if len(response) == 4:
            # Example response handling: assuming response format 0xFF 0xXX 0xYY 0xZZ
            distance = (response[1] << 8) + response[2]  # Combine bytes for distance
            return distance
        else:
            print("Invalid response length")
            return None
    except ValueError:
        # Handle any errors in reading the distance
        print("Error reading distance: Could not convert to float")
        return None
    except serial.SerialException as e:
        print(f"Serial exception: {e}")
        return None

def main():
    while True:
        distance = read_distance()
        if distance is not None:
            print(f"Distance: {distance} cm")
        else:
            print("Failed to read distance")
        time.sleep(1)  # Adjust the delay as necessary

if __name__ == "__main__":
    main()
