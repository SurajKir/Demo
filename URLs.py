#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:18:38 2019

@author: newuser
"""


visited_URLs = []
flag = 1
print('To exit enter "0"')

while(flag != 0):
    url = input()
    if(url in visited_URLs):
        print('Already visited.')
    elif(url == '0'):
        flag = 0
        break
    else:
        visited_URLs.append(url)
        print('URL added.')


