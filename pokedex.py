from PyQt6.QtWidgets import QApplication
from pokedexLogic import PokedexLogic


def main():
    application = QApplication([])
    window = PokedexLogic()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()
