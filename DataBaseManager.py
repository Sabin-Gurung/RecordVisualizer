#!usr/bin/python3
import sqlite3


class RecordDataBaseManager():
	''' handles initializing database and its modification and query of data '''
	def __init__ (self):
		''' loads the files and creates table if its first time '''
		self.__conn = sqlite3.connect("record.db");
		self.__cur = self.__conn.cursor();

		#if its first time creating database then the table needs to be created
		self.__cur.execute ("SELECT SQLITE_VERSION()")
		data = self.__cur.fetchone()
		print ("Sql Log: Current version %s", data);

		self.__cur.execute ("select name from sqlite_master where type ='table' and name = 'Record'")
		data = self.__cur.fetchone()

		if data == None:
			print ("Sql Log: Creating new table : Record");
			self.__createRecordTable();
		else :
			print ("Sql Log: Record table already Exists")

	def __createRecordTable (self):
		self.__cur.execute ("create table " + 
		                    "Record (" +
		                    "Name text, " +
		                    "Surname text, " + 
		                    "DOB text, " + 
		                    "Address text, " + 
		                    "Occupation text" +
		                    ")"
		                    )



	def addOneRecord (self, rec):
		try:
			self.__cur.execute ("""insert into Record
			                       (
			                        Name,
			                        Surname,
			                        DOB,
			                        Address,
			                        Occupation
			                       ) 
			                       values (?, ?, ?, ?, ?);
			                       """, rec)
			self.__conn.commit()

		except sqlite3.Error as e:
			print ("Sql Error:", e.args[0])
			self.__conn.rollback()

	def getAllRecords (self):
		self.__cur.execute ("select * from Record")
		rows = self.__cur.fetchall()
		return rows

	def getDataGroupedBy (self, colName):
		command = "select " + colName + ", count (*) from Record group by " + colName + ";"
		self.__cur.execute (command)
		rows = self.__cur.fetchall()
		return rows

	def eraseAllData (self):
		try:
			self.__cur.execute ("delete from Record;")
			self.__conn.commit()
		except sqlite3.Error as e:
			print ("Sql Error:", e.args[0])
			self.__conn.rollback()

	def close (self):
		self.__conn.close ()


