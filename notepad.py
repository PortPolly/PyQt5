import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog,QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import qApp, QAction,QMainWindow
class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        
        self.init_ui()
    def init_ui(self):
        self.yazialani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("Kaydet")
        hbox = QHBoxLayout()
        hbox.addWidget(self.temizle)
        hbox.addWidget(self.ac)
        hbox.addWidget(self.kaydet)
        vbox = QVBoxLayout()
        vbox.addWidget(self.yazialani)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setWindowTitle("Notepad")
        
        self.temizle.clicked.connect(self.yazitemizle)
        self.ac.clicked.connect(self.dosyaac)
        self.kaydet.clicked.connect(self.dosyakaydet)

    def yazitemizle(self):
        self.yazialani.clear()

    def dosyaac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya aç",os.getenv("HOME"))
        try: 
            with open(dosya_ismi[0],"r",encoding="utf-8") as file:
                self.yazialani.setText(file.read())
        except:
            pass

    def dosyakaydet(self):
        dosyaismi = QFileDialog.getSaveFileName(self,"Dosya kaydet",os.getenv("HOME"))
        try:
            with open(dosyaismi[0],"w",encoding="utf-8") as file:
                file.write(self.yazialani.toPlainText())
        except:
            pass

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.pencere = Notepad()
        self.setCentralWidget(self.pencere)
    
        self.menuleriolustur()
    def menuleriolustur(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        dosyaac = QAction("Dosya aç",self)
        dosyaac.setShortcut("ctrl+o")

        dosyakaydet = QAction("Dosya kaydet",self)
        dosyakaydet.setShortcut("Ctrl+S")
        temizle = QAction("Dosyayı temizle",self)
        temizle.setShortcut("Ctrl+D")
        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+q")
        dosya.addAction(dosyaac)
        dosya.addAction(dosyakaydet)
        
        
        dosya.addAction(temizle)
        dosya.addAction(cikis)
        self.setWindowTitle("Text Editor")
        dosya.triggered.connect(self.response)
      
        self.show()
    def response(self,action):
        if action.text() == "Dosya aç":
            print("Dosya aça basıldı")
            self.pencere.dosyaac()
        elif action.text() == "Dosya kaydet":
            print("Dosya kaydete basıldı")
            self.pencere.dosyakaydet()
        elif action.text()== "Dosyayı temizle":
            print("Dosyayı temizleye basıldı")
            self.pencere.yazitemizle()
        elif action.text()=="Çıkış":
            print("Çıkışa basıldı")
            qApp.quit()






app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())