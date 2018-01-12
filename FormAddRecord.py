#!/usr/bin/python3

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QDialog

import sys


class FormAddRecord (QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI ()

    def initUI (self):
        # flag to know if datas were inserted properly
        self.success = False
        # buttons
        self.addButton    = QPushButton ("Ok")
        self.cancelButton = QPushButton ("Cancel")
        buttonsLayout     = QHBoxLayout()
        buttonsLayout.addStretch (1)
        buttonsLayout.addWidget (self.addButton)
        buttonsLayout.addWidget (self.cancelButton)

        gl = QGridLayout()
        gl.addWidget (QLabel ("Name :")      , 0, 0)
        gl.addWidget (QLabel ("Surname :")   , 1, 0)
        gl.addWidget (QLabel ("DOB :")       , 2, 0)
        gl.addWidget (QLabel ("Address :")   , 3, 0)
        gl.addWidget (QLabel ("Occupation :"), 4, 0)

        self.name       = QLineEdit ()
        self.surname    = QLineEdit ()
        self.dob        = QComboBox()
        self.address    = QLineEdit ()
        self.occupation = QLineEdit ()

        for i in range (1980, 2005):
            self.dob.addItem (str (i))

        gl.addWidget (self.name      , 0, 1) 
        gl.addWidget (self.surname   , 1, 1)
        gl.addWidget (self.dob       , 2, 1)
        gl.addWidget (self.address   , 3, 1)
        gl.addWidget (self.occupation, 4, 1)

        vbox = QVBoxLayout()
        vbox.addLayout (gl)
        vbox.addLayout (buttonsLayout)

        self.setLayout (vbox)

        # signals and slots
        self.addButton.clicked.connect (self.slot_add)
        self.cancelButton.clicked.connect (self.slot_cancel)

        # setup
        self.setGeometry (700, 200, 420, 200)
        self.setWindowTitle ('Add Record')
        self.show()

    def __checkFields (self):
        if self.name.text() == "":
            return False
        if self.surname.text() == "":
            return False
        if self.address.text() == "":
            return False
        if self.occupation.text() == "":
            return False
        return True
        
    @pyqtSlot()
    def slot_add (self):
        if self.__checkFields():
            print ("good")
            self.success = True
            self.close()
        else :
            print ("invalid")

    def slot_cancel (self):
        self.success = False
        self.close()
