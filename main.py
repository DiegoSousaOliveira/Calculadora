import sys

from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from buttons import Button

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    display = Display()
    window.addToVLayout(display)

    button = Button('Texto do botão')
    window.addToVLayout(button)

    window.adjustFixedSize()
    window.show()
    app.exec()