from PySide6.QtWidgets import (QApplication, QLabel,  QMainWindow, QVBoxLayout,
                               QWidget)

class MainWindow(QMainWindow):
    def __init__(self, parent= None, *args, **kwargs): # type: ignore
        super().__init__(parent)

        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
