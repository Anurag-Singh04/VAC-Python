#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[17]:


df = pd.read_csv("data.csv")
plt.plot(df["Month"],df["Sales_INR"],marker = 'o')
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()


# In[19]:


df = pd.read_csv("data.csv")
plt.bar(df["Month"],df["Sales_INR"])
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()


# In[31]:


df = pd.read_csv("data.csv")
plt.pie(df["Sales_INR"],labels=df["Month"],autopct='%1.1f%%')
plt.title("Monthly Sales")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




