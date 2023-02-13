#!/usr/bin/env python
# coding: utf-8

# # Reverse Function

# In[3]:


input_list= [[1, 2], [3, 4,5], [6, 7]]
k=[]
l=[]

for i in range(len(input_list)):
    k.append(input_list[i][::-1])

l.append(k[::-1])
            
print(k)
print(l)

