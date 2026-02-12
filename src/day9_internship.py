# Task-1
#Goal: Practice creating a Series with custom labels and accessing specific data.
#Scenario: You are managing a small electronics store.

# Importing pandas
import pandas as pd

# Creating a Pandas Series named products
products =pd.Series([700, 150, 300],index=['Laptop', 'Mouse', 'Keyboard'])

# Printing the panda series
print( products )

# Accessing the price of 'Laptop'
print("The price of the device is", products ['Laptop'])

# Slice the Series to show the first two products using positional indexing.
print( products.iloc[0:2])

# Task-2
# Goal: Use boolean masking to filter data and handle incomplete records.
# Scenario: You have a list of student exam scores, but some students missed the test.


# Importing pandas
import pandas as pd

#Creating a Series named grades
grades=pd.Series( [85, None, 92, 45, None, 78, 55])

#Printing the original list
print(grades)

#Identifing which values are missing using.isnull().
null_values=grades.isnull()
print("viewing null values",null_values)

#Fill the missing values with a default score of O using .fillna().
filled_series=grades.fillna(0)
print("viewing missing values",filled_series)

#Applying a boolean mask to filter 
filtered_result=grades[grades<60]
print("viewing after filtering values",filtered_result)

# Task-3
#Goal: Process text data efficiently using the .str accessor.

#Scenario: A list of usernames was collected with inconsistent casing and extra spaces

# Importing pandas
import pandas as pd

#Create a Series named usernames
usernames=pd.Series( [' Alice', 'bOB', 'Charlie_Data ', 'daisy'])

# Removing leading/trailing whitespace (.strip())
remove=usernames.str.strip()

# Converting all names to lowercase (.lower()).
low=usernames.str.lower()

# Checking which names contain the letter 'a' (.contains()).
contains=low.str.contains('a')

#displaying Cleaned Series
print("Cleaned Series",remove)

#displaying boolean result
print("The boolean result of the 'a' search.",contains)