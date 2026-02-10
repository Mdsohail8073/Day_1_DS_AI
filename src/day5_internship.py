# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 15:57:07 2026

@author: MD SOHAIL
"""

# define two functions
def Text():
    print("welcome to college")
Text()

#write a function arguments and return value
def add(a,b):
    return a+b
result=add(3,2)
print(result)

# identify local or global
x=5
def show():
   x=4
   print(x)
show()
print(x)

#changing global 
x=5
def update():
   global x
   x=20
update()
print(x)

 #create a module
import math
import random
print(math.sqrt(16)) 
print(random.randint(1,10))

#  create file and import

def multifly(a, b):
    return a * b

print(multifly(4, 5))

# Task1
def calc_rectangle(length,width):
    area = length * width
    perimeter = 2 *(length+width)
    return area,perimeter # returnig both as tuple
# taking input 
length =float(input("enter length"))
width =float(input("enter width"))
# function call
area,perimeter =calc_rectangle(length,width) 
# print the function
print(f"Area:{area} , Perimeter:{perimeter}")

#Task 2