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
        MainWindow.resize(583, 770)
        MainWindow.setMinimumSize(QtCore.QSize(583, 770))
        MainWindow.setMaximumSize(QtCore.QSize(583, 770))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.find_entry_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.find_entry_pushButton.setGeometry(QtCore.QRect(120, 170, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.find_entry_pushButton.setFont(font)
        self.find_entry_pushButton.setObjectName("find_entry_pushButton")
        self.pokedex_id_entry = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pokedex_id_entry.setGeometry(QtCore.QRect(140, 90, 151, 20))
        self.pokedex_id_entry.setObjectName("pokedex_id_entry")
        self.pokemon_name_entry = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pokemon_name_entry.setGeometry(QtCore.QRect(140, 50, 151, 20))
        self.pokemon_name_entry.setObjectName("pokemon_name_entry")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.sprite_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.sprite_label.setGeometry(QtCore.QRect(340, 30, 161, 151))
        self.sprite_label.setText("")
        self.sprite_label.setPixmap(QtGui.QPixmap(".\\../../Downloads/52.png"))
        self.sprite_label.setScaledContents(True)
        self.sprite_label.setObjectName("sprite_label")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 280, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 280, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 500, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 500, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.listWidget_5 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(30, 520, 256, 192))
        self.listWidget_5.setObjectName("listWidget_5")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.height_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.height_label.setGeometry(QtCore.QRect(180, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.height_label.setFont(font)
        self.height_label.setObjectName("height_label")
        self.weight_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.weight_label.setGeometry(QtCore.QRect(180, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.weight_label.setFont(font)
        self.weight_label.setObjectName("weight_label")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(70, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(30, 300, 256, 192))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.hp_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.hp_label.setGeometry(QtCore.QRect(440, 310, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hp_label.setFont(font)
        self.hp_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hp_label.setObjectName("hp_label")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(330, 310, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(330, 330, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.attack_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.attack_label.setGeometry(QtCore.QRect(440, 330, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.attack_label.setFont(font)
        self.attack_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.attack_label.setObjectName("attack_label")
        self.label_18 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(330, 350, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.defense_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.defense_label.setGeometry(QtCore.QRect(440, 350, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.defense_label.setFont(font)
        self.defense_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.defense_label.setObjectName("defense_label")
        self.label_20 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(330, 370, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.special_attack_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.special_attack_label.setGeometry(QtCore.QRect(440, 370, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.special_attack_label.setFont(font)
        self.special_attack_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.special_attack_label.setObjectName("special_attack_label")
        self.label_22 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(330, 390, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.special_defense_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.special_defense_label.setGeometry(QtCore.QRect(440, 390, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.special_defense_label.setFont(font)
        self.special_defense_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.special_defense_label.setObjectName("special_defense_label")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(330, 410, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.speed_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.speed_label.setGeometry(QtCore.QRect(440, 410, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.speed_label.setFont(font)
        self.speed_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.speed_label.setObjectName("speed_label")
        self.label_26 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(330, 450, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.stat_total_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.stat_total_label.setGeometry(QtCore.QRect(440, 450, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stat_total_label.setFont(font)
        self.stat_total_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stat_total_label.setObjectName("stat_total_label")
        self.treeWidget_2 = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.treeWidget_2.setGeometry(QtCore.QRect(300, 520, 256, 192))
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 110, 251, 31))
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 190, 43, 13))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.form_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.form_frame.setEnabled(True)
        self.form_frame.setGeometry(QtCore.QRect(360, 180, 120, 80))
        self.form_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.form_frame.setObjectName("form_frame")
        self.male_pushButton = QtWidgets.QPushButton(parent=self.form_frame)
        self.male_pushButton.setGeometry(QtCore.QRect(10, 30, 41, 41))
        self.male_pushButton.setObjectName("male_pushButton")
        self.female_pushButton = QtWidgets.QPushButton(parent=self.form_frame)
        self.female_pushButton.setGeometry(QtCore.QRect(70, 30, 41, 41))
        self.female_pushButton.setObjectName("female_pushButton")
        self.label_12 = QtWidgets.QLabel(parent=self.form_frame)
        self.label_12.setGeometry(QtCore.QRect(30, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(40, 140, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: red")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("error_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 21))
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
        self.label_6.setText(_translate("MainWindow", "Games/Locations"))
        self.label_9.setText(_translate("MainWindow", "Abilities"))
        self.label_10.setText(_translate("MainWindow", "Height"))
        self.height_label.setText(_translate("MainWindow", "TextLabel"))
        self.weight_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "Weight"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Moves"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Level Up Moves"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Move 1"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Learned Moves"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "move 2"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Egg Moves"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "move 3"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(4).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(5).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(6).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(7).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(8).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(9).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(10).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(11).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(12).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(13).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(14).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).child(15).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.hp_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "HP"))
        self.label_16.setText(_translate("MainWindow", "Attack"))
        self.attack_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "Defense"))
        self.defense_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "Special Attack"))
        self.special_attack_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_22.setText(_translate("MainWindow", "Special Defense"))
        self.special_defense_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_24.setText(_translate("MainWindow", "Speed"))
        self.speed_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_26.setText(_translate("MainWindow", "Total"))
        self.stat_total_label.setText(_translate("MainWindow", "TextLabel"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "Games"))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "Encounter Rate"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("MainWindow", "Game1"))
        self.treeWidget_2.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Location"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("MainWindow", "Game2"))
        self.treeWidget_2.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "route"))
        self.treeWidget_2.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "3"))
        self.treeWidget_2.topLevelItem(1).child(0).child(0).setText(1, _translate("MainWindow", "day: 50% "))
        self.treeWidget_2.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("MainWindow", "Game3"))
        self.treeWidget_2.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Location"))
        self.treeWidget_2.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(3).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(4).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(5).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(6).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(7).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(8).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(9).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(10).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(11).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(12).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(13).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(14).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.topLevelItem(2).child(15).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "or"))
        self.label_11.setText(_translate("MainWindow", "ID will be preferred when both are entered"))
        self.male_pushButton.setText(_translate("MainWindow", "M"))
        self.female_pushButton.setText(_translate("MainWindow", "F"))
        self.label_12.setText(_translate("MainWindow", "Form"))
        self.label_3.setText(_translate("MainWindow", "Welcome to the Pokedex!"))
        self.error_label.setText(_translate("MainWindow", "Please enter a valid ID or Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
