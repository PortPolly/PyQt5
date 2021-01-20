import sys
from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QPushButton, QVBoxLayout

class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        
        self.init_ui()
    def init_ui(self):

        self.radioyazi = QLabel("Hangi dili daha çok seviyorsun ?")

        self.java = QRadioButton("Java")
        self.py = QRadioButton("Python")
        self.php = QRadioButton("PHP")
        self.yazi = QLabel("")
        self.buton = QPushButton("Gönder")
        vbox = QVBoxLayout()
        vbox.addWidget(self.radioyazi)
        vbox.addWidget(self.java)
        vbox.addWidget(self.py)
        vbox.addWidget(self.php)
        vbox.addStretch()
        vbox.addWidget(self.yazi)
        vbox.addWidget(self.buton)
        self.setLayout(vbox)
        self.setWindowTitle("Radiobutton")
        self.setGeometry(300,100,500,500)
        self.buton.clicked.connect(lambda: self.click(self.java.isChecked(),self.py.isChecked(),self.php.isChecked(),self.yazi))
        self.show()

    def click(self,java,py,php,yazi):
        if java:
            yazi.setText("Javayı seçtiniz")
        elif py:
            yazi.setText("Pythonu seçtiniz")
        else:
            yazi.setText("PHPyi seçtiniz")












app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())