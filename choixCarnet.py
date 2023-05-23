import sqlite3
from PyQt6 import QtCore
from PyQt6.QtWidgets import QDialog, QComboBox, QPushButton, QGridLayout
from creationCarnet import CreationCarnetDialog

class CarnetDialog(QDialog):
    selectionTable = QtCore.pyqtSignal(list)
    def __init__(self):
        super().__init__()

        # Créer la fenêtre de dialogue Choix du carnet d'adresses
        self.setWindowTitle("Choix du carnet d'adresses")
        self.setGeometry(625, 275, 400, 200)

        # Permet un alignement sur la grille des widgets
        grid = QGridLayout()
        self.setLayout(grid)

        # Créer le combobox
        self.comboBox = QComboBox()
        self.comboBox.setFixedSize(250,50)
        grid.addWidget(self.comboBox, 0, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        conn = sqlite3.connect("projet.db")
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
        res = cursor.fetchall()

        nomsComboBox = [table[0] for table in res]
        self.comboBox.addItems(nomsComboBox)

        # Créer le bouton pour valider
        self.btnValider = QPushButton("Valider")
        self.btnValider.setFixedSize(100, 50)
        grid.addWidget(self.btnValider, 0, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.btnValider.clicked.connect(self.selectionnerCarnet)

        # Créer le bouton pour ajouter un nouveau carnet
        self.btnAjouter = QPushButton("Nouveau carnet")
        self.btnAjouter.setFixedSize(250, 50)
        grid.addWidget(self.btnAjouter, 1, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.btnAjouter.clicked.connect(self.ouvrirCreationCarnetDialog)

    def ouvrirCreationCarnetDialog(self):
        self.creationCarnet = CreationCarnetDialog()
        self.creationCarnet.show()
        self.close()

    def selectionnerCarnet(self):
        nomTable = self.comboBox.currentText()
        data = self.recupererDonneesCarnet(nomTable)
        self.selectionTable.emit(data)
        self.close()

    def recupererDonneesCarnet(self, nomTable):
        conn = sqlite3.connect("projet.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {nomTable}")
        return cursor.fetchall()