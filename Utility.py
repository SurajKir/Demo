#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:07:16 2020

@author: newuser
"""
def mul(x,y):
    return x*y


def div(x,y):
    return x/y


def add(x,y):
    return x+y


def sub(x,y):
    return x-y


def bracketValidator(string):
    stack = []
    flag = 1
    for i in string:
        if(i=='('):
            stack.append(i)
        elif(i==')'):
            if(len(stack)==0):
                flag = 0
                print('Invalid Expression. The first offender is at [{}] index.'.format(string.index(i)))
                break
            else:
                stack.pop()
            
    if(len(stack)==0 and flag!=0):
        return True
    else:
        return False
    

def validateOperator(expression):
    operators = '+-*/()'
    
    if(expression[0]=='-'):
        expression = '0' + expression   
    
    for i in range(len(expression)):
        
        if(expression[i] in operators and expression[i+1] in operators):
            
            if(expression[i]== '+' and expression[i+1] == '-'):
                expression = expression[:i] + expression[i+1:]
                return expression
            
            elif(expression[i]== '-' and expression[i+1] == '+'):
                expression = expression[:i+1] + expression[i+2:]
                return expression
            
            elif(expression[i]== '+' and expression[i+1] == '(' and expression[i+2] == '-'):
                
                close_bracket = 0
                
                for j in range(i+1,len(expression)):
                    if(expression[j]==')'):
                        close_bracket = j
                        break
                
                expression = expression[:i] + expression[i+2:close_bracket] + expression[close_bracket+1:]
                return expression
            
            elif(expression[i]== '-' and expression[i+1] == '(' and expression[i+2] == '+'):
                
                for j in range(i+1,len(expression)):
                    if(expression[j]==')'):
                        close_bracket = j
                        break
                    
                expression = expression[:i+1] + expression[i+3:close_bracket] + expression[close_bracket+1:]
                return expression
            
            elif(expression[i]== '-' and expression[i+1] == '(' and expression[i+2] == '-'):
                
                for j in range(i+1,len(expression)):
                    if(expression[j]==')'):
                        close_bracket = j
                        break
                    
                expression = expression[:i+1] + expression[i+3:close_bracket] + expression[close_bracket+1:]
                return expression
            else:
                return expression
                
    return expression
                
                