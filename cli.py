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
from lib.pin_details import PIN_CONNECTION
from lib.ADC.pot import Pot
from lib.ADC.ldr import LDRSensor
from lib.ADC.tds import TDS_Sensor
from lib.UART.PM_Sensor import SDS011
from lib.RS485.rsReceive import *
from lib.RS485.rsTransmitter import sendData
import sys
def switch_case(value):
    match value:
        case 1:#i2c
            device = int(input('''
                                    Choose Device : 
                                    1.BH1750
                                    2.OLED
                                    3.MLX90614
                                    Enter the Device : '''))
            match device:
                case 1:  #this is for the BH17501
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("BH1750")
                               print(pin.pin_connections)
                            case 2:
                                bh1750 = BH1750()
                                print(bh1750.activate_cli())
                            case 3:
                                break    
     
                case 2:# for the OLED
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. Pin Connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                pin = PIN_CONNECTION("OLED")
                                print(pin.pin_connections)
                            case 2:
                                while True:
                                    oled = I2C_OLED()
                                    status = oled.activate_cli()
                                    print(status)
                                    break
                            case 3:
                                break # this for the Oled 
                case 3:# for the MLX90614
                    
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. Pin Connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                pin = PIN_CONNECTION("MXL90614")
                                print(pin.pin_connections)
                            case 2:
                                while True:
                                    mxl90614 =MLX90614()
                                    mxl90614.activate_cli()
                                    break
                            case 3:
                                break # this for the Oled             
        case 2:#SPI
            device = int(input('''
                                    Choose Device : 
                                    1.SD Card MOdule
                                    2.OLED
                                    Enter the Device : '''))
            match device:
                case 1:  #sd card
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. Scan
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pass
                            case 2:
                                pass
                            case 3:
                                break    
     
                case 2:# for the OLED
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                pin = PIN_CONNECTION("SPI OLED")
                                print(pin.pin_connections)
                            case 2:
                               oled = SPI_OLED() 
                               oled.activate_cli(image_path="c.bmp")
                            case 3:
                                break # this for the Oled 
        case 3:#UART
            device = int(input('''
                                    Choose Device : 
                                    1.PM Sensor
                                    Enter the Device : '''))
            match device:
                case 1:  #this is for the pm sensor
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("PM Sensor")
                               print(pin.pin_connections)
                            case 2:
                                sensor = SDS011()
                                sensor.activate_cli()
                            case 3:
                                break
        case 4:#pwm
            device = int(input('''
                                        Choose Device : 
                                        1.LED(Fading)
                                        2.Servo Motor
                                        3.RGB LED
                                        Enter the Device : '''))
            match device:
                case 1:  #led fading
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                pin = PIN_CONNECTION("LED_FADE")
                                print(pin.pin_connections)
                            case 2:
                                    fader = LedFader(18)
                                    fader.activate_cli()
                            case 3:
                                break
                case 2:  #rbg
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                pin = PIN_CONNECTION("servo motor")
                                print(pin.pin_connections)
                            case 2:
                                    servo_motor = ServoMotor()
                                    servo_motor.activate_cli()
                            case 3:
                                break
                case 3:  #rbg
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                pin = PIN_CONNECTION("RGB led")
                                print(pin.pin_connections)
                            case 2:
                                rgb=RGBLED()
                                rgb.activate_cli()
                            case 3:
                                break             
        case 5:#ADC
            device = int(input('''
                                    Choose Device : 
                                    1.Pot
                                    2.tds
                                    3.ldr
                                    Enter the Device : '''))
            match device:
                case 1:  #this is for pot
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("Potentiometer")
                               print(pin.pin_connections)
                            case 2:
                                pot = Pot()
                                pot.activate_cli()

                                    
                            case 3:
                                break 
                case 2:  #this is for tds
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("tds")
                               print(pin.pin_connections)
                            case 2:
                                sensor = TDS_Sensor(channel=0)
                                sensor.activate_cli()
                                    
                            case 3:
                                break   
                case 3:  #this is for ldr
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("ldr")
                               print(pin.pin_connections)
                            case 2:
                                ldr_sensor = LDRSensor()
                                ldr_sensor.activate_cli()
                            case 3:
                                break                       
        case 6:#GPIO
            device = int(input('''
                                    Choose Device : 
                                    1.LED
                                    2.Button
                                    3.ultrasonic sensor
                                    4.DHT11
                                    5.DS18B20
                                    
                                
                                    Enter the Device : '''))
            match device:
                case 1: #LED
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("LED")
                               print(pin.pin_connections)
                            case 2:
                                led_controller = LEDController(5)
                                led_controller.activate_cli() 
                            case 3:  
                                break
                case 2:#BUTTON
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("BUTTON")
                               print(pin.pin_connections)
                            case 2:
                                button_controller = ButtonController(button_pin=6)
                                button_controller.activate_cli()
                            case 3:  
                                break
                case 3:#ultrasonic
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("ultrasonic sensor")
                               print(pin.pin_connections)
                            case 2:
                                sensor = UltrasonicSensor(trigger_pin=26, echo_pin=19)
                                sensor.activate_cli()
                            case 3:  
                                break 
                case 4:#dht11
                     while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("DHT11")
                               print(pin.pin_connections)
                            case 2:
                                sensor = DHTSensor(pin=board.D13)
                                print(sensor.activate_cli())
                            case 3:  
                                break 
                case 5:#DS18B20
                     while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pin = PIN_CONNECTION("DS18B20")
                               print(pin.pin_connections)
                            case 2:
                                sensor = DS18B20()
                                print(sensor.activate_cli())
                            case 3:  
                                break                             
        case 7:
            while True:
                device = int(input('''
                                    Choose Device : 
                                    1. Send Data
                                    2. Receive Data 
                                    3. Exit
                                    Enter the Device : '''))
                match device:
                    case 1:
                        client, slave_id = config()
                        while True:
                            read_modbus_values(client, slave_id)
                    case 2:
                        sendData()
                    case 3:
                        break
                    case _:
                        print("❌ Invalid choice. Please try again.")
                                   
            
        
        case _:
            return "Invalid case"

    



def main():
    print("\n...........................")
    print("    **** TEST-JIG ****")
    print("""''''''''''''''''''''''''''""")
    
    while True:
        try:
            choice = int(input('''
Choose Protocol:
                
    1. I2C 
    2. SPI
    3. UART    
    4. PWM
    5. ADC 
    6. GPIO
    7. RS485
    8. EXIT
    Enter your choice: ''').strip())

            if choice == 8:
                print("\nExiting program...")
                break
            elif 1 <= choice <= 7:
                switch_case(choice)
            else:
                print("\n❌ Invalid choice. Please try again.")

        except ValueError:
            print("\n❌ Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
