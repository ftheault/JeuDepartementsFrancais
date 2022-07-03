from PyQt5.QtWidgets import QApplication
from src.startGui import Start
import sys


if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    gui = Start()
    app.exec_()


