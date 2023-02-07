#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[6]:


df1 = pd.read_csv('file1.csv')
df1


# In[ ]:


##Show the dataframe shape.##


# In[7]:


df1.shape
df1


# In[ ]:


##Standardize header names.##


# In[8]:


df1.columns


# In[ ]:


##Which columns are numerical?##


# In[9]:


df1.describe()


# In[ ]:


##Which columns are categorical?


# In[11]:


df1.dtypes


# In[ ]:


##Check and deal with NaN values.


# In[12]:


df1.isna()


# In[ ]:


##Datetime format - Extract the months from the dataset and store in a separate column. Then filter the data 
to show only the information for the first quarter , ie. January, February and March. Hint: If data from March 
    does not exist, consider only January and February.##


# In[15]:


file1 = pd.read_csv('file1.csv')  # index_col='Unnamed: 0'
file1#.dtypes


# In[30]:


file1['Monthly Premium Auto'] = pd.to_datetime(file1['Monthly Premium Auto'], errors='coerce')
file1['Monthly Premium Auto']


# In[31]:


file1['Monthly Premium Auto'][1].month # .month   #.year   #.isoweekday() # .time()


# In[32]:


file1['Monthly Premium Auto'][2].month


# In[35]:


import datetime 
file1


# In[41]:


file1['year'] = pd.DatetimeIndex(file1['Month']).year
file1.head()


# In[38]:


df1['month'] = pd.DatetimeIndex(df1['1']).month
df1.head()


# In[ ]:


df['month_year'] = pd.to_datetime(df['birth_date']).dt.to_period('M')


# In[ ]:


##BONUS: Put all the previously mentioned data transformations into a function.##


# In[ ]:


Note: I am not sure whether I am solving the last "datetime" question correctly. 
I checked with other classmates as well. Tried to implement those functions but still not getting through.Can you please check it and correct it.

