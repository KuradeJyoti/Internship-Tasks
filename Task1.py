#!/usr/bin/env python
# coding: utf-8

# Name:- Jyoti Suresh Kurade

# Data Science and Buisness Analytics Internship

# TSF GRIPMARCH23

# Task1:- Pridiction Using Supervised ML(Pridict the percentage of student based on the number of study         hours.)
# 
# Algorithm:- Linear Regresion
# 
# 1) Required Libraries

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 2) Import Data using URL

# In[12]:


url="http://bit.ly/w-data"
data=pd.read_csv(url)
data


# 3) Data Cleaning

# In[9]:


data.shape
print("Name of Columns: ",data.columns)


# In[2]:


data.isna().values.any()


# In[10]:


data.duplicated().sum()


# In[ ]:




