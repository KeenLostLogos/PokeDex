import os
import re
import requests_mock
from PyQt6.QtCore import Qt
from pokedexLogic import PokedexLogic, read_from_json


class TestDownloadFile:
    # TODO implement test cases
    pass


class TestKebabToStartCase:
    # TODO implement test cases
    pass


class TestReadFromJson:
    # TODO implement test cases
    pass


class TestInitAndConfigUI:
    # TODO implement test cases
    pass


class TestSendError:
    # TODO implement test cases
    pass


class TestPlayCry:
    # TODO implement test cases
    pass


class TestDownloadSprites:
    # TODO implement test cases
    pass


class TestDownloadCries:
    # TODO implement test cases
    pass


class TestUpdateSprites:
    # TODO implement test cases
    pass


class TestGetAbilities:
    # TODO implement test cases
    pass


class TestGetMoves:
    # TODO implement test cases
    pass


class TestAddTreeItem:

    def test_no_selection(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.add_tree_item("test", "test", "test")

        assert len(dex.pokemon_move_treeWidget.children()) == 7

    def test_valid_selection(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        # TODO need to make sure that this file exists and has the move 'Swords Dance'
        dex.pokedexEntry = read_from_json("./testData/Pokedex_test_entry")
        dex.add_tree_item("Swords Dance", "test", "test")

        assert dex.pokemon_move_treeWidget.topLevelItem(0).text(0) == "test"
        assert dex.pokemon_move_treeWidget.topLevelItem(0).child(0).text(0) == "Swords Dance"
        assert dex.pokemon_move_treeWidget.topLevelItem(0).child(0).text(1) == "Normal"
        assert dex.pokemon_move_treeWidget.topLevelItem(0).child(0).text(3) == ""
        assert dex.pokemon_move_treeWidget.topLevelItem(0).child(0).text(4) == ""
        assert dex.pokemon_move_treeWidget.topLevelItem(0).child(0).text(5) == "20"
        assert dex.pokemon_move_treeWidget.topLevelItem(0).child(0).text(6) == ""
        assert dex.pokemon_move_treeWidget.topLevelItem(0).child(0).text(
            7) == "\nRaises the user's Attack by two stages.\n"


class TestUpdateStats:

    def test_no_selection(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.update_stats()

        assert dex.hp_label.text() == ""
        assert dex.attack_label.text() == ""
        assert dex.defense_label.text() == ""
        assert dex.special_attack_label.text() == ""
        assert dex.special_defense_label.text() == ""
        assert dex.speed_label.text() == ""
        assert dex.stat_total_label.text() == ""

    def test_valid_selection(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.pokedexEntry = read_from_json("./testData/Pokedex_test_entry")
        dex.update_stats()

        assert dex.hp_label.text() == "45"
        assert dex.attack_label.text() == "49"
        assert dex.defense_label.text() == "49"
        assert dex.special_attack_label.text() == "65"
        assert dex.special_defense_label.text() == "65"
        assert dex.speed_label.text() == "45"
        assert dex.stat_total_label.text() == "318"


class TestToggleMeasurementSystem:

    def test_toggle_to_imperial(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.toggle_measurement_system()

        assert dex.metric_system is False

    def test_toggle_back_to_metric(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.toggle_measurement_system()
        dex.toggle_measurement_system()

        assert dex.metric_system is True


class TestUpdateHeightAndWeight:

    def test_no_selection(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.update_height_and_weight()

        assert dex.height_label.text() == ""
        assert dex.weight_label.text() == ""

    def test_metric(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.pokedexEntry = read_from_json("./testData/Pokedex_test_entry")
        dex.update_height_and_weight()

        assert dex.height_label.text() == "0.7m"
        assert dex.weight_label.text() == "6.9kg"

    def test_imperial(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.pokedexEntry = read_from_json("./testData/Pokedex_test_entry")
        dex.metric_system = False
        dex.update_height_and_weight()

        assert dex.height_label.text() == "2.3ft"
        assert dex.weight_label.text() == "15.2lbs"


class TestSetTypes:

    def test_no_selection(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.set_types()

        assert dex.types_label.text() == "Type"
        assert dex.type_image_one_label.isHidden() is True
        assert dex.type_image_two_label.isHidden() is True

    def test_one_type(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.pokedexEntry = read_from_json("./testData/Pokedex_test_entry_2")
        dex.set_types()

        assert dex.types_label.text() == "Type"
        assert dex.type_image_one_label.isHidden() is False
        assert dex.type_image_two_label.isHidden() is True

    def test_two_types(self, qtbot):
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.pokedexEntry = read_from_json("./testData/Pokedex_test_entry")
        dex.set_types()

        assert dex.types_label.text() == "Types"
        assert dex.type_image_one_label.isHidden() is False
        assert dex.type_image_two_label.isHidden() is False


@requests_mock.Mocker(kw='mock')
class TestGetPokeDexEntry:

    def test_correct(self, qtbot, **kwargs):
        """Test pokedex entry calls correct api, PokemonName and Game are set correctly"""
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        mock_pokedex_data = read_from_json("testData/Pokedex_test_entry")
        mock_ability_data = read_from_json("testData/testAbility1")
        mock_move_data = read_from_json("testData/test_move")
        ability_url_mock = re.compile(".*ability.*")
        move_url_mock = re.compile(".*move.*")
        kwargs['mock'].get("https://pokeapi.co/api/v2/pokemon/1", json=mock_pokedex_data, status_code=200)
        kwargs['mock'].get(ability_url_mock, json=mock_ability_data, status_code=200)
        kwargs['mock'].get(move_url_mock, json=mock_move_data, status_code=200)
        dex.pokedex_id_entry.setText("1")
        qtbot.mouseClick(dex.find_entry_pushButton, Qt.MouseButton.LeftButton)
        if os.path.exists("./moves.json"):
            os.remove("./moves.json")
        assert dex.pokemonName == "bulbasaur"
        assert dex.game == "Red Blue"
        assert dex.error_label.isHidden() is True

    def test_empty(self, qtbot, **kwargs):
        """Test pokedex entry does not call anything when there is no input and displays an error"""
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        qtbot.mouseClick(dex.find_entry_pushButton, Qt.MouseButton.LeftButton)
        if os.path.exists("./moves.json"):
            os.remove("./moves.json")

        assert dex.error_label.text() == "Please enter a valid Name or ID."
        assert dex.error_label.isHidden() is False
        assert dex.pokemonName == ""
        assert dex.game == ""

    def test_incorrect(self, qtbot, **kwargs):
        """Test displays an error when there is an incorrect entry"""
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.pokedex_id_entry.setText("1")
        kwargs['mock'].get("https://pokeapi.co/api/v2/pokemon/1", status_code=404)
        qtbot.mouseClick(dex.find_entry_pushButton, Qt.MouseButton.LeftButton)
        if os.path.exists("./moves.json"):
            os.remove("./moves.json")
        assert dex.error_label.text() == "Please enter a valid Name or ID."
        assert dex.error_label.isHidden() is False
        assert dex.pokemonName == ""
        assert dex.game == ""

    def test_server_down(self, qtbot, **kwargs):
        """Test displays an error when the server is down"""
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.pokedex_id_entry.setText("1")
        kwargs['mock'].get("https://pokeapi.co/api/v2/pokemon/1", status_code=500)
        qtbot.mouseClick(dex.find_entry_pushButton, Qt.MouseButton.LeftButton)
        if os.path.exists("./moves.json"):
            os.remove("./moves.json")
        assert dex.error_label.text() == "The server currently unavailable, please try again later!"
        assert dex.error_label.isHidden() is False
        assert dex.pokemonName == ""
        assert dex.game == ""

    def test_other_error(self, qtbot, **kwargs):
        """Test displays an error when the server gives unexpected error"""
        dex = PokedexLogic()
        qtbot.addWidget(dex)
        dex.pokedex_id_entry.setText("1")
        kwargs['mock'].get("https://pokeapi.co/api/v2/pokemon/1", status_code=401)
        qtbot.mouseClick(dex.find_entry_pushButton, Qt.MouseButton.LeftButton)
        if os.path.exists("./moves.json"):
            os.remove("./moves.json")
        assert dex.error_label.text() == "There was an unexpected issue, please try again later!"
        assert dex.error_label.isHidden() is False
        assert dex.pokemonName == ""
        assert dex.game == ""
