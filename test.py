#!/usr/bin/env python3
import sys
import logging
from pymodbus.server.sync import StartSerialServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext, ModbusSparseDataBlock
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian

# Configure logging to show only errors
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.ERROR)

# Basic configuration for Modbus server

def configure_modbus():
    # Baud Rate selection
    baud_rate_choices = {1: 9600, 2: 115200}
    baud_choice = int(input('''Baud Rate:
    1. 9600
    2. 115200
Choose Baud Rate: ''').strip())
    baud_rate = baud_rate_choices.get(baud_choice, 9600)

    # Parity selection
    parity_choices = {1: 'E', 2: 'N', 3: 'O'}
    parity_choice = int(input('''Parity Bit:
    1. E (Even)
    2. N (None)
    3. O (Odd)
Choose Parity Bit: ''').strip())
    parity = parity_choices.get(parity_choice, 'E')

    # Slave ID selection
    slave_id = int(input("Enter the Slave ID: ").strip())

    print("✅ Configuration complete. Starting server...")
    return baud_rate, parity, slave_id


def build_registers(count_mode, data_type, register_address, values):
    builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
    for value in values:
        if count_mode == 1 and data_type == 'uint':
            builder.add_16bit_uint(int(value))
        elif count_mode == 2:
            if data_type == 'float':
                builder.add_32bit_float(value)
            elif data_type == 'long':
                builder.add_32bit_int(int(value))
            else:
                print("❌ Unsupported combination of count mode and data type.")
                sys.exit(1)
        else:
            print("❌ Unsupported combination of count mode and data type.")
            sys.exit(1)
    return builder.to_registers()


def start_modbus_server(context, baud_rate, parity):
    StartSerialServer(
        context,
        framer=ModbusRtuFramer,
        port="/dev/ttyUSB0",
        baudrate=baud_rate,
        parity=parity,
        stopbits=1,
        bytesize=8,
        method='rtu'
    )


def main():
    baud_rate, parity, slave_id = configure_modbus()

    # Count Mode
    count_mode = int(input('''Count Mode:
    1. Single Register (16-bit)
    2. Double Register (32-bit)
Choose Count Mode: ''').strip())

    # Data Type
    data_type = input('''Data Type:
    float - 32-bit Float
    long  - 32-bit Integer
    uint  - 16-bit Unsigned Integer
Choose Data Type: ''').strip()

    # Register Address
    register_address = int(input("Enter the starting register address: ").strip())

    # Sample data
    sample_values = [220.0, 120.0, 50.0, 115.0]  # Replace with actual values if needed
    registers = build_registers(count_mode, data_type, register_address, sample_values)

    # Prepare context
    data_block = {register_address + i: reg for i, reg in enumerate(registers)}
    slave_ctx = ModbusSlaveContext(hr=ModbusSparseDataBlock(data_block))
    context = ModbusServerContext(slaves={slave_id: slave_ctx}, single=False)

    print(f"✅ Modbus server ready. Serving data at registers starting from {register_address}")
    start_modbus_server(context, baud_rate, parity)


if __name__ == '__main__':
    main()

