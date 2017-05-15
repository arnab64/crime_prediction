from sklearn import linear_model
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

	def train(self):
		regr = linear_model.LinearRegression()
		regr.fit(self.train_X,self.train_y)
		pred=regr.predict(self.test_X)
		org=self.test_y

		print("correlation coefficients",np.corrcoef(self.train_X,self.train_y))

		#print("predicted",pred)
		#print("original",org)
		#print("coefficients",regr.coef_)
		mse=np.mean((pred-org) ** 2)
		mae=np.mean(abs(pred-org))
		rmse=np.sqrt(mse)
		rae=abs(org[0]-pred[0])/abs(org[0])
		#variance_scr=regr.score(diabetes_X_test, diabetes_y_test)
		print("mse/mae/rae/rmse",mse,mae,rae,rmse)

for k in range(1,10):
	p1=predict(k)
	p1.split_test_train()
	p1.train()