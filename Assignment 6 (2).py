#!/usr/bin/env python
# coding: utf-8

# ## Q.1 
# ## Keyword 

# Keywords in python are reserved words that connot be used as the ordinary identifires.They are used to define the syntex and stucture of python languge. 

# In[5]:


# All python keywords
import keyword 
print(keyword.kwlist)


# # Q.2

# # Variable
# variable is like a container that holds data. Very similar to how our containers in the kitchen holds items . Creating a variable is like a placeholder in the memory and assigning it some value .

# ### Rules to create variables in python

# 1. Varible names should start with alphabets
# 2. variable names should not contain any special character like ^%&@#&

# # Q.3

# ## Nomenclature of variables

# In Python, the names of variables should be lowercase. Individual words can be separated by underscores when needed. This will improve readability and maintainability within your code. Method names should follow the same conventions as function names.

# # Q.4

# when we know that keywords are the reserved words that cannot be used as ordinary identifier. So, when we use keyword as variable tha error will shown . As shown bellow

# In[7]:


class = 10


# In[8]:


return = "adi"


# so we can use them but after some modification

# In[13]:


class_no = 10


# In[15]:


print(class_no)


# # Q.5

# ### def keyword
# 

# def( ) keyword in python is used to define the function that users can use to built their own function. They are used to define the syntex and stucture of thr python language

# # Q.6

# ### \ (Backslash)
# In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return. Conversely, prefixing a special character with \ turns it into an ordinary character.

# # Q.7

# ### (1) Hetrogeneous list 
#  In Python, lists can contain heterogeneous data types and objects. For instance, integers, strings, and even functions can be stored within the same list.

# ### (2) Hetrogeneous sets
# In Python, sets  can store heterogeneous data types and objects in it,i.e.,a setcan store  integers, strings,boolean and  even functions  within it.

# ### (3)Homogeneous tuple
# In Python, tuples can contain homogeneous data types and objects. For instance only integers/strings/boolean etc. can be stored within the same tuple

# # Q.8

# ### Mutable Data type
# An object that allows you to change its values without changing its identity is a mutable object. The changes that you can perform on a mutable object's value are known as mutations. Example-lists 

# ### Immutable Data type
# An object that don't allow you to change its values or identity is an Immutable object . They cannot be modified after creation . Example- tuples
# 

# # Q.9

# In[3]:


n = 5

# Loop through each row
for i in range(n):
  # Print spaces before the stars
  print(" " * (n - i - 1), end="")
  # Print stars in increasing order
  print("*" * (2 * i + 1))


# # Q.10

# In[2]:



n = 5

# Loop through each row
for i in range(n):
  # Print spaces before the exclamation marks
  print(" " * i, end="")
  # Print exclamation marks in decreasing order
  print("!" * (2 * (n - i) - 1))


# In[ ]:




