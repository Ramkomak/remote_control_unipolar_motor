from machine import Pin, UART
import time
import sys

controlTab1 = [0, 1, 1, 0]
controlTab2 = [1, 1, 0, 0]
controlTab3 = [1, 0, 0, 1]
controlTab4 = [0, 0, 1, 1]


class Engine:
    def __init__(self):
        self.initPins()
        self.direction = 1
        self.speed = 0.06
        self.on = 1

    def initPins(self):
        self.A_plus = Pin(2, Pin.OUT)
        self.A_minus = Pin(3, Pin.OUT)
        self.B_plus = Pin(4, Pin.OUT)
        self.B_minus = Pin(5, Pin.OUT)

    def rotate(self):
        if self.on:
            for i in range(0, 3):
                if self.direction:
                    self.A_plus.value(controlTab1[i])
                    self.B_plus.value(controlTab2[i])
                    self.A_minus.value(controlTab3[i])
                    self.B_minus.value(controlTab4[i])
                else:
                    self.A_plus.value(controlTab1[i])
                    self.B_plus.value(controlTab4[i])
                    self.A_minus.value(controlTab3[i])
                    self.B_minus.value(controlTab2[i])
                time.sleep(self.speed)
    def changeSpeed(self, op):
        self.speed = op * 0.015
        print('speedMod')
        
    def changeDirection(self, op):
        if op:
            self.direction = 1
            print('left')
        else:
            self.direction = 0
            print('right')
    def startStop(self):
        if self.on:
            self.on = 0
            print('stop')
        else:
            self.on = 1
            print('start')
                
        
silnik = Engine()

def uartActions(option):
    if option == b's':
        value = int(uart.read(1))
        silnik.changeSpeed(value)    
    if option == b'o':
        silnik.startStop()
    if option == b'l':
        silnik.changeDirection(1)
    if option == b'r':
        silnik.changeDirection(0)
    





uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
try:
    while 1:
        silnik.rotate()
        if uart.any():
            uartActions(uart.read(1))
            uart.write('%d,%1.2f\n'%(silnik.direction,silnik.speed))
            
        

except KeyboardInterrupt:
    sys.exit()
