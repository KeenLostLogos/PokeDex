import sys

from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QApplication
from pokedexLogic import PokedexLogic


class Pokedex:
    def __init__(self):
        self.application = QApplication(sys.argv)
        QFontDatabase.addApplicationFont("./Pokemon GB.ttf")
        QFontDatabase.addApplicationFont("./Pokemon Solid.ttf")
        self.application.setStyleSheet("QLabel,QLineEdit, QPushButton, QComboBox{font-family: 'Pokemon GB'}")
        self.window = PokedexLogic()
        self.window.show()
        sys.exit(self.application.exec())


if __name__ == "__main__":
    Pokedex()
