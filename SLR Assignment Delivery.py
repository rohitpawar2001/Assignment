#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=pd.read_csv(r"C:\Users\Rohit\Downloads\delivery_time.csv")


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


sns.pairplot(df)


# In[8]:


df.isna().sum()


# In[9]:


df.head()


# In[10]:


#duplicate values

df[df.duplicated()].shape


# In[11]:


sns.heatmap(df.corr(), annot=True)


# In[12]:


sns.histplot(x = df['Delivery Time'])


# In[13]:


sns.histplot(x = df['Sorting Time'])


# In[14]:


data = df.rename({'Delivery Time':'DT', 'Sorting Time':'ST'},axis=1)
data


# In[16]:


#MODEL BUILDING

import statsmodels.formula.api as smf


# In[17]:


Model1 = smf.ols("DT ~ ST", data=data).fit()


# In[18]:


Model1.params


# In[20]:


#rsquare and #adj

Model1.rsquared


# In[21]:


Model1.rsquared_adj


# In[22]:


Model2 = smf.ols("DT ~ np.log(ST)", data=data).fit()


# In[23]:


Model2.params


# In[24]:


#rsquare and #adj

Model2.rsquared


# In[28]:


#rsquare and #adj

Model2.rsquared_adj


# In[26]:


Model3 = smf.ols("DT ~ np.square(ST)", data=data).fit()


# In[27]:


Model3.params


# In[29]:


#rsquare and #adj

Model3.rsquared


# In[30]:


#rsquare and #adj

Model3.rsquared_adj


# In[31]:


Model4 = smf.ols("DT ~ np.sqrt(ST)", data=data).fit()


# In[32]:


Model4.params


# In[33]:


#rsquare and #adj

Model4.rsquared


# In[34]:


#rsquare and #adj

Model4.rsquared_adj


# In[ ]:




