#!/usr/bin/env python
# coding: utf-8

# In[22]:


friends = {}
friends['joey'] = [30, 'mathias']
friends['catherine'] = [31, 'guarnieri']
friends['liam'] = [29, 'mcmahon']
friends['ryan'] = [32, 'dougherty']
friends['george'] = [33, 'lauinger']
print(friends)


# In[24]:


friends.pop('george')
print(friends)


# In[26]:


joey[0] = 35


# In[27]:


print(friends)


# In[36]:


print(joey)


# In[29]:


print(friends)


# In[30]:


friends['joey'] = [35, 'mathias']
print(friends)


# In[46]:


ages = []
for person in friends:
    ages.append(friends[person][0])
    print(ages)


# In[47]:


names = []
for person in friends:
    names.append(friends[person][1])
    print(names)


# In[ ]:




