import sqlite3
from PyQt6.QtWidgets import QApplication
from ajouter import Ajouter
from fenetreMain import CarnetAdresses

if __name__ == "__main__":
    # Créer une instance de QApplication
    app = QApplication([])

    # Créer une instance de la fenêtre principale du carnet d'adresses
    fenMain = CarnetAdresses()

    # Lancer l'application
    fenMain.show()
    app.exec()
