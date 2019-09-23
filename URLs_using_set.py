#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:30:55 2019

@author: newuser
"""

visited_URLs = set()
flag = 1
print('To exit enter "0"')
last_len = len(visited_URLs)

while(flag != 0):
    url = input()
    if(url == '0'):
        break
    visited_URLs.add(url)
    curr_len = len(visited_URLs)
    if(curr_len == last_len):
        print('Already Visited.')
    else:
        print('URL added to the set.')
    last_len = len(visited_URLs)
