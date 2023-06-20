from machine import Pin, UART
import time
import sys

controlTab1 = [0, 1, 1, 0]
controlTab2 = [1, 1, 0, 0]
controlTab3 = [1, 0, 0, 1]
controlTab4 = [0, 0, 1, 1]
left = 1
right = 0


class Engine:
    def __init__(self):
        self.initPins()
        self.direction = left

    def initPins(self):
        self.A_plus = Pin(2, Pin.OUT)
        self.A_minus = Pin(3, Pin.OUT)
        self.B_plus = Pin(4, Pin.OUT)
        self.B_minus = Pin(5, Pin.OUT)

    def rotate(self):
        i = 0
        while 1:
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
            time.sleep(0.01)
            i = i + 1
            if i > 4:
                i = 0

silnik = Engine()
uart = UART(1, baudrate=9600, tx=Pin(0), rx=Pin(1))
try:
    while 1:
        uart.irq(UART.RX_ANY, priority=1, handler=print('Uart callback!'), wake=machine.IDLE)
        silnik.rotate()

except KeyboardInterrupt:
    sys.exit()