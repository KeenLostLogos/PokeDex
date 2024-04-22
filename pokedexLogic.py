import os
import requests
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow
from pokedexUI import Ui_MainWindow


def download_file(url, directory, filename=""):

    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = filename + '.' + url.split('.')[-1]
    filepath = os.path.join(directory, filename)

    if not os.path.exists(filepath):
        response = requests.get(url)

        if response.status_code != 200:
            return False

        with open(filepath, 'wb') as f:
            f.write(response.content)

    return True


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
        self.find_entry_pushButton.clicked.connect(self.get_pokedex_entry)
        self.male_pushButton.clicked.connect(lambda: self.update_sprite())
        self.female_pushButton.clicked.connect(lambda: self.update_sprite("F"))
        self.form_frame.hide()

    def download_sprites(self):
        directory = os.path.dirname(os.path.abspath(__file__)) + r"\sprites"
        default_url = self.__pokedexEntry["sprites"]["front_default"]
        female_url = self.__pokedexEntry["sprites"]["front_female"]
        download_file(default_url, directory, self.__pokemonName)
        if female_url:
            download_file(default_url, directory, self.__pokemonName + "_female")
            self.form_frame.show()
        else:
            self.form_frame.hide()

    def update_sprite(self, gender="M"):
        filename = self.__pokemonName + ".png" if gender == "M" else self.__pokemonName + "_female.png"
        pixmap = QPixmap('sprites' "\\" + filename)
        self.sprite_label.setPixmap(pixmap)

    def get_pokedex_entry(self):
        url = "https://pokeapi.co/api/v2/pokemon/" + self.pokedex_id_entry.text()
        response = requests.get(url)
        if response.status_code != 200:
            return False

        self.__pokedexEntry = response.json()
        self.__pokemonName = self.__pokedexEntry["species"]["name"]
        self.download_sprites()
        self.update_sprite()
        return True
