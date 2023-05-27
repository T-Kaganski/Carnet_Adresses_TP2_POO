import sqlite3
from PyQt6 import QtCore
from PyQt6.QtWidgets import QDialog, QPushButton, QGridLayout, QLabel, QLineEdit

class ModifierSupprimer(QDialog):
    def __init__(self, id):
        super().__init__()
        self.id = id

        # Créer la fenêtre de dialogue pour modifier ou supprimer enregistrement
        self.setWindowTitle("Modifier ou Supprimer un enregistrement")
        self.setGeometry(600, 325, 550, 100)

        # Permet un alignement sur la grille des widgets
        grid = QGridLayout()
        grid.setContentsMargins(20, 20, 20, 20)
        grid.setSpacing(0)
        grid.setVerticalSpacing(20)
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

        # Créer le bouton pour modifier
        self.btnValider = QPushButton("Modifier")
        self.btnValider.setFixedSize(100, 30)
        grid.addWidget(self.btnValider, 2, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.btnValider.clicked.connect(self.modifier)

        # Créer le bouton pour supprimer
        self.btnValider = QPushButton("Supprimer")
        self.btnValider.setFixedSize(100, 30)
        grid.addWidget(self.btnValider, 2, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.btnValider.clicked.connect(self.supprimer)

        # Créer le bouton pour annuler
        self.btnAnnuler = QPushButton("Annuler")
        self.btnAnnuler.setFixedSize(100, 30)
        grid.addWidget(self.btnAnnuler, 2, 2, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.btnAnnuler.clicked.connect(self.reject)




    def modifier(self):
        print("modifier les valeurs dans la table")
        conn = sqlite3.connect("projet.db")
        cursor = conn.cursor()
        req = "UPDATE Personnes SET Nom=?, Prenom=?, Mail=?, Telephone=? WHERE ID=?"
        values = (self.lineNom.text(), self.linePrenom.text(), self.lineMail.text(), self.linePhone.text(), self.id)
        cursor.execute(req, values)
        conn.commit()
        conn.close()
        self.setResult(QDialog.DialogCode.Accepted)
        self.accept()

    def supprimer(self):
        print("supprimer la ligne de la table")
        conn = sqlite3.connect("projet.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Personnes WHERE ID=?", (self.id,))
        conn.commit()
        conn.close()
        self.setResult(QDialog.DialogCode.Accepted)
        self.accept()

    def remplirChamps(self, nom, prenom, email, telephone):
        self.lineNom.setText(nom)
        self.linePrenom.setText(prenom)
        self.lineMail.setText(email)
        self.linePhone.setText(telephone)