import csv
import numpy as np
import math
import random, sys


class makebins:
	def __init__(self):	
		self.data=None
		self.months=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
		self.daysinmonths=[31,29,31,30,31,30,31,31,30,31,30,31]
		self.cumulative={}
		self.ofile=open('output.txt')
		for x in range(12):
			self.cumulative[x+1]=sum(self.daysinmonths[:x])
		print(self.cumulative)
		self.crime_types={}
		infile=open('crime_types.txt','r')
		inlines=infile.readlines()
		for j in range(len(inlines)):
			ctype=inlines[j]
			self.crime_types[ctype[:-1]]=j

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

	def dump_week(self,dx):
		neweek=[0]*30
		for el in dx.keys():
			indx=self.crime_types

	def engine(self):
		count=0
		dx={}
		for j in range(12):
			dx[j+1]=0	
		weeklystat={}	
		prev_week=0
		with open("2001.csv","r") as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			row=next(reader)
			for j in range(75000):
				row=next(reader)
				date_time=row[2]
				date_time=date_time.split()
				date=date_time[0]
				threeparts=date.split('/')
				month=int(threeparts[0])
				day=int(threeparts[1])
				year=int(threeparts[2])
				day_count = self.cumulative[month]+day
				week=day_count//7
				crtype=row[5]
				if week=prev_week:
					if weeklystat.get(crtype,-1)==-1:
						weeklystat[crtype]=1
					else:
						weeklystat[crtype]+=1
				else:
					self.dump_week(weeklystat)
				prev_week=week

ux=makebins()
#ux.get_date()