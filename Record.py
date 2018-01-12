#!/usr/bin/python3


class Record():
	def __init__ (self, name, surname, dateOfBirth, address, occupation):
		self.__name       = name
		self.__surname    = surname
		self.__DOB        = dateOfBirth
		self.__address    = address
		self.__occupation = occupation

	def getData (self):
		'''returns a list containing data in the right order'''
		return [self.__name, self.__surname, self.__DOB, self.__address, self.__occupation]

	@staticmethod
	def getHeaders():
		return ["Name", "Surname", "DOB", "Address", "Occupation"]


