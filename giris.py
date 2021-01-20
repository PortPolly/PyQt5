import sys #Gerekli olan modülleri dahil ediyoruz  

import sqlite3 #Gerekli olan modülleri dahil ediyoruz

from PyQt5 import QtWidgets #Gerekli olan modülleri dahil ediyoruz

class Pencere(QtWidgets.QWidget): #Pencere sınıfını oluştururken miras almak istediğimiz sınıfı yazıyoruz

    def __init__(self): #Objemizin özelliklerini tanımlıyoruz

        super().__init__() #Miras aldığımız sınıfın özelliklerini çağırıyoruz 
    
        self.baglantiolustur() #Database ile bağlantı kurmak için bir fonksiyon tanımlıyoruz

        self.init_ui() #Sınıfa eklemek istediğimiz ekstra özellikleri oluşturabilmek için bir fonksiyon tanımlıyoruz

    def init_ui(self): #Oluşturduğumuz fonksiyonumuzun özelliklerini tanımlıyoruz

        self.kullanici_adi = QtWidgets.QLineEdit() #Kullanıcıdan veri alabilmek için arayüzümüzde bir input oluşturuyoruz

        self.sifre = QtWidgets.QLineEdit() #Kullanıcıdan veri alabilmek için arayüzümüzde bir input oluşturuyoruz

        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password) #Kullanıcı şifresini girerken karakterlerin gizlenmesi için parola modunu kullanıyoruz
        
        self.giris = QtWidgets.QPushButton("Giriş yap") #Giriş yapma işlemi için bir buton oluşturuyoruz

        self.yazialani = QtWidgets.QLabel("") #Ekrana yazdırma işlemi yapabilmek için bir yazı alanı oluşturuyoruz
        self.register = QtWidgets.QPushButton("Kayıt ol")
        vbox = QtWidgets.QVBoxLayout() #Bir tane vertical box layout oluşturuyoruz

        vbox.addWidget(self.kullanici_adi) #Kullanıcı adı elementimizi arayüzümüze ekliyoruz

        vbox.addWidget(self.sifre) #Şifre elementimizi arayüzümüze ekliyoruz

        vbox.addWidget(self.yazialani) #Yazı alanı elementimizi arayüzümüze ekliyoruz

        vbox.addStretch() #Layoutumuza boşluk ekliyoruz

        vbox.addWidget(self.giris) #Giriş yapmak için oluşturduğumuz butonumuzu ekliyoruz
        vbox.addWidget(self.register)
        hbox = QtWidgets.QHBoxLayout() #Bir tane horizontal box layout oluşturuyoruz

        hbox.addStretch() #Layoutumuza boşluk ekliyoruz

        hbox.addLayout(vbox) #Layoutumuza önceden oluşturduğumuz vertical layoutumuzu ekliyoruz

        hbox.addStretch() #Layoutumuza boşluk ekliyoruz

        self.setLayout(hbox) #Arayüzümüze oluşturduğumuz layoutumuzu yerleştiriyoruz

        self.giris.clicked.connect(self.login) #Butonumuzu bir fonksiyona bağlıyoruz
        self.register.clicked.connect(self.kayit)

        self.setWindowTitle("Kullanıcı girişi") #Oluşturduğumuz pencereye bir isim veriyoruz

        self.setGeometry(100,100,500,500) #Penceremizin boyutunu ve konumunu ayarlıyoruz

        self.show() #Penceremizdeki elementleri gösteriyoruz
    
    def baglantiolustur(self): #Oluşturduğumuz fonksiyonumuzun özelliklerini tanımlıyoruz

        baglanti = sqlite3.connect("Database.db") #Database'imizi oluşturuyoruz varsa da bağlantımızı kuruyoruz

        self.cursor = baglanti.cursor() #Database'imiz üstünde işlem yapabilmek için bir imleç oluşturuyoruz

        self.cursor.execute("Create table if not exists üyeler (Kullanıcı_adı TEXT,Parola TEXT)") #Database içerisine bir tablo oluşturuyoruz

        baglanti.commit() #Yaptığımız işlemleri kaydediyoruz

    def login(self): #Butonumuza tanımladığımız fonksiyonun özelliklerini yazıyoruz

        adi = self.kullanici_adi.text() #Kullanıcının girdiği kullanıcı adını alıyoruz

        sifresi = self.sifre.text() #Kullanıcının girdiği şifreyi alıyoruz

        self.cursor.execute("Select * from üyeler where Kullanıcı_adı = ? and Parola = ?",(adi,sifresi)) #Database sorgumuzu yapıyoruz

        data = self.cursor.fetchall() #Seçtiğimiz verileri çekiyoruz

        if len(data) == 0 : #Listenin uzunluğuna göre sonuç veren bir if sorgusu

            self.yazialani.setText("Böyle bir kullanıcı yoktur\nLütfen tekrar deneyin.....") #Print işlemini yaptırıyoruz

        else:
            self.yazialani.setText("Hoşgeldiniz "+adi) #Print işlemini yaptırıyoruz

    def kayit(self):
        adi = self.kullanici_adi.text()

        sifresi = self.sifre.text()
        self.cursor.execute("Select * from üyeler where Kullanıcı_adı = ?",(adi,))

        sorgu = self.cursor.fetchall()



        if len(sorgu) == 0:

            self.cursor.execute("Insert into üyeler values(?,?)",(adi,sifresi))
            self.yazialani.setText("Sisteme başarıyla kaydedildi.\nKullanıcı adınız : {}\nŞifreniz {}".format(adi,sifresi))

        else:
            self.yazialani.setText("Böyle bir kullanıcı hali hazırda bulunmaktadır. Lütfen başka bir kullanıcı adı seçiniz.")
        
app = QtWidgets.QApplication(sys.argv) #Uygulamamızı oluşturuyoruz

pencere = Pencere() #Pencere sınıfından bir obje oluşturuyoruz

sys.exit(app.exec()) #Programımızın kapanmaması için sonsuz döngüye sokuyoruz