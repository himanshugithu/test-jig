import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

def config():
    # Select Baud Rate
    baud_rate_choices = {1: 9600, 2: 115200}
    baud_choice = int(input('''Baud Rate:
    1. 9600
    2. 115200
        Choose Baud Rate: ''').strip())
    baud_rate = baud_rate_choices.get(baud_choice, 9600)

    # Select Parity
    parity_choices = {1: 'E', 2: 'N', 3: 'O'}
    parity_choice = int(input('''\nParity Bit:
    1. E (Even)
    2. N (None)
    3. O (Odd)
        Choose Parity Bit: ''').strip())
    parity = parity_choices.get(parity_choice, 'E')

    # Enter Slave ID
    try:
        slave_id = int(input("\nEnter the Slave ID: ").strip())
    except ValueError:
        print("❌ Invalid Slave ID. Defaulting to 1.")
        slave_id = 1

    # Create Modbus Client
    client = ModbusClient(
        method='rtu',
        port="/dev/ttyUSB0",
        baudrate=baud_rate,
        parity=parity,
        stopbits=1,
        bytesize=8,
        timeout=1
    )

    if not client.connect():
        print("❌ Failed to open serial port. Check USB and permissions.")
        exit(1)
    else:
        print("✅ Connected successfully.")
    
    return client, slave_id
  
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

def read_modbus_values(client, slave_id):
    try:
        while True:
            try:
                addr = int(input("\nEnter the register address to fetch data from: ").strip())
            except ValueError:
                print("❌ Invalid register number. Please enter a valid number.")
                continue  # Prompt again if the input is not a number

            rr = client.read_holding_registers(address=addr, count=2, unit=slave_id)
            if rr.isError():
                print(f"❌ Error while fetching data from register {addr}")
                continue  # Prompt again if there's an error
            
            regs = rr.registers
            decoder = BinaryPayloadDecoder.fromRegisters(
                regs,
                byteorder=Endian.Big,     # bytes are big-endian
                wordorder=Endian.Little   # words are swapped
            )
            value = round(decoder.decode_32bit_float(), 3)
            print(f"\nRegister {addr}: {value}")

    except KeyboardInterrupt:
        print("\n\nExiting register reader. Goodbye! 👋")

    

if __name__ == "__main__":


    meter_ids = [1]
    for mid in meter_ids:
        print(f"\nReading Meter #{mid}")
        data = read_modbus_values(mid, client)
        for name, val in data.items():
            print(f"  {name:10s}: {val}")
        time.sleep(0.2)   # small pause

    client.close()
    print("\nAll done.")
