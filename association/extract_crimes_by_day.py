import csv
import numpy as np
import math
import random, sys


class makebins:
	def __init__(self):	
		self.data=None
		csvfile1=open('crimesbyday2015.csv', 'w',newline='')
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

	def extract_crime_years(self,countx):
		with open("../prediction/allfiles/original_data_files/Chicago_Crimes_2012_to_2017.csv","r") as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			headerrow=next(reader)
			self.csvfile.writerow(headerrow)
			for j in range(countx):
				row=next(reader)
				date_time=row[3]
				#print("date_time:",date_time)
				date_time1=date_time.split()
				date=date_time1[0]
				threeparts=date.split('/')
				year=int(threeparts[2])
				#print("date_time:",date_time," / year:",year)
				if year==2016:
					self.csvfile.writerow(row)
				self.drawProgressBar(j/countx)			#242480)

	def extract_days(self,countx):
		infile=open('listofcrimes.txt','r')
		intext=infile.read()
		crimes=intext.split(',')
		positions={}
		for j in range(len(crimes)):	#position of the crime
			positions[crimes[j]]=j
		countofcrimes={}
		for	j in range(len(crimes)):	#initializing the numbers of each crime
			countofcrimes[crimes[j]]=0	
		with open("crime_2015.csv","r") as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			headerrow=next(reader)
			self.csvfile.writerow(crimes)
			prev=None
			listofcrimes=[]
			day=1
			for j in range(countx):
				row=next(reader)
				crime=row[6]
				date_time=row[3]
				#print("date_time",date_time)
				date_time1=date_time.split()
				date=date_time1[0]
				time=date_time1[1]
				timespl=time.split(':')
				hour=int(timespl[0])
				#print(j,"crime=",crime)
				if date==prev:
					countofcrimes[crime]+=1	
					#print(countofcrimes)
				else:
					#listofcrimes.insert(0,day)
					#print(countofcrimes)
					vectorx=[]
					for j in range(len(crimes)):
						crimex=crimes[j]
						#print(crimex,countofcrimes[crimex])
						vectorx.append(countofcrimes[crimex])
						countofcrimes[crimex]=0
					self.csvfile.writerow(vectorx)
					#for	j in range(len(crimes)):	#initializing the numbers of each crime
					#	countofcrimes[crimes[j]]=0									
					day+=1
				prev=date
				'''
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
				year=int(threeparts[2])
				if hour>=0 and hour<6:
					timeofday='Night'
				elif hour>=6 and hour<12:
					timeofday='Morning'
				elif hour>=12 and hour<18:
					timeofday='Afternoon'
				elif hour>=18 and hour<24:
					timeofday='Evening'
				if date==prev:
					if crime not in listofcrimes:
						listofcrimes.append(crime)
				else:			
					self.csvfile.writerow(listofcrimes)
					'''
				self.drawProgressBar(j/countx)			#242480)

	def get_all_crimes(self,countx):
		ofile=open('listofcrimes.txt','w')
		with open("crime_2015.csv","r") as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			headerrow=next(reader)
			listofcrimes=[]
			for j in range(countx):
				row=next(reader)		
				crime=row[6]
				if crime not in listofcrimes:
					listofcrimes.append(crime)
		for el in range(len(listofcrimes)):
			ofile.write(listofcrimes[el]+',')

ux=makebins()
#ux.extract_crime_years(1456714)
#ux.get_all_crimes(262995)
ux.extract_days(262995)