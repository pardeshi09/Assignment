#!/usr/bin/env python
# coding: utf-8

# ### 1. What is the result of the code, and explain?
# 

# X = 'iNeuron'
# def func():
#     print(X)
# func()
# 
# solution : 'iNeuron'
# Explamation:
# The global variables are accessible in side the functions in python. But we can not access function variable out side 
# function. 
# Since x is golbal variable we are able to print it in side the function
# 

# In[1]:


X = 'iNeuron'
def func():
    print(X)
func()


# ### 2. What is the result of the code, and explain?
# 
X = 'iNeuron'
def func():
    X = 'NI!'

func()
print(X)


solution: iNeuron
Explantion:
The global variables are access in side the functions in python. But we can not access function variable out side 
function. 
Since x is golbal variable we are able to print it out side of the function

# In[2]:


X = 'iNeuron'
def func():
    X = 'NI!'

func()
print(X)


# ### 3. What does this code print, and why?
# 
X = 'iNeuron'
def func():
    X = 'NI!'
    print(X)

func()
print(X)

Solution: NI!
          iNeuron
          
Since,The global variables are access in side the functions in python. But we can not access function variable out side 
function. X is updated with 'NI' which is local to function and its immutable. its name space is with in the function
# In[3]:


X = 'iNeuron'
def func():
    X = 'NI!'
    print(X)

func()
print(X)


# ### 4. What output does this code produce? Why?
# 
X = 'iNeuron'
def func():
    global X
    X = 'NI!'
    print(X)

func()
print(X)

Solution:NI!
         NI!
         
Since the X in side function is made Global, it will be accesible out side of the function too. now X will have new value.
# In[4]:


X = 'iNeuron'
def func():
    global X
    X = 'NI!'
    print(X)

func()
print(X)


# ### 5. What about this code—what’s the output, and why?
# 
X = 'iNeuron'
def func():
    X = 'NI'
def nested():
    print(X)

nested()
func()
X

Soltuion:
the nested() function will print 'iNeuron', Then func() does not display anything, and x ='NI' is not accessible out 
side the function.
The Solution : 'iNeuron'
# In[5]:


X = 'iNeuron'
def func():
    X = 'NI'
def nested():
    print(X)

nested()
func()
X


# ### 6. How about this code: what is its output in Python 3, and explain?
# 
X = 'kkl'
def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'spam'
    nested()
    print(X)

func()


Soltion:spam

Since, Nonlocal variables are used in nested functions whose local scope is not defined. 
This means that the variable can be neither in the local nor the global scope. it print the updated value from nested 
function

# In[ ]:


X = 'kkl'
def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'spam'
    nested()
    print(X)

func()

