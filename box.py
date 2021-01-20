import sys

from PyQt5 import QtWidgets, QtGui



def Pencere():
    

    app = QtWidgets.QApplication(sys.argv)


    pencere = QtWidgets.QWidget()

    

    pencere.setWindowTitle("Box")

    okay = QtWidgets.QPushButton("Tamam")

    no = QtWidgets.QPushButton("İptal")

    hbox = QtWidgets.QHBoxLayout()

    hbox.addStretch()

    hbox.addWidget(okay)
    
    hbox.addWidget(no)

    vbox = QtWidgets.QVBoxLayout()

    vbox.addStretch()

    vbox.addLayout(hbox)

    

    pencere.setLayout(vbox)


    etiket1 = QtWidgets.QLabel(pencere)

    etiket2 = QtWidgets.QLabel(pencere)

    etiket2.setPixmap(QtGui.QPixmap("python.png"))

    etiket1.setText("Ozanın kutucuğu")

    etiket1.move(200,30)

    etiket2.move(70,100)

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())


Pencere()