# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:22:45 2017

@author: AA82758
"""


import sys; import numpy as np;
from PyQt5 import uic, QtWidgets
 
qtCreatorFile = "vsc.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calcul.clicked.connect(self.Calculate_price)
    def Calculate_price(self):
        adultes = int(self.adultes_sbox.value())
        enfants = int(self.enfants_sbox.value())
        formule = (self.formule_cbox.currentIndex())
        rooms = np.ceil(adultes/2)
        d_arivee=self.calendar_arivee.selectedDate()
        d_depart=self.calendar_depart.selectedDate()
        nombre_jours=d_arivee.daysTo(d_depart)
        
        if formule == 0:
            if adultes > 1.1:
                total_price = str(adultes *60) 
                self.prix_total.setText(total_price)
                self.chambres.setText(str(nombre_jours))
            else:
                total_price = str(adultes *70) 
                self.prix_total.setText(total_price)
                self.chambres.setText(str(rooms))


        elif formule ==1:
            if adultes > 1.1:
                total_price = str(adultes *54) 
                self.prix_total.setText(total_price)
                self.chambres.setText(str(rooms))
            else:
                total_price = str(adultes *64) 
                self.prix_total.setText(total_price)
                self.chambres.setText(str(rooms))
        elif formule == 2:
            if adultes > 1.1:
                total_price = str(adultes *40) 
                self.prix_total.setText(total_price)
                self.chambres.setText(str(rooms))
            else:
                total_price = str(adultes *50) 
                self.prix_total.setText(total_price)
                self.chambres.setText(str(rooms))
            
if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
