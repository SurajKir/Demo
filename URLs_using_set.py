#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:30:55 2019

@author: newuser
"""
def urlAdd(set, url):
    last_len = len(set)
    set.add(url)
    curr_len = len(set)
    if(last_len == curr_len):
        return False
    else:
        return True


visited_URLs = set()
flag = 1
print('To exit enter "0"')

while(flag != 0):
    url = input()
    if(url == '0'):
        break
    if(urlAdd(visited_URLs, url)):
        print('URL added to the set.')
    else:
        print('Already Visited')
