import sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazialani = QtWidgets.QLineEdit()

        self.temizle = QtWidgets.QPushButton("Temizle")

        self.yazdir = QtWidgets.QPushButton("Yazdır")

        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(self.yazialani)

        vbox.addWidget(self.temizle)

        vbox.addWidget(self.yazdir)

        vbox.addStretch()

        self.setLayout(vbox)

        self.temizle.clicked.connect(self.click)

        self.yazdir.clicked.connect(self.click)

        self.show()

    def click(self):

        sender = self.sender()

        if(sender.text() == "Temizle"):

            self.yazialani.clear()

        else:

            print(self.yazialani.text())



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())


