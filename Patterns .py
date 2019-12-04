#!/usr/bin/env python
# coding: utf-8

# In[87]:


for i in range(1,6):
    print("*"*i)


# In[90]:


for i in range(1,6):
    print(" "*(6-i) +"*"*i)


# In[54]:



for i in range(5,0,-1):
    print("*"*i)


# In[111]:


for i in range(1,6):
    print(' '*(6-i) + " *"*i)


# In[85]:


for i in range(1,6):
    print(' '*(6-i) + "*"*i)


# In[105]:


tmp = ''
for i in 'python':
    tmp = tmp + i
    print(tmp)


# In[137]:


tmp = ''
str='python'
for i in 'python':
    tmp = tmp + i
    print(tmp)


# In[45]:


temp=1
for row in range(1,6):
    for col in range(1,row+1):
        print(temp,end=' ')
        temp=temp+1
    print("\n")
    


# In[4]:


str1


# In[4]:


temp=1
for i in range(1,6):
    print(f' {temp}'*i)
    temp=temp+1


# In[19]:



for row in range(1,6):
    for col in range (1,6):
        if(col>=row):
            print(row, end=' ')
    print("\n")      
        


# In[ ]:





# In[ ]:




