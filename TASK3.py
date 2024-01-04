#!/usr/bin/env python
# coding: utf-8

# # Task-3
# 
1) Write a Python program to sum all the items in a list.
# In[143]:


l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    sum=l[0]+l[1]+l[2]+l[3]+l[4]+l[5]+l[6]+l[7]+l[8]+l[9]
sum

2)Write a Python program to get the largest number from a list.

# In[144]:


list=[32,56,28,100,90,86]
list.sort()
print("the largest number from the list is:",list[-1])

3)Write a Python program to remove duplicates from a list.

# In[2]:


# converting the list to set to remove duplicate values
l=[1,1,3,4,4,7,7,7,8,8,9,10] 
a=set(l)
list(a)

4)Write a Python program to check if a list is empty or not.
# In[146]:


thislist=[]
len(thislist)
if len(thislist)==0:
    print("This list is empty")
else:
    print("This list is not empty")  

5)Write a Python program to filter the list if the length of the character is< 4
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result: ['abc', 'xyz', 'aba']

# In[1]:


samplelist=['abc', 'xyz', 'aba', '1221']
ExpectedResult=[]
for i in samplelist:
    if len(i)<4:
        ExpectedResult.append(i)
print(ExpectedResult)

6)Write a Python program to find the second largest number in a list.

# In[148]:


list=[32,56,28,100,90,86]
list.sort()
print("the second largest number from the list is:",list[-2])

7)Write a Python program to reverse a list at a specific location.

# In[167]:


mylist=["apple","ball","cat"]
mylist.reverse()
a=mylist
print("Reversed list:",a)

8)Write a Python program to check if a list is a palindrome or not. Return true otherwise false.
# In[4]:


lst=["m","a","l","a","y","a","l","a","m"]
a=lst.copy()
lst.reverse()
b=lst
if a==b:
    print("The list is palindrome")
else:
    print("The list is not Palindrome")

10. Write a Python a program to find the union and intersection of two lists.
# In[2]:


list1=[1,2,3,4,5,6,7]
list2=[1,2,3,8,9,10,11]
Union=print(set(list1) | set(list2))
Union
Intersection=print(set(list1) & set(list2))
Intersection


# In[12]:


#11 sort by value
d = {'a':1, 'd':3,'s':2,'g':4}
res = {}
values = sorted(d.values())
for i in values :
    for k,v in d.items():
        if v == i:
            res[k] = v
print("Ascending: ",res)
print("Descending: ",dict(reversed(list(res.items))))


# In[4]:


#12 
dic = {'a':33,'b':32,'f':322}
key = 'f'
if key in dic.keys():
        print("Present, ", end =" ")
        print("value =", dic[key])
else:
        print("Not present")


# In[5]:


#13
dic = {'a':33,'b':32,'f':322}
values = list(dic.values())
print(sum(values))


# In[6]:


#14 
n=int(input("Input a number less than 10 "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 


# In[7]:


#15 sort dictionary by key
dict = {'a':1, 'd':3,'s':2,'g':4}
keys = list(dict.keys())
keys.sort()
sorted_d = {i : dict[i] for i in keys}

print(sorted_d)


# In[8]:


#16 
s = "Hello Welcome"
dic = {}
for i in s :
    dic[i] = dic.get(i,0)+1
print(dic)


# In[9]:


#17 

from heapq import nlargest
from operator import itemgetter
items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)


# In[ ]:




