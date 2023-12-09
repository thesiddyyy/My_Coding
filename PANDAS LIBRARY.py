#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('Pip install pandas')


# In[2]:


import pandas


# In[3]:


import pandas as pd


# # Creation of SERIES FROM SCALLER VALUE

# In[4]:


Series1=pd.Series([10,20,30])
print(Series1)


# In[7]:


Series2=pd.Series([10,20,30],index=['A','B','C'])
print(Series2)


# In[9]:


Series3=pd.Series([10,20,30,40,50,60],index=['A','B','C','D','E','F'])
print(Series3)


# # Creation of series from NUMPY ARRAY

# In[10]:


import numpy as np


# In[21]:


arr1=np.array([1,2,3,4])
Series5=pd.Series(arr1)
print(Series5)


# In[19]:


arr1=np.array([1,2,3,4])
Series5=pd.Series(arr1,index=['A','B','C','D'])
print(Series5)


# # Creation of SERIES from DICTIONARY

# In[22]:


dict1={'India':'New Delhi','Uk':'London','Japan':'Tokyo'}
Series7=pd.Series(dict1)
print(Series7)


# # Access an element from series

# In[31]:


Series8=pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
print(Series8[['A','C','D']])


# In[ ]:





# In[ ]:




