# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vsc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 725)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Public/Pictures/Sample Pictures/SAINT CAMILLE_FICHE VACANCES_V4 - PDF-XChange Viewer_2017-06-23_22-52-28.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calcul = QtWidgets.QPushButton(self.centralwidget)
        self.calcul.setGeometry(QtCore.QRect(300, 610, 261, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calcul.setFont(font)
        self.calcul.setObjectName("calcul")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 580, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.prix_total = QtWidgets.QTextEdit(self.centralwidget)
        self.prix_total.setGeometry(QtCore.QRect(630, 610, 104, 41))
        self.prix_total.setObjectName("prix_total")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 440, 441, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.adultes_sbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.adultes_sbox.setMinimum(1)
        self.adultes_sbox.setMaximum(51)
        self.adultes_sbox.setProperty("value", 1)
        self.adultes_sbox.setObjectName("adultes_sbox")
        self.horizontalLayout_2.addWidget(self.adultes_sbox)
        self.formule_cbox = QtWidgets.QComboBox(self.layoutWidget)
        self.formule_cbox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.formule_cbox.setObjectName("formule_cbox")
        self.formule_cbox.addItem("")
        self.formule_cbox.addItem("")
        self.formule_cbox.addItem("")
        self.horizontalLayout_2.addWidget(self.formule_cbox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 410, 681, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 50, 871, 238))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.calendar_arivee = QtWidgets.QCalendarWidget(self.layoutWidget2)
        self.calendar_arivee.setObjectName("calendar_arivee")
        self.horizontalLayout_3.addWidget(self.calendar_arivee)
        self.calendar_depart = QtWidgets.QCalendarWidget(self.layoutWidget2)
        self.calendar_depart.setObjectName("calendar_depart")
        self.horizontalLayout_3.addWidget(self.calendar_depart)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 871, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 580, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.chambres = QtWidgets.QTextEdit(self.centralwidget)
        self.chambres.setGeometry(QtCore.QRect(120, 610, 104, 41))
        self.chambres.setObjectName("chambres")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 660, 211, 16))
        self.label_8.setObjectName("label_8")
        self.nb_nuits = QtWidgets.QTextEdit(self.centralwidget)
        self.nb_nuits.setGeometry(QtCore.QRect(500, 300, 104, 31))
        self.nb_nuits.setObjectName("nb_nuits")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 310, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(780, 440, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(780, 470, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(780, 500, 71, 16))
        self.label_12.setObjectName("label_12")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(530, 440, 231, 82))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.enfants_sbox_15 = QtWidgets.QSpinBox(self.widget)
        self.enfants_sbox_15.setMaximum(21)
        self.enfants_sbox_15.setObjectName("enfants_sbox_15")
        self.verticalLayout.addWidget(self.enfants_sbox_15)
        self.enfants_sbox_9 = QtWidgets.QSpinBox(self.widget)
        self.enfants_sbox_9.setMaximum(21)
        self.enfants_sbox_9.setObjectName("enfants_sbox_9")
        self.verticalLayout.addWidget(self.enfants_sbox_9)
        self.enfants_sbox_3 = QtWidgets.QSpinBox(self.widget)
        self.enfants_sbox_3.setMaximum(21)
        self.enfants_sbox_3.setObjectName("enfants_sbox_3")
        self.verticalLayout.addWidget(self.enfants_sbox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calcul.setText(_translate("MainWindow", "Calcul"))
        self.label_6.setText(_translate("MainWindow", "Prix total"))
        self.formule_cbox.setCurrentText(_translate("MainWindow", "Pension complete"))
        self.formule_cbox.setItemText(0, _translate("MainWindow", "Pension complete"))
        self.formule_cbox.setItemText(1, _translate("MainWindow", "Demi pension"))
        self.formule_cbox.setItemText(2, _translate("MainWindow", "Bed and breakfast"))
        self.label_3.setText(_translate("MainWindow", "Adultes"))
        self.label_5.setText(_translate("MainWindow", "Formule"))
        self.label_4.setText(_translate("MainWindow", "Enfants"))
        self.label.setText(_translate("MainWindow", "Date d\'arivee"))
        self.label_2.setText(_translate("MainWindow", "Date de depart"))
        self.label_7.setText(_translate("MainWindow", "Chambres"))
        self.label_8.setText(_translate("MainWindow", "Created by MONFERRATO Saverio "))
        self.label_9.setText(_translate("MainWindow", "Nombre de nuits"))
        self.label_10.setText(_translate("MainWindow", "10/15 ans"))
        self.label_11.setText(_translate("MainWindow", "3/9 ans"))
        self.label_12.setText(_translate("MainWindow", "- 3 ans"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.calcul.clicked.connect(self.Calculate_price)
    def Calculate_price(self):
        adultes = int(self.adultes_sbox.value())
        enfants15 = int(self.enfants_sbox_15.value())
        enfants9 = int(self.enfants_sbox_9.value())
        enfants3 = int(self.enfants_sbox_3.value())
        formule = (self.formule_cbox.currentIndex())
        rooms = np.ceil(adultes/2)
        d_arivee=self.calendar_arivee.selectedDate()
        jour_arivee=self.calendar_arivee.selectedDate().day()
        mois_arivee=self.calendar_arivee.selectedDate().month()
        annee_arivee=self.calendar_arivee.selectedDate().year()
        d_depart=self.calendar_depart.selectedDate()
        jour_depart=self.calendar_arivee.selectedDate().day()
        mois_depart=self.calendar_arivee.selectedDate().month()
        annee_depart=self.calendar_arivee.selectedDate().year()
        nombre_jours=d_arivee.daysTo(d_depart)
        self.nb_nuits.setText(str(nombre_jours))
        #basse saison
        dper1=(QtCore.QDate(annee_arivee, 1, 2))
        fper1=(QtCore.QDate(annee_depart, 2, 10))
        dper2=(QtCore.QDate(annee_arivee, 2, 25))
        fper2=(QtCore.QDate(annee_depart, 4, 28))
        dper3=(QtCore.QDate(annee_arivee, 9, 30))
        fper3=(QtCore.QDate(annee_depart, 12, 31))
        #moyenne saison
        dper4=(QtCore.QDate(annee_arivee, 2, 11))
        fper4=(QtCore.QDate(annee_depart, 2, 24))
        dper5=(QtCore.QDate(annee_arivee, 4, 29))
        fper5=(QtCore.QDate(annee_depart, 7, 7))
        dper6=(QtCore.QDate(annee_arivee, 8, 19))
        fper6=(QtCore.QDate(annee_depart, 9, 29))
        #haute saison
        dper7=(QtCore.QDate(annee_arivee, 7, 8))
        fper7=(QtCore.QDate(annee_depart, 8, 18))
        incr_date=d_arivee
        total_price=0
# dans le cas d'une PC
    
        if formule == 0:
            for i in range(1,nombre_jours+1):
                incr_date=incr_date.addDays(1)
                #for a specific iteration if the i date falls in the period 1
                if incr_date.daysTo(dper1)< 1 and incr_date.daysTo(fper1)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *60 + enfants15*43 + enfants9*35 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *70 + enfants15*43 + enfants9*35 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                #for a specific iteration if the i date falls in the period 2
                if incr_date.daysTo(dper2)< 1 and incr_date.daysTo(fper2)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *60 + enfants15*43 + enfants9*35 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *70 + enfants15*43 + enfants9*35 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper3)< 1 and incr_date.daysTo(fper3)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *60 + enfants15*43 + enfants9*35 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *70 + enfants15*43 + enfants9*35 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper4)< 1 and incr_date.daysTo(fper4)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *65 + enfants15*48 + enfants9*40 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *75 + enfants15*48 + enfants9*40 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper5)< 1 and incr_date.daysTo(fper5)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *65 + enfants15*48 + enfants9*40 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *75 + enfants15*48 + enfants9*40 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper6)< 1 and incr_date.daysTo(fper6)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *65 + enfants15*48 + enfants9*40 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *75 + enfants15*48 + enfants9*40 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper7)< 1 and incr_date.daysTo(fper7)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *75 + enfants15*54 + enfants9*45 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *85 + enfants15*54 + enfants9*45 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

        if formule == 1:
            for i in range(1,nombre_jours+1):
                incr_date=incr_date.addDays(1)
                #for a specific iteration if the i date falls in the period 1
                if incr_date.daysTo(dper1)< 1 and incr_date.daysTo(fper1)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *54 + enfants15*37 + enfants9*29 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *64 + enfants15*37 + enfants9*29 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                #for a specific iteration if the i date falls in the period 2
                if incr_date.daysTo(dper2)< 1 and incr_date.daysTo(fper2)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *54 + enfants15*37 + enfants9*29 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *64 + enfants15*37 + enfants9*29 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper3)< 1 and incr_date.daysTo(fper3)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *54 + enfants15*37 + enfants9*29 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *64 + enfants15*37 + enfants9*29 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper4)< 1 and incr_date.daysTo(fper4)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *59 + enfants15*42 + enfants9*34 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *69 + enfants15*42 + enfants9*34 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper5)< 1 and incr_date.daysTo(fper5)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *59 + enfants15*42 + enfants9*34 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *69 + enfants15*42 + enfants9*34 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper6)< 1 and incr_date.daysTo(fper6)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *59 + enfants15*42 + enfants9*34 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *69 + enfants15*42 + enfants9*34 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper7)< 1 and incr_date.daysTo(fper7)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *69 + enfants15*48 + enfants9*39 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *79 + enfants15*48 + enfants9*39 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

        if formule == 2:
            for i in range(1,nombre_jours+1):
                incr_date=incr_date.addDays(1)
                #for a specific iteration if the i date falls in the period 1
                if incr_date.daysTo(dper1)< 1 and incr_date.daysTo(fper1)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *40 + enfants15*23 + enfants9*15 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *50 + enfants15*23 + enfants9*15 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                #for a specific iteration if the i date falls in the period 2
                if incr_date.daysTo(dper2)< 1 and incr_date.daysTo(fper2)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *40 + enfants15*23 + enfants9*15 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *50 + enfants15*23 + enfants9*15 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper3)< 1 and incr_date.daysTo(fper3)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *40 + enfants15*23 + enfants9*15 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *50 + enfants15*23 + enfants9*15 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper4)< 1 and incr_date.daysTo(fper4)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *45 + enfants15*28 + enfants9*19 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *55 + enfants15*28 + enfants9*19 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper5)< 1 and incr_date.daysTo(fper5)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *45 + enfants15*28 + enfants9*19 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *55 + enfants15*28 + enfants9*19 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper6)< 1 and incr_date.daysTo(fper6)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *45 + enfants15*28 + enfants9*19 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *55 + enfants15*28 + enfants9*19 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

                if incr_date.daysTo(dper7)< 1 and incr_date.daysTo(fper7)>-1:
                    if adultes > 1.1:
                        temp_price= adultes *55 + enfants15*34 + enfants9*25 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))
                    else:
                        temp_price= adultes *65 + enfants15*34 + enfants9*25 + enfants3*0
                        total_price =total_price+temp_price 
                        self.prix_total.setText(str(total_price))
                        self.chambres.setText(str(rooms))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    

