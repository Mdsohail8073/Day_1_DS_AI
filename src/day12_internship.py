# -*- coding: utf-8 -*-
"""
Created on sat Feb 14 12:30:58 2026

@author: MD SOHAIL
"""
#Task 1
#Create a  scatter_plot.py

import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [49, 53, 59, 72, 78, 89, 94, 97]

# Creating a scatter plot
plt.scatter(study_hours, scores, color='blue', marker='o')

# Labels and title
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Hours vs Exam Scores")

# Show plot
plt.show()

#Task 2
#Creating a dashboard.py

import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (example: monthly sales trend)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
monthly_sales = [200, 250, 300, 350, 400]

# Creating a figure with 1 row and 2 columns
plt.figure(figsize=(10, 5))

# First subplot: Bar chart
plt.subplot(1, 2, 1)
plt.bar(categories, sales, color=['blue', 'green', 'orange'])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Second subplot: Line plot
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales, marker='o', linestyle='-', color='purple')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display plots
plt.show()



