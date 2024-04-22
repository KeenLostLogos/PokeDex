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
        self.__pokedexEntry = {}
        self.find_entry_pushButton.clicked.connect(self.get_pokedex_entry)
        self.male_pushButton.clicked.connect(lambda: self.update_sprite())
        self.female_pushButton.clicked.connect(lambda: self.update_sprite("F"))
        self.form_frame.hide()
        self.error_label.hide()

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

    def update_stats(self):
        self.hp_label.setText(str(self.__pokedexEntry["stats"][0]["base_stat"]))
        self.attack_label.setText(str(self.__pokedexEntry["stats"][1]["base_stat"]))
        self.defense_label.setText(str(self.__pokedexEntry["stats"][2]["base_stat"]))
        self.special_attack_label.setText(str(self.__pokedexEntry["stats"][3]["base_stat"]))
        self.special_defense_label.setText(str(self.__pokedexEntry["stats"][4]["base_stat"]))
        self.speed_label.setText(str(self.__pokedexEntry["stats"][5]["base_stat"]))
        total = sum(stat["base_stat"] for stat in self.__pokedexEntry["stats"])
        self.stat_total_label.setText(str(total))
        self.height_label.setText(str(self.__pokedexEntry["height"]))
        self.weight_label.setText(str(self.__pokedexEntry["weight"]))

    def get_pokedex_entry(self):
        try:
            url = "https://pokeapi.co/api/v2/pokemon/"
            pokemon_id = self.pokedex_id_entry.text().strip()
            name = self.pokemon_name_entry.text().strip().lower()
            url = url + pokemon_id if pokemon_id else url + name
            response = requests.get(url)
            if response.status_code != 200:
                self.error_label.show()
                return
            self.error_label.hide()
            self.__pokedexEntry = response.json()
            self.__pokemonName = self.__pokedexEntry["species"]["name"]
            self.download_sprites()
            self.update_sprite()
            self.update_stats()

        except Exception as e:
            self.error_label.show()
