import os
import requests
from PyQt6.QtGui import QPixmap, QStandardItem
from PyQt6.QtWidgets import QMainWindow, QTreeWidgetItem
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


def kebab_to_start_case(kebab_case_string):
    words = kebab_case_string.split('-')
    start_case_string = ' '.join(word.capitalize() for word in words)
    return start_case_string


class PokedexLogic(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__pokemonName = ""
        self.__pokedexEntry = {}
        self.__allMoves = {}
        self.__game = "emerald"
        self.find_entry_pushButton.clicked.connect(self.get_pokedex_entry)
        self.male_pushButton.clicked.connect(lambda: self.update_sprite())
        self.female_pushButton.clicked.connect(lambda: self.update_sprite("F"))
        self.form_frame.hide()
        self.error_label.hide()
        self.pokemon_move_treeWidget.setColumnWidth(0, 180)
        self.pokemon_move_treeWidget.setColumnWidth(1, 60)
        self.pokemon_move_treeWidget.setColumnWidth(2, 50)
        self.pokemon_move_treeWidget.setColumnWidth(3, 60)
        self.pokemon_move_treeWidget.setColumnWidth(4, 30)
        self.pokemon_move_treeWidget.setColumnWidth(5, 85)
        self.pokemon_move_treeWidget.setColumnWidth(6, 50)

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

    def get_moves(self):
        self.pokemon_move_treeWidget.clear()
        methods = {}
        for move in self.__pokedexEntry["moves"]:
            name = kebab_to_start_case(move["move"]["name"])
            for version in move["version_group_details"]:
                if version["version_group"]["name"] == self.__game:
                    move_learn_method = kebab_to_start_case(version["move_learn_method"]["name"])
                    learned_at = str(version["level_learned_at"])
                    url = move["move"]["url"]
                    response = requests.get(url)
                    if move_learn_method not in methods:
                        methods[move_learn_method] = QTreeWidgetItem(self.pokemon_move_treeWidget)
                        self.pokemon_move_treeWidget.addTopLevelItem(methods[move_learn_method])
                        methods[move_learn_method].setText(0, move_learn_method)
                    if response.status_code == 200:
                        details = response.json()
                        accuracy = str(details["accuracy"])
                        power = str(details["power"])
                        pp = str(details["pp"])
                        priority = str(details["priority"])
                        move_type = details["type"]["name"]
                        damage_class = details["damage_class"]["name"]
                        effect = details["effect_entries"][0]["short_effect"]
                        tree_item = QTreeWidgetItem(methods[move_learn_method])
                        tree_item.setText(0, name if move_learn_method != "Level Up" else f"{name} (lvl-{learned_at})")
                        tree_item.setText(1, move_type)
                        tree_item.setText(2, str(power) if str(power) != "None" else "")
                        tree_item.setText(3, accuracy if accuracy != "None" else "")
                        tree_item.setText(4, pp)
                        tree_item.setText(5, damage_class)
                        tree_item.setText(6, priority if priority != "0" else "")
                        tree_item.setText(7, effect)

    def update_stats(self):
        self.hp_label.setText(str(self.__pokedexEntry["stats"][0]["base_stat"]))
        self.attack_label.setText(str(self.__pokedexEntry["stats"][1]["base_stat"]))
        self.defense_label.setText(str(self.__pokedexEntry["stats"][2]["base_stat"]))
        self.special_attack_label.setText(str(self.__pokedexEntry["stats"][3]["base_stat"]))
        self.special_defense_label.setText(str(self.__pokedexEntry["stats"][4]["base_stat"]))
        self.speed_label.setText(str(self.__pokedexEntry["stats"][5]["base_stat"]))
        total = sum(stat["base_stat"] for stat in self.__pokedexEntry["stats"])
        self.stat_total_label.setText(str(total))
        self.height_label.setText(str(float(self.__pokedexEntry["height"] / 10)) + "M")
        self.weight_label.setText(str(float(self.__pokedexEntry["weight"] / 10)) + "Kg")

    def get_pokedex_entry(self):
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
        self.get_moves()
