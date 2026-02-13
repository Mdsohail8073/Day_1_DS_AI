import matplotlib.pyplot as plt
#using the plot function
a=[1,2,3,4,5]
b=[2,4,6,8,10]
plt.plot(a,b)
plt.show() #for output


a=[1,2,3,4,5]
b=[2,4,6,8,10]
plt.scatter(a,b)
plt.show() #for output


#using the bar function
names=["rahul","bob","alice"]
marks=[46,49,51]
plt.bar(names,marks)
plt.show() #for output
print("cryptography and network security")

import matplotlib.pyplot as plt
plt.subplot(1, 3, 1)
plt.plot([1,2,3], [1,4,9])
plt.title("Line Plot")

plt.subplot(1, 3, 2)
plt.bar(['A','B','C'], [3,7,5])
plt.title("Bar Chart")
plt.show()

plt.subplot(1, 3, 3)
a=[1,2,3,4,5]
b=[0.5,1.5,2.5,3.5,4.5]
plt.scatter(a,b)
plt.title("scatter plot")
plt.show()




#Task1
import matplotlib.pyplot as plt

# Define the data
months = [1, 2, 3, 4, 5]
revenue = [1000, 3000, 6000, 7500, 9000]

# Create the line plot
plt.plot(months, revenue)

# Add title and labels
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")

# Show the plot
plt.show()








 

