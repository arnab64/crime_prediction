from sklearn import linear_model
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
import numpy as np

class predict:
	def __init__(self,weekno):
		infname='weeks/week_'+str(weekno)+'.txt'
		self.indata=np.loadtxt(infname,delimiter=',')
		#print(self.indata.shape)	

	def split_test_train(self):
		self.train_X=self.indata[:-1,:-3]
		self.test_X=self.indata[-1:,:-3]		
		self.train_y=self.indata[:-1,-3]
		self.test_y=self.indata[-1:,-3]

	def train(self,modelx):
		if modelx=='linear':
			regr = linear_model.LinearRegression()
		elif modelx=='ridge':
			regr = Ridge(alpha=1.0)
		elif modelx=='elastic':
			regr = ElasticNet(alpha=1.0, l1_ratio=0.7)
		regr.fit(self.train_X,self.train_y)
		pred=regr.predict(self.test_X)
		org=self.test_y

		#print("correlation coefficients",np.corrcoef(self.train_X,self.train_y))

		#print("predicted",pred)
		#print("original",org)
		coeffx=regr.coef_
		#print("coefficients",)
		mse=np.mean((pred-org) ** 2)
		mae=np.mean(abs(pred-org))
		rmse=np.sqrt(mse)
		rae=abs(org[0]-pred[0])/abs(org[0])
		#variance_scr=regr.score(diabetes_X_test, diabetes_y_test)
		print("mse/mae/rae/rmse",mse,mae,rae,rmse)
		return mse,mae,rae,rmse,coeffx

def aggregate():
	ofile=open('compare_regression.txt','a+')
	models=['linear','ridge','elastic']
	for el in models:
		mse=[]
		mae=[]
		rae=[]
		rmse=[]
		coeffx=[]
		for k in range(1,53):
			p1=predict(k)
			p1.split_test_train()
			a,b,c,d,e=p1.train(el)
			mse.append(a)
			mae.append(b)
			rae.append(c)
			rmse.append(d)
			coeffx.append(e)
		print("Average MSE over 52 weeks",np.mean(mse))
		print("Average MAE over 52 weeks",np.mean(mae))
		print("Average RAE over 52 weeks",np.mean(rae))
		print("Average RMSE over 52 weeks",np.mean(rmse))
		print("Average coeffx over 52 weeks",np.mean(coeffx,axis=0))
		ofile.write(el+"	"+str(np.mean(mse))+"	"+str(np.mean(mae))+"	"+str(np.mean(rae))+'\n')
	ofile.close()

aggregate()