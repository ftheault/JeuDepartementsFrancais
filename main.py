from PyQt5.QtWidgets import QApplication
from src.startGui import LaunchGame
import sys


if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    gui = LaunchGame()
    app.exec_()


