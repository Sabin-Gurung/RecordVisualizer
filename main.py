#!usr/bin/python3

from ViewRecord import ViewRecord

from PyQt5.QtWidgets import QApplication

import sys

if __name__ == '__main__':
	app = QApplication (sys.argv)
	rv = ViewRecord()
	sys.exit (app.exec_())
