def warn(*args,**kwargs):
    pass
import warnings
warnings.warn=warn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score
import csv
filename='sample1.csv'
raw_data=open(filename,'rt')
reader=csv.reader(raw_data,delimiter=',',quoting=csv.QUOTE_NONE)
x=list(reader)
x=x[1:100]
age=[]
income=[]
#print(x)
#data=np.array(x).astype('float')
#print(data.shape)
for i in x:
    #print(i)
    ag=int(i[1])
    while ag in age:
        #print("yo")
        ag=ag+1
    age.append(ag)
    income.append(float(i[2][1:]))
#print(age)
#print(income)
data_x_train=np.array(age[:40])
data_y_train=np.array(income[:40])
data_x_test=age[40:]
data_y_test=income[40:]
data_y_pred=[]
reg=linear_model.LinearRegression()
reg.fit(np.transpose(np.matrix(data_x_train)),np.transpose(np.matrix(data_y_train)))
for i in data_x_test:
    temp=[i]
    data_y_pred.append(reg.predict(temp)[0])
print(data_x_test)
print(data_y_pred)
plt.scatter(data_x_test,data_y_test,color='red')
plt.plot(data_x_test,data_y_pred,color='blue',linewidth=2)
plt.xticks(())
plt.yticks(())
plt.show()
