#!/usr/bin/env python
# coding: utf-8

# # Flatten Funciton

# In[25]:


input_list = [[[1,2,3],[4,5,6],"a"],[[14,25,36]],[["cat"],["dog"]]]

flatten_list= [c for k in input_list for i in k for c in i]

print(flatten_list)

