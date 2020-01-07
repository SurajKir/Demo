#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 09:52:55 2020

@author: newuser
"""
from Utility import mul, div, add, sub, bracketValidator, validateOperator


def parse(expression):
    operators = set('+-*/')
    operator_out = []
    number_out = []
    buffer = []
    
    expression = validateOperator(expression)
#    print(expression)
    
    for i in expression:
        
        if i in operators:
            number_out.append(''.join(buffer))
            buffer = []
            operator_out.append(i)
        else:
            buffer.append(i)
    number_out.append(''.join(buffer))
    
    return number_out,operator_out


def expressionEval(expression):
    number_out, operator_out = parse(expression)
    numbers = list(number_out)
    operators = list(operator_out)
    operator_precedence = ('*/','+-')
    
    operator_dict = {'*':mul,
                    '/':div,
                    '+':add,
                    '-':sub}
    
    for op in operator_precedence:
        while(any(operator in operators for operator in op)):
            
            index, to_use_operator = next((i, operator) for i,operator in 
                                          enumerate(operators) if operator in op)
            
            operators.pop(index)
            values = map(float,numbers[index:index+2])
#            print(numbers[index:index+2])
            value = operator_dict[to_use_operator](*values)
            numbers[index:index+2] = [value]
            
    return numbers[0]


def bracketEval(expression):
    if(bracketValidator(expression) == False):
        return False
    
    bracket_count = 0
    open_bracket = {}
    for i in range(len(expression)):
        if(expression[i] == '('):
            bracket_count += 1
            open_bracket[bracket_count] = i
    
    for i in range(len(open_bracket)+1):
        if(bracket_count==0):
            value = expressionEval(expression)
            return value
        
        for j in range(open_bracket[bracket_count]+1,len(expression)):
            if(expression[j]==')'):
                close_bracket = j
                break
        try:
            value = expressionEval(expression[(open_bracket[bracket_count]+1):close_bracket])
            expression = expression[:open_bracket[bracket_count]] + str(value) + expression[(close_bracket+1):]
            bracket_count -= 1
        except:
            raise('Invalid Expression')


expression = input()
print(bracketEval(expression))
