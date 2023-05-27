import sqlite3
from PyQt6 import QtCore
from PyQt6.QtWidgets import QDialog, QPushButton, QGridLayout, QLabel, QLineEdit

class Ajouter(QDialog):
    def __init__(self):
        super().__init__()

        # Créer la fenêtre de dialogue d'ajout d'enregistrement au carnet d'adresses
        self.setWindowTitle("Ajouter au carnet d'adresses")
        self.setGeometry(600, 325, 550, 200)

        # Permet un alignement sur la grille des widgets
        grid = QGridLayout()
        grid.setContentsMargins(20, 0, 20, 20)
        grid.setSpacing(0)
        grid.setVerticalSpacing(5)
        self.setLayout(grid)

        # Créer les labels
        self.labelNom = QLabel("Nom")
        self.labelNom.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.labelNom, 0, 0, QtCore.Qt.AlignmentFlag.AlignLeft)

        self.labelPrenom = QLabel("Prénom")
        self.labelPrenom.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.labelPrenom, 0, 1, QtCore.Qt.AlignmentFlag.AlignLeft)

        self.labelMail = QLabel("Email")
        self.labelMail.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.labelMail, 0, 2, QtCore.Qt.AlignmentFlag.AlignLeft)

        self.labelPhone = QLabel("Téléphone")
        self.labelPhone.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.labelPhone, 0, 3, QtCore.Qt.AlignmentFlag.AlignLeft)

        # Créer les QLineEdit
        self.lineNom = QLineEdit()
        self.lineNom.setFixedHeight(30)
        self.lineNom.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.lineNom, 1, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelNom.setBuddy(self.lineNom)

        self.linePrenom = QLineEdit()
        self.linePrenom.setFixedHeight(30)
        self.linePrenom.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.linePrenom, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelPrenom.setBuddy(self.linePrenom)

        self.lineMail = QLineEdit()
        self.lineMail.setFixedHeight(30)
        self.lineMail.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.lineMail, 1, 2, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelMail.setBuddy(self.lineMail)

        self.linePhone = QLineEdit()
        self.linePhone.setFixedHeight(30)
        self.linePhone.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.linePhone, 1, 3, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelPhone.setBuddy(self.linePhone)

        # Créer le bouton pour valider
        self.btnValider = QPushButton("Valider")
        self.btnValider.setFixedSize(100, 50)
        grid.addWidget(self.btnValider, 2, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.btnValider.clicked.connect(self.inserer)

        # Créer le bouton pour annuler
        self.btnAnnuler = QPushButton("Annuler")
        self.btnAnnuler.setFixedSize(100, 50)
        grid.addWidget(self.btnAnnuler, 2, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.btnAnnuler.clicked.connect(self.reject)



    def inserer(self): # Insérer les valeurs entrées dans la base de données
        print("inserer dans la table")
        conn = sqlite3.connect("projet.db")
        cursor = conn.cursor()
        req = "INSERT INTO Personnes (Nom ,Prenom ,Mail, Telephone) VALUES (?, ?, ?, ?)"
        values = (self.lineNom.text(), self.linePrenom.text(), self.lineMail.text(), self.linePhone.text())
        cursor.execute(req, values)
        conn.commit()
        conn.close()
        self.setResult(QDialog.DialogCode.Accepted)
        self.accept()
