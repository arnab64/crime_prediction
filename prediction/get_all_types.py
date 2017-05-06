import csv
import numpy as np
import math
import random, sys


class makebins:
	def __init__(self):	
		self.data={}

	def drawProgressBar(self,percent, barLen = 50):			#just a progress bar so that you dont lose patience
		    sys.stdout.write("\r")
		    progress = ""
		    for i in range(barLen):
		        if i<int(barLen * percent):
		            progress += "="
		        else:
		            progress += " "
		    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
		    sys.stdout.flush()

	def engine(self):
		with open("2016.csv","r") as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			row=next(reader)				#skip the first row
			count=0
			for k in range(242480):
				row=next(reader)
				type=row[6]
				if self.data.get(type,-1)==-1:
					self.data[type]=1
				else:
					self.data[type]+=1
				count+=1
				self.drawProgressBar(count/242480)

		print('\n',self.data)
		ofile=open('crime_types.txt','w')
		for el in self.data.keys():
			ofile.write(el+', ')

ux=makebins()
ux.engine()