#!/usr/bin/env python
# coding: utf-8

# In[3]:


def subList(*args):
    for i in args:
        print(i)


# In[7]:


subList([1,2,3,4],[1],[33],'hello')


# In[22]:


def subDict(**kargs):
        print(kargs)


# In[24]:


subDict(apple='f',kiwi='170')


# In[26]:


def MyChoice(*args,**kargs):
    print(args)
    print(kargs)


# In[28]:


MyChoice(10,20,30,fruit='orange',fruit1='kiwi')


# In[33]:


def myfunc(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum


# In[34]:


myfunc(1,2,3,4)	


# In[35]:


def myfunc(*args):
    return [i for i in args if i%2==0]
            
            
           


# In[36]:


myfunc(1,2,3,4)	


# In[57]:


def myfunc(*args):
    for latter in list(args):
        print(latter)


# In[58]:


myfunc('pawan')	


# In[63]:


name='abcdef'
for i in range(len(name)):
    if name[i]=
    print(f"position is{[i]}",f"and element is{name[i]}")


# In[ ]:





# In[ ]:




