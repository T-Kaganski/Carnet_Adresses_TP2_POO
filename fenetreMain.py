from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QHeaderView, QMessageBox
from choixCarnet import CarnetDialog


class CarnetAdresses(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Carnet d'adresses")
        self.setGeometry(300, 100, 1000, 700)
        self.setupUI()
        self.choix = CarnetDialog()
        self.choix.selectionTable.connect(self.afficherCarnet)

    def setupUI(self):
        self.qtab = QTableWidget(self)
        self.qtab.setGeometry(30, 30, 940, 600)
        self.qtab.setColumnCount(5)
        self.qtab.setRowCount(10)
        self.qtab.setHorizontalHeaderLabels(['ID', 'Nom', 'Prénom', 'Email', 'Téléphone'])
        header = self.qtab.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btnExit = QPushButton(self)
        btnExit.setText("Quitter")
        btnExit.setGeometry(770, 645, 200, 40)
        btnExit.clicked.connect(self.confirmerExit)

        btnAdd = QPushButton(self)
        btnAdd.setText("Ajouter")
        btnAdd.setGeometry(30, 645, 200, 40)
        btnAdd.clicked.connect(self.ajouterEnregistrement)

        btnCarAdd = QPushButton(self)
        btnCarAdd.setText("Carnet d'adresses")
        btnCarAdd.setGeometry(260, 645, 200, 40)
        btnCarAdd.clicked.connect(self.ouvrirChoixCarnet)

    def afficherCarnet(self, data):
        self.qtab.clearContents()  # Effacer les anciennes données de la table
        self.qtab.setRowCount(len(data))  # Définir le nombre de lignes en fonction des données

        for row_number, row_data in enumerate(data):
            for column_number, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.qtab.setItem(row_number, column_number, item)

    def ajouterEnregistrement(self):
        pass

    def ouvrirChoixCarnet(self):
        self.choix.show()

    def confirmerExit(self):
        reply = QMessageBox.question(self, "Confirmation", "Êtes-vous sûr de vouloir quitter ?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.instance().quit()
