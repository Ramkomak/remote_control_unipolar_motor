import sys
import glob
import serial
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QSlider, QLCDNumber, QSplitter, QHBoxLayout, QGroupBox,QRadioButton,QGridLayout, QListWidget, QLabel
from PyQt5.QtCore import Qt
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Sterowanie silnikiem krokowym unipolarnym'
        self.left = 0 # odległośc od lewej krawędzi ekranu w pixelach
        self.top = 0 # odległośc od górnej krawędzi ekranu w pixelach
        self.width = 400 # szerokośc okna
        self.height = 300 # wysokość okna
        self.availablePorts = []
        self.option = 0
        self.listOfActions = [b'l', #obroty w lewo 0
                              b'r', #obroty w prawo 1
                              b'o', #start/stop 2
                              ]
        self.listOfSpeeds = [b's0', #nieuzywany
                             b's4', #najwolniej
                             b's3',
                             b's2',
                             b's1', #najszybciej
                             ]
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) ############### # Tu w kolejnych zadaniach będziemy dodwać przycisk typu QPushButton, Slot oraz QLineEdit ###############
        self.center()
        self.interface()

    def interface(self):
        self.suwak = QSlider(Qt.Horizontal)
        self.suwak.setMinimum(1)
        self.suwak.setMaximum(4)
        self.suwak.setTickPosition(QSlider.TicksBothSides)
        self.suwak.setTickInterval(1)
        self.suwak.setSingleStep(1)
        self.suwak.valueChanged.connect(self.speedControl)


        self.start = QPushButton('&Start/Stop',self)
        self.connect = QPushButton('&Refresh',self)
        self.left = QPushButton('&Left',self)
        self.right = QPushButton('&Right',self)

        self.porty = QListWidget(self)

        self.connect.clicked.connect(self.insertList)
        self.left.clicked.connect(self.leftDir)
        self.start.clicked.connect(self.startStop)
        self.right.clicked.connect(self.rightDir)

        self.one = QLabel(self)
        self.one.setText('1')
        self.two = QLabel(self)
        self.two.setText('2')
        self.three = QLabel(self)
        self.three.setText('3')
        self.four = QLabel(self)
        self.four.setText('4')



        ukladH2 = QGridLayout()
        ukladH2.addWidget(self.suwak,2,0,1,3)
        ukladH2.addWidget(self.start,3,0,1,1)
        ukladH2.addWidget(self.connect,0,0)
        ukladH2.addWidget(self.left,3,1,1,1)
        ukladH2.addWidget(self.right,3,2,1,1)
        ukladH2.addWidget(self.porty,0,1,1,2)
        ukladH2.addWidget(self.one,1,0,1,1)
        ukladH2.addWidget(self.two,1,1,1,1)
        ukladH2.addWidget(self.three,1,2,1,1)
        ukladH2.addWidget(self.four,1,3,1,1)
        self.setLayout(ukladH2)
        self.show()


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        center_point = screen.center()
        window_position = center_point - window_size.center()
        self.move(window_position)
    def insertList(self):
        self.porty.clear()
        self.availablePorts = serial_ports()
        for i in self.availablePorts:
            self.porty.addItem(i)

    def startStop(self):
        self.option = self.listOfActions[2]
        self.uartActions()
    def leftDir(self):
        self.option = self.listOfActions[0]
        self.uartActions()
    def rightDir(self):
        self.option = self.listOfActions[1]
        self.uartActions()
    def speedControl(self):
        self.option = self.listOfSpeeds[self.suwak.value()]
        self.uartActions()
    def uartActions(self):
        if self.porty.currentItem() != None:
            self.uart = serial.Serial(self.availablePorts[self.porty.currentRow()])
            self.uart.write(self.option)
            print(self.uart.readline())
            self.uart.close()
        else:
            print('dupa')

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()







