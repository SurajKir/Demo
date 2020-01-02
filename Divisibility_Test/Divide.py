# -*- coding: utf-8 -*-
"""
Spyder Editor
//Changes done on remote server.//
This is a temporary script file.
""" 
def divide(x,y):
    if(y==0):
        raise Exception('Divide by Zero')
    elif(x==0):
        return 0
    elif(x==y):
        return 1
    
    if(y<0 and x<0):
        return divide(abs(x),abs(y))
    elif(y<0 or x<0):
        return -divide(abs(x),abs(y))
    
    curr_quo = 0
    inc = y
    
    for i in range(int(x)):
        inc += y
        if(inc>x):
            curr_quo = i-1
            break
        elif(inc==x):
            return i+2
    
    while((curr_quo*y) < x):
        curr_quo += 0.01
        
    return curr_quo

