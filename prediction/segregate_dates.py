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
		self.oldweek=[0]*30
		self.ofile=open('output_2016.txt','w')
		self.ofile.write('week, OFFENSE INVOLVING CHILDREN, PROSTITUTION, NARCOTICS, ASSAULT, DECEPTIVE PRACTICE, NON - CRIMINAL, WEAPONS VIOLATION, CRIM SEXUAL ASSAULT, NON-CRIMINAL, CRIMINAL TRESPASS, STALKING, LIQUOR LAW VIOLATION, BATTERY, OTHER NARCOTIC VIOLATION, HUMAN TRAFFICKING, CRIMINAL DAMAGE, INTERFERENCE WITH PUBLIC OFFICER, HOMICIDE, CONCEALED CARRY LICENSE VIOLATION, BURGLARY, GAMBLING, ROBBERY, OTHER OFFENSE, OBSCENITY, SEX OFFENSE, MOTOR VEHICLE THEFT, KIDNAPPING, THEFT, ARSON, NON-CRIMINAL (SUBJECT SPECIFIED), PUBLIC INDECENCY, PUBLIC PEACE VIOLATION, INTIMIDATION \n')
		for x in range(12):
			self.cumulative[x+1]=sum(self.daysinmonths[:x])
		#print(self.cumulative)
		self.crime_types={}
		infile=open('crime_types.txt','r')
		intext=infile.read()
		seg=intext.split(',')
		for j in range(len(seg)):
			ctype=seg[j].strip()
			self.crime_types[ctype]=j

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

	def printit(self,arx):
		for j in range(len(arx)):
			arx[j]=str(arx[j])
		strx=",".join(arx) 
		self.ofile.write(strx+'\n')

	def difference(Self,arx,ary):
		arz=[0]*30
		for j in range(30):
			#if j==0: print(type(arx[j]),type(arx[j]))
			arz[j]=ary[j]-arx[j]
		return(arz)

	def dump_week(self,weekno,dx):				#take a dictionary and prints it in a table
		neweek=[0]*33
		for el in dx.keys():			#el is the key i.e. the crime type
			indx=self.crime_types[el]
			val=dx[el]
			neweek[indx]=val
		newark=self.difference(self.oldweek,neweek)
		self.oldweek=neweek[:]
		newark.insert(0,weekno)
		self.printit(newark)

	def engine(self):
		count=0
		dx={}
		for j in range(12):
			dx[j+1]=0	
		weeklystat={}	
		prev_week=0
		with open("2016.csv","r") as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			row=next(reader)
			for j in range(242480):	#242480):
				row=next(reader)
				date_time=row[3]
				date_time=date_time.split()
				date=date_time[0]
				threeparts=date.split('/')
				month=int(threeparts[0])
				day=int(threeparts[1])
				year=int(threeparts[2])
				day_count = self.cumulative[month]+day
				
				week=day_count//7
				#print("daycount",day_count," / week",week)
				crtype=row[6]
				#print("week/prevweek",week,prev_week)
				if week==prev_week:
					if weeklystat.get(crtype,-1)==-1:
						weeklystat[crtype]=1
					else:
						weeklystat[crtype]+=1
				else:
					self.dump_week(week,weeklystat)
					dx={}
				prev_week=week
				self.drawProgressBar(j/242480)			#242480)

ux=makebins()
ux.engine()