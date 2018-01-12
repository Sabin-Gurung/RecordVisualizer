

import sys
import random

# simple script to generate list of random records

if __name__ == "__main__":
	args = sys.argv
	if len (args) != 2:
		print ("Error: invalid number of arguments")
		print ("usage: python3 recordsGenerator.py _no_of_record") 
		sys.exit (0)

	# get base datas
	print ("reading base datas from ./data/ files")
	with open('./data/cities.txt') as f:
		cities = [line.rstrip ('\n') for line in f]
	with open('./data/occupatioins.txt') as f:
		occupatioins = [line.rstrip ('\n') for line in f]
	with open('./data/names.txt') as f:
		names = [line.rstrip ('\n') for line in f]
	with open('./data/surnames.txt') as f:
		surnames = [line.rstrip ('\n') for line in f]
	with open('./data/DOB.txt') as f:
		dobRange = f.readline()

	dbr = dobRange.split(" ")
	dbi = int (dbr[0])
	dbf = int (dbr[1])

	# create list of lines that contain info about a single record
	# each record is created randomly
	nRecord = int (args[1])
	records = []
	for i in range (nRecord):
		c = random.choice (cities)
		o = random.choice (occupatioins)
		n = random.choice (names)
		s = random.choice (surnames)
		d = random.randint (dbi, dbf)
		line = n + " " + s + " " + str (d) + " " + c + " " + o
		records.append (line)

	print ("writing created record list to output/")
	with open ('./output/records.txt', 'w') as f:
		f.writelines ("%s\n" % l for l in records)



