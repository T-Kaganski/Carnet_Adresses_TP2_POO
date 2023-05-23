import sqlite3
from PyQt6 import QtCore
from PyQt6.QtWidgets import QDialog, QGridLayout, QPushButton, QLineEdit


class CreationCarnetDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Créer la fenêtre de dialogue Création d'un nouveau carnet d'adresses
        self.setWindowTitle("Création d'un carnet d'adresses")
        self.setGeometry(625, 275, 400, 200)

        # Permet un alignement sur la grille des widgets
        grid = QGridLayout()
        self.setLayout(grid)

        # Créer le champ pour le nom
        self.champNom = QLineEdit()
        self.champNom.setFixedSize(250, 50)
        grid.addWidget(self.champNom, 0, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)

        # Créer le bouton pour créer le nouveau carnet
        self.btnCreer = QPushButton("Créer")
        self.btnCreer.setFixedSize(100, 50)
        grid.addWidget(self.btnCreer, 1, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.btnCreer.clicked.connect(self.CreerTable)

        # Créer le bouton pour annuler
        self.btnAnnuler = QPushButton("Annuler")
        self.btnAnnuler.setFixedSize(100, 50)
        grid.addWidget(self.btnAnnuler, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.btnAnnuler.clicked.connect(self.reject)

    def CreerTable(self):
        print("création nouveau carnet")
        conn = sqlite3.connect("projet.db")

        req = "CREATE TABLE IF NOT EXISTS "+self.champNom.text()+"(PersonID INTEGER PRIMARY KEY AUTOINCREMENT,Nom varchar(25),Prenom varchar(25),Mail varchar(40),Telephone varchar(25));"

        cursor = conn.cursor()
        cursor.execute(req)
        conn.close()

        self.close()