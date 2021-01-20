from PyQt5 import QtWidgets

import sys 

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        
        super().__init__()
        
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Func")

        self.yazialani = QtWidgets.QLabel("Bana henüz tıklanmadı.....")

        self.buton = QtWidgets.QPushButton("Bana tıkla......")

        self.say = 0

        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(self.buton)

        vbox.addWidget(self.yazialani)

        vbox.addStretch()

        hbox = QtWidgets.QHBoxLayout()

        hbox.addStretch()

        hbox.addLayout(vbox)

        hbox.addStretch()

        self.buton.clicked.connect(self.click)

        self.setLayout(hbox)

        self.show()

    def click(self):

        self.say += 1

        self.yazialani.setText("Bana "+str(self.say)+" defa tıklandı.")



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())

