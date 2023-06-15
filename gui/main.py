import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QSlider, QLCDNumber, QSplitter, QHBoxLayout, QGroupBox,QRadioButton,QGridLayout
from PyQt5.QtCore import Qt
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Sterowanie silnikiem krokowym unipolarnym'
        self.left = 0 # odległośc od lewej krawędzi ekranu w pixelach
        self.top = 0 # odległośc od górnej krawędzi ekranu w pixelach
        self.width = 400 # szerokośc okna
        self.height = 300 # wysokość okna
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


        self.start = QPushButton('&Start/Stop',self)
        self.connect = QPushButton('&Connect',self)
        self.left = QPushButton('&Left',self)
        self.right = QPushButton('&Right',self)



        ukladH2 = QGridLayout()
        ukladH2.addWidget(self.suwak,2,0,1,2)
        ukladH2.addWidget(self.start,1,0)
        ukladH2.addWidget(self.connect,0,0)
        ukladH2.addWidget(self.left,3,0)
        ukladH2.addWidget(self.right,3,1)
        self.setLayout(ukladH2)
        self.show()


    def center(self):
        # Pobierz rozmiar głównego ekranu
        screen = QDesktopWidget().screenGeometry()
        # Pobierz rozmiar okna
        window_size = self.geometry()
        # Oblicz pozycję środka ekranu
        center_point = screen.center()
        # Oblicz pozycję lewego górnego rogu okna
        window_position = center_point - window_size.center()
        # Ustaw pozycję okna
        self.move(window_position)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()