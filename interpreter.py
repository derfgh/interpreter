# -*- coding: utf-8 -*-


"""

variables = {}


def detect_syntax_errors(line):
    tokens = line.split()
    if len(tokens) != 3:
        return True
   
    if tokens[1] != '=':
        return True 
    if not tokens[0].isalpha() and tokens[0] != '_':
        return True
 
    if tokens[2].isalpha() or tokens[2].isdigit() or tokens[2] == '_':
        return False
    else:
        return True

def report_uninitialized_variables(line):
   
    tokens = line.split()
   
    if tokens[0] in variables:
        return False
    else:
        return True



def perform_assignments(line):
  
    tokens = line.split()
   
    variables[tokens[0]] = tokens[2]



def print_variables():
   
    for key, value in variables.items():
        
        print(key + '=' + value)

lines = input().split(';')

for line in lines:
    
    if detect_syntax_errors(line):
        print('Syntax Error')
        break
   
    if report_uninitialized_variables(line):
        print('Uninitialized Variable')
        break
    perform_assignments(line)
print_variables()
