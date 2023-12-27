#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Look at the data given below. Plot the data, find the outliers and find out  μ,σ,σ^2


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.Series([24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00])


# In[3]:


company=['Allied Signal','Bankers Trust','General Mills','ITT Industries','J.P.Morgan & Co.','Lehman Brothers',
      'Marriott','MCI','Merrill Lynch','Microsoft','Morgan Stanley','Sun Microsystems','Travelers','US Airways',
      'Warner-Lambert']


# In[7]:


#to find outliers plot bloxplot

sns.boxplot(df)


# In[6]:


plt.figure(figsize=(6,8))
plt.pie(df,labels=company,autopct='%1.0f%%')
plt.show()


# In[8]:


#to find mean
df.mean()


# In[9]:


#to find sd
df.std()


# In[11]:


#to find var
df.var()


# In[12]:





# In[ ]:




