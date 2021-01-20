import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout

class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        
        self.init_ui()
    def init_ui(self):
        self.yazialani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        vbox = QVBoxLayout()
        vbox.addWidget(self.yazialani)
        vbox.addWidget(self.temizle)
        self.setWindowTitle("Yazı alanı")
        self.temizle.clicked.connect(self.click)
        self.setLayout(vbox)
        self.show()


    def click(self):
        self.yazialani.clear()








app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())