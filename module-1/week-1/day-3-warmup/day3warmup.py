#!/usr/bin/env python
# coding: utf-8

# In[1]:


friends = {}
friends['joey'] = [30, 'mathias']
friends['catherine'] = [31, 'guarnieri']
friends['liam'] = [29, 'mcmahon']
friends['ryan'] = [32, 'dougherty']
friends['george'] = [33, 'lauinger']
print(friends)


# In[2]:


friends.pop('george')
print(friends)


# In[4]:


print(friends)


# In[6]:


print(friends)


# In[7]:


friends['joey'] = [35, 'mathias']
print(friends)


# In[8]:


ages = []
for person in friends:
    ages.append(friends[person][0])
    print(ages)


# In[9]:


names = []
for person in friends:
    names.append(friends[person][1])
    print(names)


# In[ ]:




