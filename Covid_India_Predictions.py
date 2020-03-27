
# coding: utf-8

# In[288]:


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
os.chdir(lib_path)


# In[290]:


covid_pred=pd.read_csv(r'total_cases_data.csv')


# In[291]:


data=covid_pred


# In[292]:


import scipy
import patsy


# In[293]:


import statsmodels.api as sm


# In[294]:


X=data.Time


# In[295]:


X=sm.add_constant(X)


# In[296]:


data['logTotal']=np.log(data.Total)


# In[297]:


y=data.logTotal


# In[298]:


mod=sm.OLS(y,X)
res=mod.fit()
print(res.summary())


# In[299]:


import math


# In[300]:


initial_value_exponent=2.2605


# In[301]:


X0=math.exp(initial_value_exponent)


# In[302]:


X0


# In[303]:


growth_factor_exponent=0.1728


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
t = today + datetime.timedelta(days = 2) #+1 in days as 1st case was on 2nd and another +1 days as we're predicting for tomorrow


# In[308]:


delta = t - start_date


# In[309]:


time=delta.days


# In[310]:


Xt = X0 * (math.pow(b,time))


# In[311]:


Xt


# In[312]:


predicted = round(Xt)


# In[313]:


predicted


# In[314]:


tomorrow = t - datetime.timedelta(days=1)


# In[315]:


tomorrow


# In[316]:


covid_actual=pd.read_csv(r'total_cases_data.csv')


# In[317]:


covid_actual.loc[:, 'Date':'human_date']


# In[318]:


#covid_predicted


# In[319]:


covid_predicted=pd.DataFrame({'Date':["26/3/2020","27/3/2020","28/3/2020"],'Total':["721","857","1019"], 'human_date':["26th Mar","27th Mar","28th Mar"]})  #change here


# In[320]:


covid_predicted.to_csv('predicted_data.csv',index=False)


# In[321]:


covid_merge = pd.merge(covid_actual,covid_predicted,left_on=['Date'],right_on=['Date'],how = 'left')


# In[322]:


covid_accuracy = covid_merge[(covid_merge['Date']=='26/3/2020') | (covid_merge['Date']=='27/3/2020') | (covid_merge['Date']=='28/3/2020')]   #change here


# In[323]:


covid_accuracy


# In[324]:


covid_accuracy['Total_y']=covid_accuracy['Total_y'].astype(int)
covid_accuracy['Total_x']=covid_accuracy['Total_x'].astype(int)


# In[325]:


covid_accuracy.loc[covid_accuracy['Total_x']>=covid_accuracy['Total_y'], 'Accuracy'] =  (covid_accuracy['Total_y']/covid_accuracy['Total_x'])*100


# In[326]:


covid_accuracy.loc[covid_accuracy['Total_x']<covid_accuracy['Total_y'], 'Accuracy'] =  (covid_accuracy['Total_x']/covid_accuracy['Total_y'])*100


# In[327]:


#covid_accuracy

