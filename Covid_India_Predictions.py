
# coding: utf-8


import pandas as pd
import os
import numpy as np
import json as json
import mysql.connector as sqlcnt
import datetime as dt
import requests
from mysql.connector.constants import SQLMode
import os
import glob
import re

import warnings
warnings.filterwarnings("ignore")
from pathlib import Path


# In[289]:


import os,sys
lib_path = r"\\"
#lib_path = r"C:\Users\300068241\Documents\Covid_Data\Daily"
os.chdir(lib_path)


covid_pred=pd.read_csv(r'total_cases_data.csv')
data=covid_pred


import scipy
import patsy

##OLS algorithm from Statsmodels library is used here. Linear regression is used here to get the initial value component(X0) on which exponential smoothing is performed. Exponential smoothing assigns exponentially decreasing weights over time. This means that exponential smoothing places a bigger emphasis on more recent observations, providing a weighted average. If the data has no trend and no seasonal pattern, then this method of forecasting the time series is essentially used. 

import statsmodels.api as sm


X=data.Time
X=sm.add_constant(X)
data['logTotal']=np.log(data.Total)
y=data.logTotal
mod=sm.OLS(y,X)
res=mod.fit()
print(res.summary())


import math
initial_value_exponent=2.2588
X0=math.exp(initial_value_exponent)
X0


growth_factor_exponent=0.1730


# In[304]:


b=math.exp(growth_factor_exponent)


# In[305]:


b


# In[306]:


from datetime import date
start_date = date(2020, 3, 2) #1st case is assumed to be of 2nd Mar'20


# In[307]:


import datetime 
today = datetime.date.today()
t = today + datetime.timedelta(days = 1) #+1 in days as 1st case was on 2nd and another +1 days as we're predicting for tomorrow

delta = t - start_date


time=delta.days


Xt = X0 * (math.pow(b,time))
#Xt
predicted = round(Xt)

tomorrow = t - datetime.timedelta(days=1)

covid_actual=pd.read_csv(r'total_cases_data.csv')

covid_actual.loc[:, 'Date':'human_date']


covid_predicted=pd.DataFrame({'Date':["26/3/2020","27/3/2020","28/3/2020"],'Total':["721","857","1022"], 'human_date':["26th Mar","27th Mar","28th Mar"]})  #change here

covid_predicted.to_csv('predicted_data.csv',index=False)


covid_merge = pd.merge(covid_actual,covid_predicted,left_on=['Date'],right_on=['Date'],how = 'left')
covid_accuracy = covid_merge[(covid_merge['Date']=='26/3/2020') | (covid_merge['Date']=='27/3/2020') | (covid_merge['Date']=='28/3/2020')]   #change here

#covid_accuracy

covid_accuracy['Total_y']=covid_accuracy['Total_y'].astype(int)
covid_accuracy['Total_x']=covid_accuracy['Total_x'].astype(int)

covid_accuracy.loc[covid_accuracy['Total_x']>=covid_accuracy['Total_y'], 'Accuracy'] =  (covid_accuracy['Total_y']/covid_accuracy['Total_x'])*100

covid_accuracy.loc[covid_accuracy['Total_x']<covid_accuracy['Total_y'], 'Accuracy'] =  (covid_accuracy['Total_x']/covid_accuracy['Total_y'])*100

accuracy_final=covid_accuracy.mean(axis = 0)

