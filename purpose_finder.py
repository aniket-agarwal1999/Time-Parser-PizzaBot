
# coding: utf-8

# DATASET

# In[87]:




# INPUT

# In[85]:


ip="i want to order movie"
iplist=ip.split()


# PURPOSE ALGO

# In[86]:


purpose='none'
for item in iplist:
    try:
        purpose=data[item]
    except KeyError:
        continue

if purpose=='none':
    print('I did not understand')
else:
    print(purpose)

