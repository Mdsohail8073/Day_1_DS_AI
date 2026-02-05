# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 10:55:04 2026

@author: MD SOHAIL
"""
#creating a dictionary
S1={"name":"alice","city":"glb","age":22}
print(S1)
print(S1["name"]) #acessinh keys
S1["name"]="bob" #update
print(S1)
del(S1["age"]) #deleting age
print(S1)

#using get()
S1={"name":"alice","city":"glb","age":22}
print(S1.get("name"))

for key , value in S1.item(): #iterate using item()
    print(key, value)
#creating two sets
x1={"1","9","2","4","6","8"}
x2={"1","3","4","5","7","10"}
common_values= x1 & x2
print(common_values,x1&x2)
unique_values= x1 | x2
print(unique_values,x1|x2)
Differance= x1 - x2
print(Differance, x1-x2)


#Task1
#Create dictionary
contacts={"rahul":"9988776655" ,"alice":"9897969594" ,"bob":"7899301717"}
print(contacts)
 
#add new contact
contacts["manoj"]=8073986666
print(contacts)

#Safe access using get()
print(contacts.get("rahul")) #name that exit
print(contacts.get("imama")) #name that does not exist
contacts={
    "rahul":"9988776655" ,
    "alice":"9897969594" ,
    "bob":"7899301717"
    } #use for loop with items() to print all contacts
for name , phone in contacts.items():
    print(f"contact :{name} | phone:{phone}")
          
#Task2
raw_logs=["ID01","ID02","ID01","ID03","ID04","ID06","ID09","ID03"] #creating a list
unique_users=set(raw_logs) #create a set unique_users
print(unique_users)   
print("ID06" in unique_users) #membernship check
print("ID05" in unique_users)  #is not present
print("Length of original list:", len(raw_logs)) #print the lenth of org list
print("Length of unique set:", len(unique_users)) 
print("Duplicates removed:", len(raw_logs) - len(unique_users))

#Task3
A={"02","03","05","06","08"} #creating two sets
B={"04","03","07","08","09"}
shared_interests = A & B # Common interests
all_interests = A | B # All unique interests
unique_to_a = A - B # Interests only A has
print("Shared interests:", shared_interests)
print("All interests:", all_interests)
print("Unique interests of A:", unique_to_a)
 