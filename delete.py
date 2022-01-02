# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:09:11 2020

@author: 23978
"""
a="a1,a2,a3,b4,b5,b6"
i=0
for j in range(i,len(a)-1):
    for h in range(i+1,len(a)-1):
         if a[j]==a[h]:
            a=a.replace(a[i],"")
    i=i+1
    if i==len(a)-1:
       break
print(a)                                     