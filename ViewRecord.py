
from Record import Record
from Controller import Controller
from ViewGroupByForm import ViewGroupBy
from FormAddRecord import FormAddRecord

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGroupBox

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem


class ViewRecord (QWidget):
	def __init__(self):
		super().__init__()
		self.controller = Controller()
		self.initUI()
		
		# bad idea saving all group by views in list
		# need to remove views if they are closed
		# will implement later
		self.groupByViewsList = []

	def initUI (self):
		# buttons
		self.addRecordButton         = QPushButton ("Add Record")
		self.addRecordFromFileButton = QPushButton ("Add Record From File")
		self.eraseAllRecordButton    = QPushButton ("Erase All Record")
		self.searchButton            = QPushButton ("Search")

		# table
		self.tableView = QTableView()
		self.model = QStandardItemModel()
		self.model.setHorizontalHeaderLabels (Record.getHeaders())
		self.tableView.setModel (self.model)
		self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

		# buttons to table for column and count
		self.occupationButton = QPushButton ("Occupation")
		self.addressButton    = QPushButton ("Adress")

		# layouts
		hbox = QHBoxLayout()
		hbox.addWidget (self.addRecordButton)
		hbox.addWidget (self.addRecordFromFileButton)
		hbox.addWidget (self.eraseAllRecordButton)
		hbox.addStretch (1)

		editdbGroupBox = QGroupBox ("Modify DataBase")
		editdbGroupBox.setLayout (hbox)

		searchGroupBox = QGroupBox ("Search")
		searchBox = QHBoxLayout ()
		searchBox.addWidget (self.searchButton)
		searchGroupBox.setLayout (searchBox)

		vbox = QVBoxLayout()
		vbox.addWidget (editdbGroupBox)
		vbox.addWidget (searchGroupBox)
		vbox.addWidget (self.tableView)

		groupByBox = QGroupBox ("Group By")
		groupByButtonsLayout = QVBoxLayout()
		groupByButtonsLayout.addStretch (1)
		groupByButtonsLayout.addWidget (self.occupationButton)
		groupByButtonsLayout.addWidget (self.addressButton)
		groupByButtonsLayout.addStretch (1)
		groupByBox.setLayout (groupByButtonsLayout)

		mainPanel = QHBoxLayout()
		mainPanel.addLayout (vbox)
		mainPanel.addWidget (groupByBox)

		self.setLayout (mainPanel)

		# signals and slots
		self.addRecordButton.clicked.connect         (self.slot_addOneRecord)
		self.addRecordFromFileButton.clicked.connect (self.slot_addRecordFromFile)
		self.eraseAllRecordButton.clicked.connect    (self.slot_eraseAllRecord)

		self.searchButton.clicked.connect            (self.slot_showData)

		self.occupationButton.clicked.connect        (self.slot_groupByOccupation)
		self.addressButton.clicked.connect           (self.slot_groupByAddress)

		# setup
		self.setGeometry (200, 100, 800, 600)
		self.setWindowTitle ('Records Manager')
		self.show()

	# slots for adding records to table
	@pyqtSlot()
	def slot_showData (self):
		# clear table first
		self.model.removeRows (0, self.model.rowCount())
		# insert data in to table
		data = self.controller.queryAllData()
		#print (data)
		for i, row in enumerate (data):
			for j, item in enumerate (row):
				self.model.setItem (i, j, QStandardItem (item))

	@pyqtSlot()
	def slot_addOneRecord (self):
	        a = FormAddRecord()
	        a.exec_()
	        print (a.success)
	        if a.success:
	            print ("Log: Data Are Valid")
	            rc = Record (a.name.text(), a.surname.text(), a.dob.currentText (), a.address.text(), a.occupation.text())
	            print (rc.getData())
	            self.controller.addOneRecord (rc)


	@pyqtSlot()
	def slot_eraseAllRecord (self):
		print ("Log: Erasing all records from database")
		self.controller.eraseAllData ()

	@pyqtSlot()
	def slot_addRecordFromFile (self):
		fname = QFileDialog.getOpenFileName (self, "Open File")
		if fname[0] != '':
			self.controller.addDataFromfile (fname[0])
			print ("Log: Succesfully added records from file " + fname[0])

	# slots for groupBy Buttons
	@pyqtSlot()
	def slot_groupByOccupation (self):
		print ("Opening view for displaying data grouped by occupation")
		vo = ViewGroupBy (self.controller, "Occupation")
		self.groupByViewsList.append (vo)

	@pyqtSlot()
	def slot_groupByAddress (self):
		print ("Opening view for displaying data grouped by address")
		va = ViewGroupBy (self.controller, "Address")
		self.groupByViewsList.append (va)



