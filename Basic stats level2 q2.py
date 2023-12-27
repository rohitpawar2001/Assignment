#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy import stats
from scipy.stats import norm


# In[2]:


# p(X>44); Employees older than 44 yrs of age
1-stats.norm.cdf(44,loc=38,scale=6)


# In[3]:


# p(38<X<44); Employees between 38 to 44 yrs of age
stats.norm.cdf(44,38,6)-stats.norm.cdf(38,38,6)


# In[4]:


# P(X<30); Employees under 30 yrs of age
stats.norm.cdf(30,38,6)


# In[5]:


# No. of employees attending training program from 400 nos. is N*P(X<30)
400*stats.norm.cdf(30,38,6)


# In[6]:


#Assignment-2-Set2-Q5 (Basic Statistic Level-2)


# In[7]:


# Mean profits from two different divisions of a company = Mean1 + Mean2
Mean = 5+7
print('Mean Profit is Rs', Mean*45,'Million')


# In[8]:


# Variance of profits from two different divisions of a company = SD^2 = SD1^2 + SD2^2
SD = np.sqrt((9)+(16))
print('Standard Deviation is Rs', SD*45, 'Million')


# In[9]:


# A. Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
print('Range is Rs',(stats.norm.interval(0.95,540,225)),'in Millions')


# In[10]:


# B. Specify the 5th percentile of profit (in Rupees) for the company
# To compute 5th Percentile, we use the formula X=μ + Zσ; wherein from z table, 5 percentile = -1.645
X= 540+(-1.645)*(225)
print('5th percentile of profit (in Million Rupees) is',np.round(X,))


# In[11]:


# Probability of Division 1 making a loss P(X<0)
stats.norm.cdf(0,5,3)


# In[12]:


# Probability of Division 2 making a loss P(X<0)
stats.norm.cdf(0,7,4)


# In[ ]:




