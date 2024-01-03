#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


# In[3]:


df=pd.read_csv(r"C:\Users\Rohit\Downloads\Salary_Data.csv")


# In[4]:


df


# In[8]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.head()


# In[13]:


df.isna().sum()


# In[14]:


sns.pairplot(df)


# In[16]:


sns.heatmap(df.corr(),annot=True)


# In[17]:


#duplicate value 

df[df.duplicated()].shape


# In[18]:


sns.distplot(x = df['YearsExperience'])


# In[19]:


sns.distplot(x = df['Salary'])


# In[20]:


#renaming column for better understanding and easy to implement the code

data = df.rename({'YearsExperience':'Exp'},axis=1)
data


# In[23]:


#model building 

import statsmodels.formula.api as smf


# In[24]:


model1 = smf.ols("Salary ~ Exp", data=data).fit()


# In[25]:


model1.params


# In[26]:


#rsquare and #adj

model1.rsquared


# In[27]:


model1.rsquared_adj


# In[29]:


model2 = smf.ols("Salary ~ np.log(Exp)", data=data).fit()


# In[30]:


model2.params


# In[32]:


#rsquare and #adj

model2.rsquared


# In[33]:


model2.rsquared_adj


# In[36]:


model3 = smf.ols("Salary ~ np.square(Exp)", data=data).fit()


# In[37]:


model3.params


# In[38]:


#rsquare and #adj

model3.rsquared


# In[39]:


model3.rsquared_adj


# In[41]:


model4 = smf.ols("Salary ~ np.sqrt(Exp)", data=data).fit()


# In[43]:


model4.params


# In[44]:


#rsquare and #adj

model4.rsquared


# In[45]:


model4.rsquared_adj


# In[ ]:




