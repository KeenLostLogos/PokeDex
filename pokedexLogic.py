import json
import os
import requests
import pygame
from PyQt6.QtGui import QPixmap, QFont, QIcon, QFontDatabase
from PyQt6.QtWidgets import QMainWindow, QTreeWidgetItem
from pokedexUI import Ui_MainWindow
from playsound import playsound


def download_file(url: str, directory: str, filename="") -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename: str = filename + '.' + url.split('.')[-1]
    filepath: str = os.path.join(directory, filename)

    if not os.path.exists(filepath):
        response: requests.models.Response = requests.get(url)

        if response.status_code != 200:
            return

        with open(filepath, 'wb') as f:
            f.write(response.content)

    return


def kebab_to_start_case(kebab_case_string: str) -> str:
    words: str = kebab_case_string.split('-')
    start_case_string: str = ' '.join(word.capitalize() for word in words)
    return start_case_string


class PokedexLogic(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.__pokemonName: str = ""
        self.__pokedexEntry: dict = {}
        self.__methods: dict = {}
        self.__allMoves: dict = {}
        self.__metric_system: bool = True
        self.__game: str = self.comboBox.currentText()
        self.ui_changes()
        pygame.mixer.init()

    def ui_changes(self) -> None:
        self.find_entry_pushButton.clicked.connect(self.get_pokedex_entry)
        self.pokedex_id_entry.returnPressed.connect(self.get_pokedex_entry)
        self.pokemon_name_entry.returnPressed.connect(self.get_pokedex_entry)
        self.measurement_pushButton.clicked.connect(self.toggle_measurement_system)
        self.form_comboBox.currentIndexChanged.connect(self.update_sprite)
        self.cry_current_pushButton.clicked.connect(lambda: self.play_cry("_latest.ogg"))
        self.cry_legacy_pushButton.clicked.connect(lambda: self.play_cry("_legacy.ogg"))
        self.error_label.hide()
        self.no_abilities_label.hide()
        self.progressBar.hide()
        self.no_moves_label.hide()
        self.cry_current_pushButton.hide()
        self.cry_legacy_pushButton.hide()
        QFontDatabase.addApplicationFont("./Pokemon Solid.ttf")
        self.title_label.setFont(QFont("Pokemon Solid", 18))
        self.pokemon_move_treeWidget.setColumnWidth(0, 210)
        self.pokemon_move_treeWidget.setColumnWidth(1, 80)
        self.pokemon_move_treeWidget.setColumnWidth(2, 50)
        self.pokemon_move_treeWidget.setColumnWidth(3, 70)
        self.pokemon_move_treeWidget.setColumnWidth(4, 30)
        self.pokemon_move_treeWidget.setColumnWidth(5, 100)
        self.pokemon_move_treeWidget.setColumnWidth(6, 55)
        self.ability_treeWidget.setColumnWidth(3, 200)
        self.ability_treeWidget.setColumnWidth(0, 125)
        self.ability_treeWidget.setColumnWidth(1, 60)
        self.pokemon_move_treeWidget.setAlternatingRowColors(True)

    def send_error(self, error_text: str) -> None:
        self.error_label.setText(error_text)
        self.error_label.show()

    def play_cry(self, cry: str) -> None:
        pygame.mixer.music.load("./cries/" + self.__pokemonName + cry)
        pygame.mixer.music.play()

    def save_to_json(self) -> None:
        if not os.path.exists(os.path.dirname(__file__) + "\\moves"):
            os.makedirs(os.path.dirname(__file__) + r"\moves")
        with open(r"Moves" + "\\" + f"{self.__game}.json", "w+") as file:
            json.dump(self.__allMoves, file)

    def read_from_json(self) -> None:
        if os.path.exists(os.path.dirname(__file__) + r"\moves" + "\\" + f"{self.__game}.json"):
            with open(r"moves" + "\\" + f"{self.__game}.json", 'r') as file:
                data = json.load(file)
            self.__allMoves = data
        else:
            self.__allMoves = {}

    def download_sprites(self) -> None:
        directory: str = os.path.dirname(os.path.abspath(__file__)) + r"\sprites"
        default_url: str = self.__pokedexEntry["sprites"]["front_default"]
        shiny_url: str = self.__pokedexEntry["sprites"]["front_shiny"]
        female_url: str = self.__pokedexEntry["sprites"]["front_female"]
        shiny_female_url: str = self.__pokedexEntry["sprites"]["front_shiny_female"]
        download_file(default_url, directory, self.__pokemonName + "_default")
        download_file(shiny_url, directory, self.__pokemonName + "_shiny")
        self.form_comboBox.setCurrentText("Default")
        self.form_comboBox.removeItem(2)
        self.form_comboBox.removeItem(2)
        if female_url:
            download_file(female_url, directory, self.__pokemonName + "_female")
            download_file(shiny_female_url, directory, self.__pokemonName + "_shiny_female")
            self.form_comboBox.addItem("Female")
            self.form_comboBox.addItem("Shiny Female")

    def download_cries(self) -> None:
        self.cry_current_pushButton.show()
        self.cry_legacy_pushButton.hide()
        directory: str = os.path.dirname(__file__) + r"\cries"
        if self.__pokedexEntry["cries"]["latest"]:
            url = self.__pokedexEntry["cries"]["latest"]
            download_file(url, directory, self.__pokemonName + "_latest")
        if self.__pokedexEntry["cries"]["legacy"]:
            url = self.__pokedexEntry["cries"]["legacy"]
            download_file(url, directory, self.__pokemonName + "_legacy")
            self.cry_legacy_pushButton.show()

    def update_sprite(self) -> None:
        if self.__pokedexEntry:
            file_suffix: str = "_" + self.form_comboBox.currentText().lower().replace(" ", "_")
            filename: str = self.__pokemonName + file_suffix
            pixmap: QPixmap = QPixmap('sprites' "\\" + filename)
            self.sprite_label.setPixmap(pixmap)

    def get_abilities(self) -> None:
        self.ability_treeWidget.clear()
        self.no_abilities_label.hide()
        no_abilities_in_current_gen: bool = True

        for ability in self.__pokedexEntry["abilities"]:
            name: str = kebab_to_start_case(ability["ability"]["name"])
            hidden: str = ability["is_hidden"]
            response: requests.models.Response = requests.get(ability["ability"]["url"])
            if response.status_code != 200:
                return
            details: dict = response.json()
            for text in details["flavor_text_entries"]:
                if "en" != text["language"]["name"]:
                    continue
                if self.__game != kebab_to_start_case(text["version_group"]["name"]):
                    continue
                flavor_text: str = text["flavor_text"].replace("\n", " ")
                generation: str = details["generation"]["name"]
                new_tree_item: QTreeWidgetItem = QTreeWidgetItem(self.ability_treeWidget)
                new_tree_item.setText(0, name)
                new_tree_item.setText(1, "True" if hidden else "")
                new_tree_item.setText(2, generation)
                new_tree_item.setText(3, flavor_text)
                no_abilities_in_current_gen = False
                break

        if no_abilities_in_current_gen:
            self.no_abilities_label.show()

    def get_moves(self) -> None:
        self.no_moves_label.hide()
        self.progressBar.show()
        self.progressBar.setValue(0)
        progress: int = 0
        self.__game = self.comboBox.currentText()
        self.pokemon_move_treeWidget.clear()
        self.__methods = {}
        self.read_from_json()
        already_displayed: list = []
        self.progressBar.setMaximum(len(self.__pokedexEntry["moves"]))
        for move in self.__pokedexEntry["moves"]:
            for version in move["version_group_details"]:

                name: str = kebab_to_start_case(move["move"]["name"])
                if name in already_displayed:
                    break

                game_version: str = kebab_to_start_case(version["version_group"]["name"])
                if game_version != self.__game:
                    continue

                if name in self.__allMoves.keys():
                    self.add_tree_item(name)
                    already_displayed.append(name)
                else:
                    response: requests.models.Response = requests.get(move["move"]["url"])
                    if response.status_code != 200:
                        self.send_error("Some moves were not able to be retrieved from the database, please try again.")
                        break
                    details: dict = response.json()
                    effect: (str, list) = details["effect_entries"][0]["short_effect"] if details[
                        "effect_entries"] else ""
                    effect = effect.split()
                    lines: list = [' '.join(effect[i:i + 8]) for i in range(0, len(effect), 8)]
                    effect = '\n'.join(lines)
                    new_move: dict = {"name": name,
                                      "move_learn_method": kebab_to_start_case(version["move_learn_method"]["name"]),
                                      "learned_at": str(version["level_learned_at"]),
                                      "accuracy": str(details["accuracy"]),
                                      "power": str(details["power"]),
                                      "pp": str(details["pp"]),
                                      "priority": str(details["priority"]),
                                      "type": details["type"]["name"],
                                      "damage_class": details["damage_class"]["name"],
                                      "effect": effect}
                    self.__allMoves[name] = new_move
                    already_displayed.append(name)
                    self.add_tree_item(name)
            progress += 1
            self.progressBar.setValue(progress)
        if not already_displayed:
            self.no_moves_label.show()
        self.save_to_json()
        self.progressBar.hide()

    def add_tree_item(self, name: str):
        move: dict = self.__allMoves[name]
        method: str = move["move_learn_method"]
        if method not in self.__methods:
            self.__methods[method] = QTreeWidgetItem(self.pokemon_move_treeWidget)
            self.pokemon_move_treeWidget.addTopLevelItem(self.__methods[method])
            self.__methods[method].setText(0, method)
            self.__methods[method].setFont(0, QFont("Verdana", 12))
        tree_item: QTreeWidgetItem = QTreeWidgetItem(self.__methods[method])
        name: str = move["name"] if move["move_learn_method"] != "Level Up" else f"{move['name']} (lvl-{move['learned_at']})"
        tree_item.setText(0, name)
        tree_item.setFont(0, QFont("Verdana", 10))
        tree_item.setText(1, move["type"].capitalize())
        tree_item.setIcon(1, QIcon(f"./types/{move['type'].capitalize()}_icon_HOME3.png"))
        tree_item.setText(2, move["power"] if move["power"] != "None" else "")
        tree_item.setText(3, move["accuracy"] if move["accuracy"] != "None" else "")
        tree_item.setText(4, move["pp"])
        tree_item.setText(5, move["damage_class"].capitalize())
        tree_item.setIcon(5, QIcon(f"./types/{move['damage_class'].capitalize()}.png"))
        tree_item.setText(6, move["priority"] if move["priority"] != "0" else "")
        tree_item.setText(7, move["effect"])

    def update_stats(self) -> None:
        self.hp_label.setText(str(self.__pokedexEntry["stats"][0]["base_stat"]))
        self.attack_label.setText(str(self.__pokedexEntry["stats"][1]["base_stat"]))
        self.defense_label.setText(str(self.__pokedexEntry["stats"][2]["base_stat"]))
        self.special_attack_label.setText(str(self.__pokedexEntry["stats"][3]["base_stat"]))
        self.special_defense_label.setText(str(self.__pokedexEntry["stats"][4]["base_stat"]))
        self.speed_label.setText(str(self.__pokedexEntry["stats"][5]["base_stat"]))
        total: str = str(sum(stat["base_stat"] for stat in self.__pokedexEntry["stats"]))
        self.stat_total_label.setText(total)

    def toggle_measurement_system(self) -> None:
        if self.__metric_system:
            self.__metric_system = False
            self.update_height_and_weight()
        else:
            self.__metric_system = True
            self.update_height_and_weight()

    def update_height_and_weight(self) -> None:
        if self.__pokedexEntry:
            height: float = float(self.__pokedexEntry["height"] / 10)
            weight: float = float(self.__pokedexEntry["weight"] / 10)
            if not self.__metric_system:
                height = height * 3.281
                weight = weight * 2.205
            height_label: str = "m" if self.__metric_system else "ft"
            weight_label: str = "kg" if self.__metric_system else "lbs"
            self.height_label.setText(str(round(height, 1)) + height_label)
            self.weight_label.setText(str(round(weight, 1)) + weight_label)

    def set_types(self) -> None:
        if self.__pokedexEntry["types"][0]:
            filename: str = self.__pokedexEntry["types"][0]["type"]["name"].upper() + "_icon_HOME3.png"
            pixmap: QPixmap = QPixmap('types' "\\" + filename)
            self.type_image_one_label.setPixmap(pixmap)
            self.types_label.setText("Type")
        try:
            if self.__pokedexEntry["types"][1]:
                filename = self.__pokedexEntry["types"][1]["type"]["name"].upper() + "_icon_HOME3.png"
                pixmap: QPixmap = QPixmap('types' "\\" + filename)
                self.type_image_two_label.setPixmap(pixmap)
                self.type_image_two_label.show()
                self.types_label.setText("Types")
        except IndexError:
            self.type_image_two_label.hide()

    def get_pokedex_entry(self) -> None:
        url: str = "https://pokeapi.co/api/v2/pokemon/"
        pokemon_id: str = self.pokedex_id_entry.text().strip()
        name: str = self.pokemon_name_entry.text().strip().lower()

        if name == "" and pokemon_id == "":
            self.send_error("Please enter a valid Name or ID")
            return

        url: str = url + pokemon_id if pokemon_id else url + name
        response: requests.models.Response = requests.get(url)
        if response.status_code != 200:
            if response.status_code == 404:
                self.send_error("Please enter a valid Name or ID.")
            elif response.status_code >= 500:
                self.send_error("The server currently unavailable, please try again later!")
            else:
                self.send_error("There was an unexpected issue, please try again later!")
            return

        self.error_label.hide()
        self.__pokedexEntry = response.json()
        self.__pokemonName = self.__pokedexEntry["species"]["name"]
        self.pokemon_name_entry.setText(self.__pokemonName.capitalize())
        self.pokedex_id_entry.setText(str(self.__pokedexEntry["id"]))
        self.__game = self.comboBox.currentText()
        self.download_sprites()
        self.update_sprite()
        self.update_stats()
        self.update_height_and_weight()
        self.get_abilities()
        self.set_types()
        self.download_cries()
        self.get_moves()
