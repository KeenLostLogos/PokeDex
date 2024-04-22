import os
import requests
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow
from pokedexUI import Ui_MainWindow


def download_file(url, directory, filename=""):
    response = requests.get(url)
    if response.status_code == 200:
        filename = filename + '.' + url.split('.')[-1]
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, filename)
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as f:
                f.write(response.content)
        return filename
    else:
        return ""


def download_sprite(url, pokemon):
    directory = os.path.dirname(os.path.abspath(__file__)) + r"\sprites"
    download_file(url, directory, pokemon)


def download_cry(url, pokemon):
    directory = os.path.dirname(os.path.abspath(__file__)) + r"\cries"
    download_file(url, directory, pokemon)


class PokedexLogic(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__pokemonName = ""
        self.__pokemonID = 0
        self.__pokedexEntry = {}
        self.pushButton.clicked.connect(self.get_pokedex_entry)
        self.male_pushButton.clicked.connect(lambda: self.update_sprite())
        self.female_pushButton.clicked.connect(lambda: self.update_sprite("F"))
        self.form_frame.hide()

    def update_sprite(self, gender="M"):
        filename = self.__pokemonName + ".png" if gender == "M" else self.__pokemonName + "_female.png"
        pixmap = QPixmap('sprites' "\\" + filename)
        self.label_3.setPixmap(pixmap)

    def get_pokedex_entry(self):
        url = "https://pokeapi.co/api/v2/pokemon/" + self.pokedex_id_entry.text()

        response = requests.get(url)
        if response.status_code == 200:
            self.__pokedexEntry = response.json()
            self.__pokemonName = self.__pokedexEntry["species"]["name"]
            default_url = self.__pokedexEntry["sprites"]["front_default"]
            female_url = self.__pokedexEntry["sprites"]["front_female"]
            download_sprite(default_url, self.__pokemonName)
            if female_url:
                download_sprite(female_url, self.__pokemonName + "_female")
                self.form_frame.show()
            else:
                self.form_frame.hide()
            self.update_sprite()
            return True
        else:
            return False
