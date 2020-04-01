#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:57:33 2019

@author: yuyiding
"""

b=input()
b=int(b)
n=input()
n=int(n)

a=float(0)

for i in range(1,n+1):                              
    q=float(input())
    if q>=200:
        q=q-40
    elif q>=100 and q<200:
        q=q-15
    elif q>=50 and q<100:
        q=q-5
    else:
        q=q
    a=a+q