import json
import os
import requests
from PyQt6.QtGui import QPixmap
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


def save_to_json(data):
    with open('Moves.json', 'w') as file:
        json.dump(data, file)


def read_from_json():
    if os.path.exists(os.path.dirname(__file__) + r"\Moves.json"):
        with open('Moves.json', 'r') as file:
            data = json.load(file)
        return data
    else:
        return {}


def download_cry(url, pokemon):
    directory = os.path.dirname(__file__) + r"\cries"
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
        self.__methods = {}
        self.__allMoves = read_from_json()
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

    def closeEvent(self, event):
        super(QMainWindow, self).closeEvent(event)
        save_to_json(self.__allMoves)

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
        self.__methods = {}
        already_displayed = []

        for move in self.__pokedexEntry["moves"]:
            for version in move["version_group_details"]:

                if move in already_displayed:
                    break

                game_version = version["version_group"]["name"]
                if game_version != self.__game:
                    continue

                name = kebab_to_start_case(move["move"]["name"])
                move_version = f"{game_version}-{name}"
                new_move = {"name": name}

                if move_version in self.__allMoves.keys():
                    self.add_tree_item(move_version)
                    already_displayed.append(move)
                else:
                    new_move["move_learn_method"] = kebab_to_start_case(version["move_learn_method"]["name"])
                    new_move["learned_at"] = str(version["level_learned_at"])
                    response = requests.get(move["move"]["url"])
                    if response.status_code != 200:
                        break
                    details = response.json()
                    new_move["accuracy"] = str(details["accuracy"])
                    new_move["power"] = str(details["power"])
                    new_move["pp"] = str(details["pp"])
                    new_move["priority"] = str(details["priority"])
                    new_move["type"] = details["type"]["name"]
                    new_move["damage_class"] = details["damage_class"]["name"]
                    new_move["effect"] = details["effect_entries"][0]["short_effect"]
                    self.__allMoves[move_version] = new_move
                    self.add_tree_item(move_version)

    def add_tree_item(self, move_version):
        move = self.__allMoves[move_version]
        method = move["move_learn_method"]
        if method not in self.__methods:
            self.__methods[method] = QTreeWidgetItem(self.pokemon_move_treeWidget)
            self.pokemon_move_treeWidget.addTopLevelItem(self.__methods[method])
            self.__methods[method].setText(0, method)
        tree_item = QTreeWidgetItem(self.__methods[method])
        tree_item.setText(0, move["name"] if move[
                                                 "move_learn_method"] != "Level Up" else f"{move['name']} (lvl-{move['learned_at']})")
        tree_item.setText(1, move["type"])
        tree_item.setText(2, move["power"] if move["power"] != "None" else "")
        tree_item.setText(3, move["accuracy"] if move["accuracy"] != "None" else "")
        tree_item.setText(4, move["pp"])
        tree_item.setText(5, move["damage_class"])
        tree_item.setText(6, move["priority"] if move["priority"] != "0" else "")
        tree_item.setText(7, move["effect"])

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
