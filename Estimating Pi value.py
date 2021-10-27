#!/usr/bin/env python
# coding: utf-8

# In[10]:


#This is a program to estimate pi value by randomly generating 2 uniform values in a func.
#We make use of a circle and square and the randomly generated points


# In[4]:


import random


# In[7]:


def estimate_pi(n):
    num_point_incircle=0
    num_point_total=0
    for i in range(n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        distance=x**2+ y**2
        if distance<=1:
            num_point_incircle+=1
        num_point_total+=1
    return 4*num_point_incircle/num_point_total
            
    


# In[9]:


estimate_pi(10000000)


# In[ ]:




