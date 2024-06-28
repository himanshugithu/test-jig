from I2C import *
import board
from lib.I2C.i2c_oled import I2C_OLED
from lib.I2C.BH1750 import BH1750
from lib.GPIO.led import LEDController
from lib.GPIO.button import ButtonController
from lib.GPIO.dht import DHTSensor
from lib.GPIO.ultrasonic import UltrasonicSensor
from lib.PWM.fade import LedFader
from lib.PWM.rgb import RGBLED
from lib.PWM.servo import ServoMotor
from lib.SPI.spi_oled import SPI_OLED
from lib.pin_details import PIN_CONNECTION
def switch_case(value):
    match value:
        case 1:#i2c
            device = int(input('''
                                    Choose Device : 
                                    1.BH1750
                                    2.OLED
                                    Enter the Device : '''))
            match device:
                case 1:  #this is for the BH17501
                    while True:
                        choice = int(input('''
                                    Choose an I2C operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               PIN_CONNECTION("bh1750")
                            case 2:
                                bh1750 = BH1750()
                                print(bh1750.read_bh1750())
                            case 3:
                                break    
     
                case 2:# for the OLED
                    
                    while True:
                        choice = int(input('''
                                    Choose an I2C operation:
                                    1. Pin Connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                PIN_CONNECTION("oled")
                            case 2:
                                oled = I2C_OLED()
                                oled.activate(timeout=10)
                            case 3:
                                break # this for the Oled 
        case 2:#SPI
            device = int(input('''
                                    Choose Device : 
                                    1.SD Card MOdule
                                    2.OLED
                                    Enter the Device : '''))
            match device:
                case 1:  
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
                                    1. pin connection2
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                PIN_CONNECTION("spi_oled")
                            case 2:
                                spi_oled = SPI_OLED() 
                                spi_oled.activate(timeout=10,image_path="c.bmp")
                            case 3:
                                break # this for the Oled 
        case 3:#UART
            pass  
        case 4:#pwm
            device = int(input('''
                                        Choose Device : 
                                        1.LED(Fading)
                                        2.Servo Motor
                                        3.RGB LED
                                        Enter the Device : '''))
            match device:
                case 1:  #rbg
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                PIN_CONNECTION("led")
                            case 2:
                                    fader = LedFader(18)
                                    fader.start_fading()
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
                                PIN_CONNECTION("servo")
                            case 2:
                                    servo_motor = ServoMotor()
                                    servo_motor.init_servo()
                                    servo_motor.rotate_180()
                                    servo_motor.cleanup_servo()
                            case 3:
                                break
                case 3:  #rbg
                    while True:
                        choice = int(input('''
                                    Choose an I2C operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                                PIN_CONNECTION("rgb")
                            case 2:
                                rgb=RGBLED()
                                rgb.Activate()
                            case 3:
                                break             
        case 5:#ADC
            pass
        case 6:#GPIO
            device = int(input('''
                                    Choose Device : 
                                    1.LED
                                    2.Button
                                    3.ultrasonic sensor
                                    4.DHT11
                                    
                                
                                    Enter the Device : '''))
            match device:
                case 1: 
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               PIN_CONNECTION("led")
                            case 2:
                                led_controller = LEDController(5)
                                led_controller.Activate(interval=1, duration=10) 
                            case 3:  
                                break

                case 2:
                    while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               PIN_CONNECTION("button")
                            case 2:
                                button_controller = ButtonController(button_pin=6)
                                button_controller.Activate()
                            case 3:  
                                break

                case 3:#ultrasonic
                    while True:
                        choice = int(input('''
                                    Choose an I2C operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               PIN_CONNECTION("ultrasonic")
                            case 2:
                                sensor = UltrasonicSensor(trigger_pin=26, echo_pin=19)
                                sensor.activate()
                            case 3:  
                                break 
                        

                case 4:
                     while True:
                        choice = int(input('''
                                    Choose an operation:
                                    1. pin connection
                                    2. Test
                                    3. Exit
                                    Enter your choice: '''))
                        match choice:
                            case 1:
                               PIN_CONNECTION("dht11")
                            case 2:
                                sensor = DHTSensor(pin=board.D13)
                                sensor.Activate()
                            case 3:  
                                break          
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
    
