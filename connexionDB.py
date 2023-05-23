import sqlite3
class ConnexionDB():

    # Connexion à la base de donnée
    print("Connexion à projet.db")
    conn = sqlite3.connect("projet.db")