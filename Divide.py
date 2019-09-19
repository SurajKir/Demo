# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def multiply(x,y):
    if(y<0 and x<0):
        return multiply(abs(x),abs(y))
    elif(y<0 or x<0):
        return -multiply(abs(x),abs(y))
    elif(y==0 or x==0):
        return 0
    elif(x==1):
        return y
    elif(y==1):
        return x
    else:
        return x + multiply(x, y-1)
    
    
def divide(x,y):
    if(y==0):
        raise Exception('Divide by Zero')
    elif(x==0):
        return 0
    
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
            return i
    
    while(multiply(curr_quo, y)<x):
        curr_quo += 0.01
        
    return curr_quo


print(divide(5,2))