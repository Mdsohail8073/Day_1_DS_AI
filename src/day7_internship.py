# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:17:39 2026

@author: MD SOHAIL
"""
#Topic 1
#writing a file
file=open("new.text","w")
file.write("Hello all")
file.close()

#using append into a file
file=open("new.text","a")
file.write("welcome all")
file.close()

#reading  a  file
file=open("new.text","r")
content=file.read()
print(content)
file.close()

#Topic 2
with open("new.text","r") as file:
    content=file.read()
    print(content)

#Topic 3
#create a data.csv file
import csv
 
with open("sohail.csv") as file:
    reader=csv.reader(file) #reads structured row
    for row in reader: #reads line by line
        print(row)

#Topic 4
 try:
     with open("new.text", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found error, please check the filename")

#Topic 5
with open("new.text","w+") as file:
    file.write("its sohail")
    file.seek(0,0)
    content=file.read()
    print(content)
    
#Task 1
name=input("Enter your name:")
goal=input("enter your daily goal:")

with open("journal.txt","a") as file :
    file.write(f"{name}-{goal}\n")
    
with open("journal.txt","r") as file:
    a=file.read()
    print(a)
    
#Task 2
import csv 
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Students who have passed:")
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
            
#Task 3
 
filename = input("Enter the filename(e.g., config.txt): ")

try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
