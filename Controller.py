
from DataBaseManager import RecordDataBaseManager

from Record import Record

class Controller():
	def __init__ (self):
		self.rdbm = RecordDataBaseManager()

	def queryDataWithConstraints (self, options):
		pass

	def queryAllData (self):
		data = self.rdbm.getAllRecords();
		return data
	
	def queryDataGroupedby (self, colName):
		data = self.rdbm.getDataGroupedBy (colName)
		return data

	def addOneRecord (self, rec):
		self.rdbm.addOneRecord (rec.getData())

	def addDataFromfile (self, path):
		print (path)
		with open (path, 'r') as f:
			for line in f :
				line.rstrip ('\n')
				l = line.split (" ")
				rec = Record (l[0], l[1], l[2], l[3], l[4])
				# print (rec.getData())
				self.addOneRecord (rec)

	def eraseAllData (self):
		self.rdbm.eraseAllData ()

