import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Sterowanie silnikiem krokowym unipolarnym'
        self.left = 0 # odległośc od lewej krawędzi ekranu w pixelach
        self.top = 0 # odległośc od górnej krawędzi ekranu w pixelach
        self.width = 300 # szerokośc okna
        self.height = 100 # wysokość okna
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) ############### # Tu w kolejnych zadaniach będziemy dodwać przycisk typu QPushButton, Slot oraz QLineEdit ###############
        self.center()
        self.start_button = QPushButton('START',self)
        self.start_button.move(100,40)

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