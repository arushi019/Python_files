def warn(*args,**kwargs):
    pass
import warnings
warnings.warn=warn
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import csv
import numpy as np
filename='sample1.csv'
raw_data=open(filename,'rt')
reader=csv.reader(raw_data,delimiter=',',quoting=csv.QUOTE_NONE)
x=list(reader)
x=x[1:100]
age=[]
income=[]
for i in x:
    ag=int(i[1])
    while ag in age:
        ag=ag+1
    age.append(ag)
    income.append(float(i[2][1:]))
reg=LogisticRegression()
#reg.fit(np.transpose(np.matrix(np.array(age))),np.transpose(np.matrix(np.array(income))))
reg.fit(np.array(age),np.array(income))
print(model)
reg_pred=[]
n_age=np.array(age)
for i in n_age:
    temp=[i]
    reg_pred.append(reg.predict(temp)[0])
print(metrics.classification_report(income,reg_pred))
print(metrics.confusion_matrix(income,reg_pred))
