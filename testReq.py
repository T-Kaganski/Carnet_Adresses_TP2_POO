import sqlite3

print("afficher toute la table")
conn = sqlite3.connect("projet.db")
cursor = conn.cursor()
# requette ici
cursor.execute("SELECT * FROM Étudiants")
resultat = cursor.fetchall()
conn.commit()
for item in resultat:
    print(item)

conn.close()