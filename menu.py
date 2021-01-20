import sys
from PyQt5.QtWidgets import QWidget, QApplication, qApp, QAction,QMainWindow

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")
        self.setWindowTitle("Menüler")
        dosyaac = QAction("Dosya aç",self)
        dosyaac.setShortcut("Ctrl+O")
        dosyakaydet = QAction("Dosya kaydet",self)
        cikis = QAction("Çıkış",self)
        dosyakaydet.setShortcut("Ctrl+S")
        cikis.setShortcut("ctrl+q")
        dosya.addAction(dosyaac)
        dosya.addAction(dosyakaydet)
        dosya.addAction(cikis)
        aravedeistir = duzenle.addMenu("Ara ve değiştir")
        ara = QAction("Ara",self)
        ara.setShortcut("Ctrl+F")
        temizle = QAction("Temizle",self)
        duzenle.addAction(temizle)
        değiştir = QAction("Değiştir",self)
        aravedeistir.addAction(ara)
        aravedeistir.addAction(değiştir)
        cikis.triggered.connect(self.cikisyap)
        dosya.triggered.connect(self.response)   
        self.show()
    def cikisyap(self):

        qApp.quit()
    def response(self,action):

        if action.text() == "Dosya aç":
            print("Dosya aça basıldı")
        elif action.text() == "Dosya kaydet":
            print("Dosya kaydete basıldı")
        elif action.text() == "Çıkış":
            print("Çıkış yapıldı")

        pass
app = QApplication(sys.argv)
pencere = Menu()
sys.exit(app.exec_())