#Task 1
a=7
b=8
c=a+b
print(type(a+b),a+b)
print(type(a-b),a-b)
print(type(a*b),a*b)
print(type(a/b),a/b)
print(type(a//b),a//b)
print(type(a%b),a%b).
print(type(a**b),a**b)

#Asking the name of the person
name=input("Enter the name :-")
#Asking the age of the person
age=input("Enter the age:- ")
#converting string into integer
age=int(age)
#calculating the age of person in 2030
age+=4
#display the age of the person
print(f"hi {name}, you will be {age} years old in 2030")

#Task 2
#total bill amount
Amount=float(input("Enter the Amount:- "))
#Number of peoples 
peoples=int(input("Enter the Number:- "))
#spliting the amount per person
Shares = Amount / peoples
#display the share of each person
print(f"Total Bill{Amount}, each person pays {Shares}")

#Task 3
#Creating four variables item_name, quantity, price, in_stock
item_name ="Smartphone"
quantity=5
price=19000
in_stock=True
#print statement
print(f" item: {item_name}, qty:{quantity}, price:{price}, Available:True")
#calculating the total cost 
total_cost=quantity*price
#print the Total cost
print("The total cost is : ", total_cost)
