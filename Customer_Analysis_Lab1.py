#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


df1 = pd.read_csv('file1.csv')


# In[6]:


df2 = pd.read_csv('file2.csv')


# In[7]:


df3 = pd.read_csv('file3.csv')


# In[8]:


df1


# In[9]:


df2


# In[10]:


df3


# In[ ]:


##Show the DataFrame's shape.##


# In[11]:


shape = df1.shape
print('\nDataFrame Shape:', shape)


# In[ ]:


###Standardize header names.##


# In[12]:


df1.columns


# In[13]:


df2.columns


# In[14]:


df3.columns


# In[15]:


df1.index


# In[ ]:


##Rearrange the columns in the dataframe as needed##


# In[ ]:


new_columns = ['Customer','Gender','State','Education','Income','Customer Lifetime Value', 
        'Monthly Premium Auto', 'Number of Open Complaints',
       'Policy Type', 'Total Claim Amount', 'Vehicle Class']
df3 = df3[new_columns]


# In[49]:


df3


# In[ ]:


##Concatenate the three dataframes##


# In[53]:


data = pd.concat([df1, df2, df3])
data.tail(15)


# In[54]:


data = pd.concat([df1, df2, df3])
data.head(15)


# In[ ]:


##Which columns are numerical?##


# In[56]:


df1.describe()


# In[ ]:


##Which columns are categorical?##


# In[60]:


df1.dtypes


# In[ ]:


##Understand the meaning of all columns##


# In[ ]:


##Perform the data cleaning operations mentioned so far in class##

Delete the column education and the number of open complaints from the dataframe.
Correct the values in the column customer lifetime value. They are given as a percent, 
so multiply them by 100 and change dtype to numerical type.
Check for duplicate rows in the data and remove if any.
Filter out the data for customers who have an income of 0 or less.


# In[58]:


df1.drop(['Education','Number of Open Complaints'], axis=1)
df1.columns


# In[69]:


df1.duplicated


# In[8]:


##Correct the values in the column customer lifetime value. They are given as a percent, 
so multiply them by 100 and change dtype to numerical type.##


# In[9]:


import pandas as pd
import numpy as np


# In[12]:


df1 = pd.read_csv('file1.csv')


# In[14]:


df1['Customer Lifetime Value'] = df1['Customer Lifetime Value'].str.replace(r'%', '') 


# In[18]:


df1['Customer Lifetime Value'] = df1['Customer Lifetime Value'].astype(float) # converts the strings into floats 


# In[19]:


df1['Customer Lifetime Value'] = round(df1['Customer Lifetime Value'],0) 


# In[20]:


df1


# In[22]:


df1['Customer Lifetime Value']  = df1['Customer Lifetime Value'] *100
df1.head() 


# In[ ]:


##Filter out the data for customers who have an income of 0 or less.##


# In[24]:


df1['Income'] =df1[df1['Income'] > 0]['Income'] #drop values lower than 0


# df1['income'] = df1[df1'income'] > 0]['income'] 
# print("Count of clients with an income less than 1 = ",
#      df1[df1['income'] < 1]['income'].count())

# In[28]:


print("Count of clients with an income less than 1 = ",
     df1[df1['Income'] < 1]['Income'].count())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




