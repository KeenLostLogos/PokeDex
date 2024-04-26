# Form implementation generated from reading ui file '.\PokedexUI.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(968, 928)
        MainWindow.setMinimumSize(QtCore.QSize(968, 788))
        MainWindow.setMaximumSize(QtCore.QSize(968, 928))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.find_entry_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.find_entry_pushButton.setGeometry(QtCore.QRect(100, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.find_entry_pushButton.setFont(font)
        self.find_entry_pushButton.setObjectName("find_entry_pushButton")
        self.pokedex_id_entry = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pokedex_id_entry.setGeometry(QtCore.QRect(140, 140, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.pokedex_id_entry.setFont(font)
        self.pokedex_id_entry.setObjectName("pokedex_id_entry")
        self.pokemon_name_entry = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pokemon_name_entry.setGeometry(QtCore.QRect(140, 100, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.pokemon_name_entry.setFont(font)
        self.pokemon_name_entry.setObjectName("pokemon_name_entry")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.sprite_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.sprite_label.setGeometry(QtCore.QRect(480, 80, 161, 151))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(1)
        self.sprite_label.setFont(font)
        self.sprite_label.setText("")
        self.sprite_label.setPixmap(QtGui.QPixmap(".\\sprites/gengar.png"))
        self.sprite_label.setScaledContents(True)
        self.sprite_label.setObjectName("sprite_label")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(700, 15, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 590, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(460, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.height_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.height_label.setGeometry(QtCore.QRect(570, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.height_label.setFont(font)
        self.height_label.setText("")
        self.height_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.height_label.setObjectName("height_label")
        self.weight_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.weight_label.setGeometry(QtCore.QRect(570, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.weight_label.setFont(font)
        self.weight_label.setText("")
        self.weight_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.weight_label.setObjectName("weight_label")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pokemon_move_treeWidget = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.pokemon_move_treeWidget.setGeometry(QtCore.QRect(10, 310, 951, 451))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.pokemon_move_treeWidget.setFont(font)
        self.pokemon_move_treeWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);")
        self.pokemon_move_treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.pokemon_move_treeWidget.setWordWrap(True)
        self.pokemon_move_treeWidget.setObjectName("pokemon_move_treeWidget")
        self.hp_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.hp_label.setGeometry(QtCore.QRect(870, 60, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.hp_label.setFont(font)
        self.hp_label.setText("")
        self.hp_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hp_label.setObjectName("hp_label")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(700, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(700, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.attack_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.attack_label.setGeometry(QtCore.QRect(870, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.attack_label.setFont(font)
        self.attack_label.setText("")
        self.attack_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.attack_label.setObjectName("attack_label")
        self.label_18 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(700, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.defense_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.defense_label.setGeometry(QtCore.QRect(870, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.defense_label.setFont(font)
        self.defense_label.setText("")
        self.defense_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.defense_label.setObjectName("defense_label")
        self.label_20 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(700, 150, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.special_attack_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.special_attack_label.setGeometry(QtCore.QRect(870, 150, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.special_attack_label.setFont(font)
        self.special_attack_label.setText("")
        self.special_attack_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.special_attack_label.setObjectName("special_attack_label")
        self.label_22 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(700, 180, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.special_defense_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.special_defense_label.setGeometry(QtCore.QRect(870, 180, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.special_defense_label.setFont(font)
        self.special_defense_label.setText("")
        self.special_defense_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.special_defense_label.setObjectName("special_defense_label")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(700, 210, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.speed_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.speed_label.setGeometry(QtCore.QRect(870, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.speed_label.setFont(font)
        self.speed_label.setText("")
        self.speed_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.speed_label.setObjectName("speed_label")
        self.label_26 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(700, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.stat_total_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.stat_total_label.setGeometry(QtCore.QRect(870, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.stat_total_label.setFont(font)
        self.stat_total_label.setText("")
        self.stat_total_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stat_total_label.setObjectName("stat_total_label")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 110, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 170, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(0, 0, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(20, 240, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: red")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("error_label")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 60, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 60, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.ability_treeWidget = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.ability_treeWidget.setGeometry(QtCore.QRect(10, 770, 951, 101))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.ability_treeWidget.setFont(font)
        self.ability_treeWidget.setObjectName("ability_treeWidget")
        self.no_abilities_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.no_abilities_label.setGeometry(QtCore.QRect(10, 770, 951, 101))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.no_abilities_label.setFont(font)
        self.no_abilities_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.no_abilities_label.setObjectName("no_abilities_label")
        self.types_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.types_label.setGeometry(QtCore.QRect(310, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.types_label.setFont(font)
        self.types_label.setToolTipDuration(-1)
        self.types_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.types_label.setObjectName("types_label")
        self.type_image_one_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.type_image_one_label.setGeometry(QtCore.QRect(330, 90, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(1)
        self.type_image_one_label.setFont(font)
        self.type_image_one_label.setText("")
        self.type_image_one_label.setScaledContents(False)
        self.type_image_one_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.type_image_one_label.setObjectName("type_image_one_label")
        self.type_image_two_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.type_image_two_label.setGeometry(QtCore.QRect(330, 190, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(1)
        self.type_image_two_label.setFont(font)
        self.type_image_two_label.setText("")
        self.type_image_two_label.setScaledContents(False)
        self.type_image_two_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.type_image_two_label.setObjectName("type_image_two_label")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 880, 951, 23))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.progressBar.setFont(font)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.measurement_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.measurement_pushButton.setGeometry(QtCore.QRect(430, 250, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.measurement_pushButton.setFont(font)
        self.measurement_pushButton.setObjectName("measurement_pushButton")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(480, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.form_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.form_comboBox.setGeometry(QtCore.QRect(480, 40, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.form_comboBox.setFont(font)
        self.form_comboBox.setObjectName("form_comboBox")
        self.form_comboBox.addItem("")
        self.form_comboBox.addItem("")
        self.form_comboBox.addItem("")
        self.form_comboBox.addItem("")
        self.no_moves_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.no_moves_label.setGeometry(QtCore.QRect(10, 310, 951, 451))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.no_moves_label.setFont(font)
        self.no_moves_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.no_moves_label.setObjectName("no_moves_label")
        self.types_label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.types_label_2.setGeometry(QtCore.QRect(410, 30, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.types_label_2.setFont(font)
        self.types_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.types_label_2.setObjectName("types_label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pokedex"))
        self.find_entry_pushButton.setText(_translate("MainWindow", "Find Entry"))
        self.label.setText(_translate("MainWindow", "Pokemon Name"))
        self.label_2.setText(_translate("MainWindow", "Pokedex ID"))
        self.label_4.setText(_translate("MainWindow", "Moves"))
        self.label_5.setText(_translate("MainWindow", "Base Stats"))
        self.label_9.setText(_translate("MainWindow", "Abilities"))
        self.label_10.setText(_translate("MainWindow", "Height"))
        self.label_13.setText(_translate("MainWindow", "Weight"))
        self.pokemon_move_treeWidget.setSortingEnabled(False)
        self.pokemon_move_treeWidget.headerItem().setText(0, _translate("MainWindow", "Move"))
        self.pokemon_move_treeWidget.headerItem().setText(1, _translate("MainWindow", "Type"))
        self.pokemon_move_treeWidget.headerItem().setText(2, _translate("MainWindow", "Power"))
        self.pokemon_move_treeWidget.headerItem().setText(3, _translate("MainWindow", "Accuracy"))
        self.pokemon_move_treeWidget.headerItem().setText(4, _translate("MainWindow", "PP"))
        self.pokemon_move_treeWidget.headerItem().setText(5, _translate("MainWindow", "Damage Class"))
        self.pokemon_move_treeWidget.headerItem().setText(6, _translate("MainWindow", "Priority"))
        self.pokemon_move_treeWidget.headerItem().setText(7, _translate("MainWindow", "Effect"))
        self.label_15.setText(_translate("MainWindow", "HP"))
        self.label_16.setText(_translate("MainWindow", "Attack"))
        self.label_18.setText(_translate("MainWindow", "Defense"))
        self.label_20.setText(_translate("MainWindow", "Special Attack"))
        self.label_22.setText(_translate("MainWindow", "Special Defense"))
        self.label_24.setText(_translate("MainWindow", "Speed"))
        self.label_26.setText(_translate("MainWindow", "Total"))
        self.label_8.setText(_translate("MainWindow", "or"))
        self.label_11.setText(_translate("MainWindow", "ID will be preferred when both are entered"))
        self.title_label.setText(_translate("MainWindow", "Welcome to the Pokédex!"))
        self.error_label.setText(_translate("MainWindow", "Please enter a valid Name or ID"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Red Blue"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Red Blue"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Yellow"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Gold Silver"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Crystal"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Ruby Sapphire"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Emerald"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Firered Leafgreen"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Diamond Pearl"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Platinum"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Heartgold Soulsilver"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Black White"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Colosseum"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Black 2 White 2"))
        self.comboBox.setItemText(13, _translate("MainWindow", "X Y"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Omega Ruby Alpha Sapphire"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Sun Moon"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Ultra Sun Ultra Moon"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Sword Shield"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Scarlet Violet"))
        self.label_17.setText(_translate("MainWindow", "Pokemon Game"))
        self.label_14.setText(_translate("MainWindow", "and"))
        self.ability_treeWidget.headerItem().setText(0, _translate("MainWindow", "Ability"))
        self.ability_treeWidget.headerItem().setText(1, _translate("MainWindow", "Hidden"))
        self.ability_treeWidget.headerItem().setText(2, _translate("MainWindow", "Generation"))
        self.ability_treeWidget.headerItem().setText(3, _translate("MainWindow", "Flavor Text"))
        self.no_abilities_label.setText(_translate("MainWindow", "No abilities in the currently selected game."))
        self.types_label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Shows the most current competitive type for a pokemon, some pokemon might be a different type or laking their second type in earlier generations.</p></body></html>"))
        self.types_label.setText(_translate("MainWindow", "Type"))
        self.measurement_pushButton.setText(_translate("MainWindow", "📏"))
        self.label_12.setText(_translate("MainWindow", "Form"))
        self.form_comboBox.setCurrentText(_translate("MainWindow", "Default"))
        self.form_comboBox.setItemText(0, _translate("MainWindow", "Default"))
        self.form_comboBox.setItemText(1, _translate("MainWindow", "Shiny"))
        self.form_comboBox.setItemText(2, _translate("MainWindow", "Female"))
        self.form_comboBox.setItemText(3, _translate("MainWindow", "Shiny Female"))
        self.no_moves_label.setText(_translate("MainWindow", "No moves in the currently selected game."))
        self.types_label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Shows the most current competitive type for a pokemon, some pokemon might be a different type or laking their second type in earlier generations.</p></body></html>"))
        self.types_label_2.setText(_translate("MainWindow", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
