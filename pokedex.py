from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6.QtWidgets import QApplication
from pokedexLogic import PokedexLogic


def main():
    application = QApplication([])
    QFontDatabase.addApplicationFont("Pokemon GB.ttf")
    application.setStyleSheet("QLabel,QLineEdit, QTreeWidget, QPushButton, QComboBox{font-family: 'Pokemon GB'}")
    window = PokedexLogic()
    window.find_entry_pushButton.clicked.connect(window.get_pokedex_entry)
    window.pokedex_id_entry.returnPressed.connect(window.get_pokedex_entry)
    window.pokemon_name_entry.returnPressed.connect(window.get_pokedex_entry)
    window.measurement_pushButton.clicked.connect(window.toggle_measurement_system)
    window.form_comboBox.currentIndexChanged.connect(window.update_sprite)
    window.cry_current_pushButton.clicked.connect(window.play_cry)
    window.cry_legacy_pushButton.clicked.connect(lambda: window.play_cry(True))
    window.error_label.hide()
    window.no_abilities_label.hide()
    window.progressBar.hide()
    window.no_moves_label.hide()
    window.cry_current_pushButton.hide()
    window.cry_legacy_pushButton.hide()
    QFontDatabase.addApplicationFont("./Pokemon Solid.ttf")
    window.title_label.setStyleSheet("font-family: 'Pokemon Solid'; color: '#ffd733'; background-color: '#1111ff'")
    window.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    window.pokemon_move_treeWidget.setColumnWidth(0, 220)
    window.pokemon_move_treeWidget.setColumnWidth(1, 100)
    window.pokemon_move_treeWidget.setColumnWidth(2, 55)
    window.pokemon_move_treeWidget.setColumnWidth(3, 42)
    window.pokemon_move_treeWidget.setColumnWidth(4, 58)
    window.pokemon_move_treeWidget.setColumnWidth(5, 15)
    window.pokemon_move_treeWidget.setColumnWidth(6, 46)
    window.ability_treeWidget.setColumnWidth(3, 220)
    window.ability_treeWidget.setColumnWidth(2, 70)
    window.ability_treeWidget.setColumnWidth(0, 140)
    window.ability_treeWidget.setColumnWidth(1, 60)
    window.pokemon_move_treeWidget.setAlternatingRowColors(True)
    window.show()
    application.exec()


if __name__ == "__main__":
    main()
