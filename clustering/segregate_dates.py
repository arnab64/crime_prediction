import csv
import numpy as np
import math
import random, sys


class makebins:
	def __init__(self):	
		self.data=None
		csvfile1=open('timeofday_2016.csv', 'w',newline='')
		self.csvfile=csv.writer(csvfile1,delimiter=',')

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

	def engine(self,countx):
		with open("../prediction/allfiles/original_data_files/Chicago_Crimes_2012_to_2017.csv","r") as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			row=next(reader)
			for j in range(countx):
				row=next(reader)
				date_time=row[3]
				date_time=date_time.split()
				date=date_time[0]
				time=date_time[1]
				timespl=time.split(':')
				hour=int(timespl[0])
				timeampm=date_time[2]
				if hour!=12:
					if timeampm=='PM':
						hour+=12
				else:
					if timeampm=='AM':
						hour=0
					else:
						hour=12
				threeparts=date.split('/')
				#month=int(threeparts[0])
				#day=int(threeparts[1])
				year=int(threeparts[2])
				if year==2016:
					if hour>=0 and hour<6:
						timeofday='Night'
					elif hour>=6 and hour<12:
						timeofday='Morning'
					elif hour>=12 and hour<18:
						timeofday='Afternoon'
					elif hour>=18 and hour<24:
						timeofday='Evening'
					#print(time,timeofday)
					row[3]=timeofday
					self.csvfile.writerow(row)
				self.drawProgressBar(j/countx)			#242480)

ux=makebins()
ux.engine(1456714)