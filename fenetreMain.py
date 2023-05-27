import sqlite3
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QHeaderView, QMessageBox, QScrollArea, \
    QDialog
from ajouter import Ajouter
from modifierSupprimer import ModifierSupprimer


class CarnetAdresses(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Carnet d'adresses")
        self.setGeometry(300, 100, 1000, 590)
        self.setupUI()
        self.contenuLigne = None
        self.qtab.cellClicked.connect(self.selectionner)

    def afficherCarnet(self):  # Afficer le contenu du carnet d'adresse
        print("afficher le carnet d'adresses")
        conn = sqlite3.connect("projet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Personnes")
        resultat = cursor.fetchall()
        conn.commit()
        conn.close()

        self.qtab.clearContents()  # Effacer les anciennes données de la table
        self.qtab.setRowCount(len(resultat))  # Définir le nombre de lignes en fonction des données

        # Remplir la table avec les données
        for row_number, row_data in enumerate(resultat):
            for column_number, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.qtab.setItem(row_number, column_number, item)

    def connexionDb(self): # Connexion à la base de données et affichage du carnet d'adresses
        print("Connexion à projet.db")
        conn = sqlite3.connect("projet.db")
        self.creerTable()
        print("Table créée)")
        self.afficherCarnet()
        print("Carnet affiché")


    def creerTable(self): # Création de la table Personnes si elle n'existe pas
        print("création nouveau carnet")
        conn = sqlite3.connect("projet.db")
        req = "CREATE TABLE IF NOT EXISTS Personnes (ID INTEGER PRIMARY KEY AUTOINCREMENT,Nom varchar(25),Prenom varchar(25),Mail varchar(40),Telephone varchar(25));"
        cursor = conn.cursor()
        cursor.execute(req)
        conn.close()

    def setupUI(self):

        # création de la fenêtre avec ses colonnes et une barre de defilement
        self.scroll = QScrollArea(self)
        self.scroll.setGeometry(30, 60, 940, 450)
        self.qtab = QTableWidget()
        self.scroll.setWidget(self.qtab)
        self.scroll.setWidgetResizable(True)
        self.qtab.setColumnCount(5)
        self.qtab.setHorizontalHeaderLabels(['ID', 'Nom', 'Prénom', 'Email', 'Téléphone'])
        header = self.qtab.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # créer un bouton connexionDb
        btnDb = QPushButton(self)
        btnDb.setText("ConnexionDB / Afficher")
        btnDb.setGeometry(30, 10, 200, 40)
        btnDb.clicked.connect(self.connexionDb)

        # créer un bouton ajouter un enregistrement
        btnAdd = QPushButton(self)
        btnAdd.setText("Ajouter")
        btnAdd.setGeometry(30, 530, 200, 40)
        btnAdd.clicked.connect(self.ajouterEnregistrement)

        # créer un bouton Quitter
        btnExit = QPushButton(self)
        btnExit.setText("Quitter")
        btnExit.setGeometry(770, 530, 200, 40)
        btnExit.clicked.connect(self.confirmerExit)

    def ajouterEnregistrement(self): # ouvre la fenêtre de dialogue pour l'ajout d'un enregistrement
        fenInserer = Ajouter()
        if fenInserer.exec() == QDialog.DialogCode.Accepted:
            self.afficherCarnet()

    def selectionner(self, row, column):
        self.contenuLigne = self.qtab.item(row, column).text()

        # Récupérer l'ID de la ligne sélectionnée (première colonne)
        id_ligne = int(self.qtab.item(row, 0).text())

        # Récupérer les valeurs depuis la base de données en utilisant l'ID
        valeurs = self.recupererValeursDepuisDb(id_ligne)

        # ouvre la fenêtre de dialogue pour la modification ou la suppression de la ligne
        fenModifier = ModifierSupprimer(id_ligne)
        fenModifier.remplirChamps(*valeurs)  # Passe les valeurs séparées avec l'opérateur *
        if fenModifier.exec() == QDialog.DialogCode.Accepted:
            self.afficherCarnet()

    def recupererValeursDepuisDb(self, id_ligne): # Récupérer les valeurs de la ligne avec l'ID correspondant
        conn = sqlite3.connect("projet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Nom, Prenom, Mail, Telephone FROM Personnes WHERE ID = ?", (id_ligne,))
        resultat = cursor.fetchone()
        conn.close()
        return resultat


    def confirmerExit(self): # Vérifier si l'utilisateur veut vraiment quitter
        reply = QMessageBox.question(self, "Confirmation", "Êtes-vous sûr de vouloir quitter ?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.instance().quit()