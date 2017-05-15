import sys, os
import numpy as np

class weekly:
	def __init__(self):
		infile=open('crime_types.txt','r')
		intext=infile.read()
		seg=intext.split(',')
		self.crime_types={}
		print("types of crime=",len(seg))
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

	def machine(self,years):
		mega=[]
		for j in range(len(years)):
			yearx=years[j]
			fname='output_'+str(yearx)+'.txt'
			csv = np.loadtxt (fname, delimiter=",")	
			#print(csv.shape)
			mega.append(csv)

		for el in mega:
			print(el.shape)
		temp=None
		for k in range(52):
			print("for week",k+1)
			for j in range(len(mega)):
				thx=mega[j]
				weekinfo=thx[k]			#only the week k
				if j==0:
					temp=weekinfo
				else:
					#temp=np.concatenate((temp,weekinfo),axis=0)
					temp=np.column_stack((temp,weekinfo))
				print(temp.shape)
			print("lastshape",temp.shape)
			ofilename='weeks/week_'+str(k+1)+'.txt'
			np.savetxt(ofilename, temp, delimiter=',',fmt='%4.0f')	


	def machine2(self,years):
		mega=[]
		for j in range(len(years)):				#add files for all the years in mega
			yearx=years[j]
			fname='yearly_data/output_'+str(yearx)+'.txt'
			csv = np.loadtxt (fname, delimiter=",")	
			mega.append(csv)

		for el in mega:
			print(el.shape)

		temp=None
		for k in range(52):				#for each week
			print("for week",k+1)			
			for j in range(len(mega)):
				thx=mega[j]				#for each year
				weekinfo=thx[k]			#only the week k
				weekinfo=np.insert(weekinfo,0,years[j])
				if j==0:
					temp=weekinfo
				else:
					temp=np.vstack((temp,weekinfo))
				print(temp.shape)
			print("lastshape",temp.shape)
			#np.transpose(temp)
			ofilename='weeks/week_'+str(k+1)+'.txt'
			np.savetxt(ofilename, temp, delimiter=',',fmt='%4.0f')				

years=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
week=weekly()
week.machine2(years)