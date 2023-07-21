import machine
import utime
from time import sleep
from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
from rpiPicoSegDisplay import SegDisplay

# LCD
i2c = I2C(1, sda=Pin(26), scl=Pin(27), freq=400000) 
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2 ,16)

# alarm components
sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_alert = machine.Pin(9, machine.Pin.OUT)
led_warning = machine.Pin(8, machine.Pin.OUT)
buzzer = machine.Pin(7, machine.Pin.OUT)

# how much time is there until the alarm is fully active
def countdown():
    SegDisplay("9")
    sleep(1)
    SegDisplay("8")
    sleep(1)
    SegDisplay("7")
    sleep(1)
    SegDisplay("6")
    sleep(1)
    SegDisplay("5")
    sleep(1)
    SegDisplay("4")
    sleep(1)
    SegDisplay("3")
    sleep(1)
    SegDisplay("2")
    sleep(1)
    SegDisplay("1")
    sleep(1)
    SegDisplay("0")
 
# pauses the program and reacts whenever the sensor is triggered
def pir_handler(pin): 
    utime.sleep_ms(100)
    if pin.value():
        lcd.putstr("INTRUDER ALERT!")
        led_warning.value(0)
        for i in range(50):
            led_alert.toggle()
            buzzer.toggle()
            utime.sleep_ms(100)
        lcd.clear()
        led_warning.value(1)
        
# how the alarm works            
def alarm():
    print("The alarm will turn on soon.")
    countdown()
    print("The alarm is on.")
    led_warning.value(1)
    sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

# the alarm system
def system():
    done = False
    print("""
        Welcome to the Raspberry Pi Pico Alarm System!
        A simple alarm system meant to detect intruders and make them think twice before stealing your items.
        You'll need to enter a passcode to both activate the alarm and turn it off.
        """)
    
    while done == False:        
        command = input("To create a new passcode, press (N). To enter your old passcode, press (E). To exit the system, press (Q): ")       
        if command == 'N':
            alert = True
            while alert == True:
                new_passcode = int(input("Please enter your new passcode: "))
                if new_passcode:
                    alarm()
                    off = int(input("To turn off the alarm, re-enter the passcode: "))
                    if off == new_passcode:
                        print("The alarm is off.")
                        alert = False
                        sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=None) # how the alarm turns off
                        led_warning.value(0)
                    else:
                        print("Incorrect passcode. Please try again.")
                                      
        elif command == 'E':
            alert = True
            while alert == True:
                old_passcode = int(input("Please enter the passcode: "))
                if old_passcode == new_passcode:
                    alarm()
                    off = int(input("To turn off the alarm, re-enter the passcode: "))
                    if off == old_passcode:
                        print("The alarm is off.")
                        alert = False
                        sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=None) # how the alarm turns off
                        led_warning.value(0)
                    else:
                        print("Incorrect passcode. Please try again.")
                else:
                    print("Incorrect passcode. Please try again.")
                        
        elif command == 'Q':
            print("""
               Thank you for using the Raspberry Pi Pico Alarm System!
               Until next time!
               """)
            done = True
            
        else:
            print("Invalid input. Please try again.")
                  
system()
