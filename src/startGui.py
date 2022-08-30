from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

import src.view.startGUI


class LaunchGame(QtWidgets.QMainWindow, src.view.startGUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LaunchGame, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        #self.labelImageFranceMap.setPixmap(QPixmap("french-map.png"))

