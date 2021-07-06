#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


print('matplotlib version: ',mpl.__version__)


# In[4]:


print(plt.style.available)


# In[5]:


from numpy.random import randn,randint,uniform,sample


# In[6]:


#Line plot
## simple example
x=np.arange(0,10)
y=np.arange(11,21)


# In[8]:


x
y


# In[11]:


plt.plot(x,y)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')


# In[15]:


plt.plot(x, y, 'go--', linewidth=1, markersize=5)


# In[16]:


x=np.arange(1,11)
y=3*x+5
plt.plot(x,y)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')


# In[17]:


x


# In[18]:


y


# In[19]:


np.pi


# In[23]:


##Assignment-1 
#Ques-1

x=np.arange(0,10)
y=x*x
plt.plot(x,y,'r*',linestyle='dashed',linewidth=2,markersize=10)


# In[24]:


y


# In[26]:


x=np.arange(1,10)
y=3*x+10

##plt plot
plt.plot(x,y,'ro--')

##plt.plot(x,y,'r*',linestyle='dashed',linewidth=2,markersize=12)
plt.xlabel('X-axis',color='blue')
plt.ylabel('Y-axis',color='blue')
plt.title('2D-diagram',color='blue')


# In[30]:


## Creating Subplot

plt.subplot(2,2,1)
plt.plot(x,y,'ro--')
plt.subplot(2,2,2)
plt.plot(x,y,'g*--')
plt.subplot(2,2,3)
plt.plot(x,y,'b.--')
plt.subplot(2,2,4)
plt.plot(x,y,'y+--')


# In[32]:


## Assignment-1 Ques-2

x=[1,2,3,4,5,6,7]
y=[160,150,140,145,175,165,180]
plt.plot(x,y,'bo--')
plt.title('Sales per day',color='blue')
plt.xlabel('Days of d week')
plt.ylabel('Sales')


# In[33]:


## Practice question 
a=np.arange(40,50)
b=np.arange(50,60)
plt.plot(x,y,'bo--')
plt.show()


# In[ ]:




