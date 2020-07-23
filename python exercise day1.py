#!/usr/bin/env python
# coding: utf-8

# ### The questions for the exercises are given above the cells and the expected output is given below the cell. Please type the code inserting a new cell below the question because if you run the expected output cell the output would vanish! Happy learning! 

# ## Exercise Question 1: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list

# In[1]:


l1=[34, 54, 67, 89, 11, 43, 94]
print(l1)
l1.pop(4)
print(l1)
l1.insert(2,11)
print(l1)
l1.append(11)
print(l1)


# ## Exercise Question 2: Given a Python list you should be able to display Python list in the following order

# In[2]:


ls1=[100, 200, 300, 400, 500]
print(ls1)
ls1.sort(reverse=True)
print(ls1)


# ## Exercise Question 3: Concatenate (join) two lists in the following order
# 

# In[4]:


ls1=['Hello ', 'take ']
ls2=['Dear', 'Sir']
ls3=ls1+ls2
print(ls3)


# ## Exercise Question 4: Add item 7000 after 6000 in the following Python List

# In[6]:


l1=[10, 20, [300, 400, [5000, 6000], 500], 30, 40]
l1[2][2].append(7000)
print(l1)


# ## Exercise Question 5: Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the

# In[14]:


list1=['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
list1[2][1][2].extend(('h','i','j'))

print(list1)


# ## Exercise Question 6: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

# In[15]:


l1=[5, 10, 20, 25, 50, 20]
l2=l1.index(20)
l1[l2]=200
print(l1)


# In[17]:


ls3=[5, 10, 15, 20, 25, 50, 20]
a=0
for x in ls3:
    if x == 20:
        ls3[a]=200
        break
    a+=1
print(ls3)


# In[ ]:




