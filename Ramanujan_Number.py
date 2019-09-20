#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:06:41 2019

@author: newuser
"""

n = int(input('Enter n:'))
cubic_limit = n*n*n
dic = {}

for a in range(1,n):
    a_cb = a*a*a
    for b in range(1,n):
        b_cb = b*b*b
        if(a_cb+b_cb>cubic_limit):
            break
        for c in range(1,n):
            c_cb = c*c*c
            if(c_cb > (a_cb + b_cb)):
                break
            for d in range(1,n):
                d_cb = d*d*d
                if(a_cb + b_cb == c_cb + d_cb and a!=c and a!=d and b!=c and b!=d):
                    if((a_cb + b_cb) in dic.keys()):
                        continue
                    else:
                        dic[a_cb + b_cb] = str(a)+'cb + '+str(b)+'cb == '+str(c)+'cb + '+str(d)+'cb'
                        
for i in dic.keys():
    print("{} = {}".format(i,dic[i]))