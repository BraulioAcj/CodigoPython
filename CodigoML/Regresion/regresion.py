#import
#import mattplotlib.pyplot as plt
import numpy as np

#importing from scikit-learn
from sklearn import fatasets, linear_model

#load dataset
house_price = [245,321,279,308,199,219,405,324,319,255]
size = [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]

print(len(house_price))
print(len(size))

#Reshape the input to your regression
size2 = np.array(size).reshape((-1,1))
print(size2)

#
regr = linear_model.linearRegression()
regr.fit(size2,house_price)
print('Coeficients: {0}'.formar(regr.coef_))
print('Intercept: {0}'.format(regr.intercept))

#Formula obtenida para modelo entrenado

def graph(formula,x_range):
	x=np.array(x_range)
	y=eval(formula)
	plt.plot(x,y)

#Plotting the prediction line
graph('regr.coed_*x+regr.intercept_',range(500,3000))
plt.scatter(size,hpuse_price,color='black')
plt.ylabel('house_price')
plt.xlabel('size of house')

#HOLA
