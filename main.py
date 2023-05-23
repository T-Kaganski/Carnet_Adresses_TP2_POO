import sqlite3
from PyQt6.QtWidgets import QApplication
from choixCarnet import CarnetDialog
from fenetreMain import CarnetAdresses
from connexionDB import ConnexionDB

if __name__ == "__main__":
    # Créer une instance de QApplication
    app = QApplication([])

    # Connexion à la base de donnée
    db = ConnexionDB()
    # Créer une instance de la fenêtre principale du carnet d'adresses
    fenMain = CarnetAdresses()
    # Créer une instance de la fenêtre de dialogue pour choisir le carnet
    fenChoixCarnet = CarnetDialog()

    # Lancer l'application
    fenMain.show()
    fenChoixCarnet.show()

    app.exec()
