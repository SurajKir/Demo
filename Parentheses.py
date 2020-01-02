#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:37:07 2019

@author: newuser
"""

string = input()
stack = []
flag = 1
for i in string:
    if(i=='('):
        stack.append(i)
    elif(i==')'):
        if(len(stack)==0):
            flag = 0
            print('The first offender is at [{}] index.'.format(string.index(i)))
            break
        else:
            stack.pop()
    else:
        flag = 0
        print('The first offender is at [{}] index.'.format(string.index(i)))
        break
        
if(len(stack)==0 and flag!=0):
    print(True)
else:
    print(False)