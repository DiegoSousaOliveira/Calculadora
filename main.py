import sys

from main_window import MainWindow
from display import Display
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    display = Display()
    window.addToVLayout(display)

    window.adjustFixedSize()
    window.show()
    app.exec()
    