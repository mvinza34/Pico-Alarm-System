# Pico-Alarm-System

### Overview
This simple alarm system features 2 LEDs, a PIR sensor, an LCD display, a buzzer, and a 7-segment display that acts as a countdown timer; all done on the Raspberry Pi Pico. 

Credit for the "rpiPicoSegDisplay.py" code goes to peppe8o and can be found at https://peppe8o.com/7-segment-display-and-raspberry-pi-pico-wiring-and-setup-with-micropython/

Credit for the "lcd_api.py" and "pico_l2c_lcd.py" programs goes to Tom's Hardware and can be found at https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico

![PXL_20230721_201701636 33477](https://github.com/mvinza34/Pico-Alarm-System/assets/89809703/60a1b7fc-12b3-448f-9a2a-9b8320fb9fc7)
![PXL_20230721_201757947 33478](https://github.com/mvinza34/Pico-Alarm-System/assets/89809703/5cefb855-cd94-4596-a398-5f85d585abb4)
![PXL_20230721_202017080 33479](https://github.com/mvinza34/Pico-Alarm-System/assets/89809703/8b974964-eaa2-44f0-b9d2-7d81ef4abd6a)
![PXL_20230721_202223045 33476](https://github.com/mvinza34/Pico-Alarm-System/assets/89809703/7ca31916-11d8-48f6-90ee-6453a8575c8a)

### Components
1) 1 Raspberry Pi Pico
2) 1 solderless breadboard
3) 1 solderless mini-breadboard
4) 2 LEDs (1 red, 1 green)
5) 8 220 Ω resistors
6) 2 330 Ω resistors
7) 1 active buzzer
8) 1 I2C LCD 1602
9) 1 PIR sensor
10) 1 7-segment-display

### Instructions
1) Design the circuit based on the provided breadboard image and schematic below:
   
![Pico_Alarm_System_bb](https://github.com/mvinza34/Pico-Alarm-System/assets/89809703/d9319415-dfe3-442e-81f8-70bb9997113e)
![Pico_Alarm_System_schem](https://github.com/mvinza34/Pico-Alarm-System/assets/89809703/64641c32-b0a7-4ca6-97f0-7a15de9e776e)
   
3) Download and install Thonny. (https://thonny.org/)
4) Open Thonny and install Micropython on the Pico.
5) Copy the files in this repository to the Pico.
6) Open Pico_Alarm_System.py
7) Run the code.
8) Sleep soundly knowing your items will be safe from intruders.
