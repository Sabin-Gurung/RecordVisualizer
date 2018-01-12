#!/usr/bin/python3


class Record():
	def __init__ (self, name, surname, dateOfBirth, address, occupation):
		self.__name       = name.upper()
		self.__surname    = surname.upper()
		self.__DOB        = dateOfBirth.upper()
		self.__address    = address.upper()
		self.__occupation = occupation.upper()

	def getData (self):
		'''returns a list containing data in the right order'''
		return [self.__name, self.__surname, self.__DOB, self.__address, self.__occupation]

	@staticmethod
	def getHeaders():
		return ["Name", "Surname", "DOB", "Address", "Occupation"]


