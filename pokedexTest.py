import os
import re
from unittest.mock import Mock, patch

import requests
import requests_mock
from PyQt6.QtCore import Qt
from pokedexLogic import PokedexLogic, read_from_json


def test_get_pokedex_entry(qtbot):
    dex = PokedexLogic()
    qtbot.addWidget(dex)
    with requests_mock.Mocker(real_http=False) as m:
        mock_pokedex_data = read_from_json("testData/Pokedex_test_entry")
        mock_ability_data = read_from_json("testData/testAbility1")
        mock_move_data = read_from_json("testData/test_move")
        ability_url_mock = re.compile(".*ability.*")
        move_url_mock = re.compile(".*move.*")
        m.get("https://pokeapi.co/api/v2/pokemon/1", json=mock_pokedex_data, status_code=200)
        m.get(ability_url_mock, json=mock_ability_data, status_code=200)
        m.get(move_url_mock, json=mock_move_data, status_code=200)
        dex.pokedex_id_entry.setText("1")
        qtbot.mouseClick(dex.find_entry_pushButton, Qt.MouseButton.LeftButton)
        os.remove("./moves.json")
        assert dex.pokemonName == "bulbasaur"
        assert dex.game == "Red Blue"
        assert dex.error_label.isHidden() is True
