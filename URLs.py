#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:18:38 2019

@author: newuser
"""
def urlAdd(dict, url):
    hashed_url = hash(url)
    if(hashed_url in dict.keys()):
        return False
    else:
        dict[hashed_url] = url
        return True


visited_URLs = {}
flag = 1
print('To exit enter "0"')

while(flag != 0):
    url = input()
    if(url == '0'):
        flag = 0
        break
    if(urlAdd(visited_URLs, url)):
        print('URL added.')
    else:
        print('Already visited.')


