
from Record import Record
from Controller import Controller


import sys


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QAbstractItemView

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem


import matplotlib.pyplot as plt
import numpy as np


class ViewGroupBy (QWidget):
	def __init__(self, controller, headerName, parent = None):
		super().__init__(parent)
		self.controller = controller
		self.initUI (headerName)


	def initUI (self, headerName):
		# buttons
		self.headerName = headerName
		self.makePieChartButton = QPushButton ("PieChart")
		self.refreshButton      = QPushButton ("Refresh Data")
		self.makeBarChartButton = QPushButton ("BarChart")

		# table
		self.tableView = QTableView()
		self.model = QStandardItemModel()
		self.model.setHorizontalHeaderLabels ([self.headerName, "Count"])
		self.tableView.setModel (self.model)
		self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

		# layouts
		tableLayout = QVBoxLayout()
		tableLayout.addWidget (self.tableView)

		buttonsLayout = QVBoxLayout()
		buttonsLayout.addWidget (self.refreshButton)
		buttonsLayout.addWidget (self.makePieChartButton)
		buttonsLayout.addWidget (self.makeBarChartButton)

		mainPanel = QHBoxLayout()
		mainPanel.addLayout (tableLayout)
		mainPanel.addLayout (buttonsLayout)

		self.setLayout (mainPanel)

		# signals and slots
		self.makePieChartButton.clicked.connect (self.slot_makePieChart)
		self.makeBarChartButton.clicked.connect (self.slot_makeBarChart)
		self.refreshButton.clicked.connect      (self.slot_showData)

		self.tableView.horizontalHeader().sectionClicked.connect (self.slot_tableHeaderClicked)

		# container to store data
		self.data = []

		# setup
		self.setGeometry (700, 200, 500, 500)
		self.setWindowTitle ('Grouped By ' + self.headerName)
		self.show()

	# slots for adding records to table
	@pyqtSlot()
	def slot_showData (self):
		# clear table first
		self.model.removeRows (0, self.model.rowCount())
		# insert data in to table
		self.data = self.controller.queryDataGroupedby (self.headerName)
		for i, row in enumerate (self.data):
			for j, item in enumerate (row):
				self.model.setItem (i, j, QStandardItem (str(item)))
	
	@pyqtSlot()
	def slot_makePieChart (self):
		labels = []
		values = []
		for i in self.data:
			labels.append (i[0])
			values.append (i[1])

		plt.pie (values, labels = labels, autopct = "%.2f")
		plt.title ("Pie Chart : " + self.headerName)
		plt.show()

	@pyqtSlot()
	def slot_makeBarChart (self):
		labels = []
		values = []
		for i in self.data:
			labels.append (i[0])
			values.append (i[1])

		y_pos = np.arange (len (labels))

		plt.bar (y_pos, values)
		plt.xticks (y_pos, labels, rotation = 90)

		plt.xlabel (self.headerName)
		plt.ylabel ("Quantity")

		plt.title ("Bar Chart : " + self.headerName)

		plt.tight_layout()

		plt.show()

	@pyqtSlot(int)
	def slot_tableHeaderClicked (self, i):
		ascending = (self.tableView.horizontalHeader().sortIndicatorSection() == i) and (self.tableView.horizontalHeader().sortIndicatorOrder() == Qt.AscendingOrder)
		if (ascending) :
		    self.model.sort (i, Qt.DescendingOrder)
		else :
		    self.model.sort (i, Qt.AscendingOrder)
		print ("sorting by header" + Record.getHeaders() [i])
