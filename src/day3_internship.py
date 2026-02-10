# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:14:50 2026

@author: imama sab
""""
#Task1

#creating student list

student_list=["rahul",22,8.36]
print(student_list)

#indexing into the list

student_list=["rahul","22","8.36"]
print(student_list[0])
print(student_list[1])
print(student_list[2])

#Adding student data into the list

student_list=["rahul","22","8.36"]
student_list.append(9)
print(student_list)

#sorting student data into the list

student_list=["3","1","2","8.36","9"]
student_list.sort()
print(student_list)

#poping student data into the list

student_list=["3","1","5","8.36","9"]
student_list.pop(2)
print(student_list)

#creating a list

list1=["apple","banana","grapes","dates","mango"]
print(list1)

list1=["apple","banana","grapes","dates","mango"] #adding the data
list1.append("watermelon")
print(list1)

list1=["apple","banana","grapes","dates","mango"] #slcing the data 
print(list1[1:2])
print(list1[2:])
print(list1[:4])
print(list1[0:2:4])

list1=["apple","banana","grapes","dates","mango"] #storing newlist into lodlist
new_list=["a","b","c","d"]
list1.append(new_list)
print(list1)

data1=("python",1,3.14,True) #creating a tuple
print(data1)

 #Task2
 
 #create a list named as temperature
 Temp=[23,26,30,42,40,43,45]
 print(Temp[0])
 print(Temp[-1])
 
 #slicing the Temp
 Temp=[23,26,30,42,40,43,45]
 print(Temp[3:6])
 print(Temp[-3:])
 
 #Task3
 
 screen_res=(1920,1080)
 print("current_resolution:1980x1080")
 
screen_res=1280 
print(screen_res)












