import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QLabel, QPushButton, QVBoxLayout

class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        
        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("Pythonu seviyor musunuz ?")
        self.yazialani = QLabel("")
        self.buton = QPushButton("Bana tıkla")
        vbox = QVBoxLayout()
        vbox.addWidget(self.checkbox)
        vbox.addWidget(self.yazialani)
        vbox.addWidget(self.buton)

        self.setLayout(vbox)
        self.setWindowTitle("Checkbox")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazialani))

    

        self.show()
    def click(self,checkbox,yazi_alani):

        if checkbox:
            yazi_alani.setText("Pythonu seviyorsun çok güzel")

        else:
            yazi_alani.setText("Pythonu neden sevmiyorsun ?")
app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())