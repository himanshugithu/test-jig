import time
from I2C import *
import board
from lib.I2C.oled import OLED
from lib.I2C.BH1750 import BH1750
from lib.GPIO.led import LEDController
from lib.GPIO.button import ButtonController
from lib.GPIO.dht import DHTSensor
from lib.GPIO.ultrasonic import UltrasonicSensor
from lib.PWM.rgb import RGBLED
from lib.PWM.servo import ServoMotor

def switch_case(value):
    match value:
        case 1:#i2c
            bus = smbus.SMBus(1)
            devices = []
            for address in range(0x03, 0x78):
                try:
                    bus.write_quick(address)
                    # devices.append("oled :")
                    devices.append(hex(address))
                except OSError:
                    pass
            print(f"\nI2C address found is {devices}")

            device = int(input('''
                                    Choose Device : 
                                    1.BH1750
                                    2.OLED
                                    Enter the Device : '''))
            match device:
                case 1:  #this is for the BH1750
                    while True:
                        choice = int(input('''
                                    Choose an I2C operation:
                                    1. Scan
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               pass
                            case 2:
                                bh1750 = BH1750()
                                print(bh1750.read_bh1750())
                            case 3:
                                break    
     
                case 2:# for the OLED
                    while True:
                        choice = int(input('''
                                    Choose an I2C operation:
                                    1. Scan
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                pass
                            case 2:
                                oled = OLED()
                                oled.activate(timeout=10)
                            case 3:
                                break # this for the Oled 
        case 2:#SPI

            while True:
                choice = int(input('''
                                    Choose an SPI operation:
                                    1. Scan
                                    2. Test
                                    0. Exit
                                    Enter your choice: ''')) 
                match choice:
                    case 1:
                        print("| Scanning SPI devices |")
                    case 2:
                        print("Test SPI device")
                    case 3:
                        print("Exiting...")
                        break
                    case _:
                        print("Invalid choice, please try again.")
        case 3:#UART
            pass  
        case 4:#pwm
            while True:
                device = int(input('''
                                        Choose Device : 
                                        1.LED(Fading)
                                        2.Servo Motor
                                        3.RGB LED
                                        Enter the Device : '''))
                match device:
                    case 1:  #led fading
                        pass    
                    case 2:  #servo motor
                        servo = ServoMotor()
                        servo.Activate()    
                    case 3:
                        rgb=RGBLED()
                        rgb.Activate()            
        case 5:#ADC
            pass
        case 6:#GPIO
            device = int(input('''
                                    Choose Device : 
                                    1.LED
                                    2.Button
                                    3.ultrasonic sensor
                                    4.IR sensor
                                    5.DHT11
                                
                                    Enter the Device : '''))
            match device:
                case 1: 
                    led_controller = LEDController(6)
                    led_controller.Activate(interval=1, duration=10) 

                case 2:
                    button_controller = ButtonController(button_pin=5)
                    button_controller.Activate()

                case 3:#ultrasonic
                    sensor = UltrasonicSensor(trigger_pin=26, echo_pin=19)
                    sensor.activate()
                        

                case 5:
                    sensor = DHTSensor(pin=board.D13)
                    sensor.Activate()
                    
        case _:
            return "Invalid case"




def main():
    print("\n...........................")
    print("    **** TEST-JIG ****")
    print("""''''''''''''''''''''''''''""")
    while True:
        choice = int(input('''
        Choose Protocal:
                        
            1. I2C 
            2. SPI
            3. UART    
            4. PWM
            5. ADC 
            6. GPIO
            Enter your choice: '''))
        result = switch_case(choice)


if __name__ == "__main__":
    main()        
    
