#!/usr/bin/env python
# coding: utf-8

# 1 Write a Python Program to implement your own myreduce() function which works exactly  like Python's built-in function reduce() 
# 

# In[20]:


def sum(x,y): 
    return x + y

def myreduce(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
    return first

print(myreduce(sum, [23,45,67,89,56]))


# 2 Write a Python program to implement your own myfilter() function which works exactly  like Python's built-in function filter() 

# In[33]:


def myfilter(fun,alist):
    x = []
    y = []
    
    for i in alist:
        x.append(fun(i))
        
    for i in range(0,len(x)):
        if x[i] == False:
            continue
        else:
            y.append(x[i])
            
    return y
def multiple_three(i):
    
    if i % 3 == 0:
        return i
    else:
        return False
print(myfilter(multiple_three,[3,5,6,7,8,9,12,15,18,21,22,27]))


# 2. Implement List comprehensions to produce the following lists.  
# Write List comprehensions to produce the following Lists 
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] 
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']  
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']  
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],  
# [4, 5, 6, 7], [5, 6, 7, 8]] 
# 

# In[2]:


word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print("ACADGILD => " + str(alphabet_list))


# Compress above for loop into a single list comprehension using technique [i <Upper for condition> <lower for condition>]
input_list = ['x','y','z']
result = [item*num for item in input_list for num in range(1,5)]
print("['x','y','z'] => " +   str(result))


# Compress above for loop into a single list comprehension using technique [i <Upper for condition> <lower for condition>]
input_list = ['x','y','z']
result = [item*num for num in range(1,5) for item in input_list]
print("['x','y','z'] => " +   str(result))


input_list = [2,3,4]
result = [[item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))


input_list = [2,3,4,5]
result = [[item+num for item in input_list] for num in range(0,4)]
print("[2,3,4,5] =>" +  str(result))

input_list=[1,2,3]
result = [(b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# In[ ]:




