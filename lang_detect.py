
# coding: utf-8

# In[97]:


import langid
#it cannot detect hinglish but our users will either use english or hinglish 
#so i am considering that if detect is not english then it is hinglish


# In[98]:


#input
ip=input("write somethin ")


# In[99]:


lang=langid.classify(ip)[0]


# In[100]:


if lang=='en':
    print('language is english')
    
else:
    print('language is hinglish')


# In[88]:




