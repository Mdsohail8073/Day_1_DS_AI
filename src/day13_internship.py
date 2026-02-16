#calling head() on dataframe 
import pandas as pd 
data={
      "age":[20,21,23,34,45,41,35,24,28],
      "salary":[30000,40000,35000,42000,36000,41000,38000,28000,25000],
      "experience":[1,2,3,4,5,10,7,8,9],
      "department":["it","hr","finance","it","hr","finance","it","hr","finance"],
      "gender":["m","f","m","f","f","m","m","f","f"]
      }
df=pd.DataFrame(data)
df.head(5)

#calling tail() on dataframe
import pandas as pd
data={
      "age":[20,21,23,34,45,41,35,24,28],
      "salary":[30000,40000,35000,42000,36000,41000,38000,28000,25000],
      "experience":[1,2,3,4,5,10,7,8,9],
      "department":["it","hr","finance","it","hr","finance","it","hr","finance"],
      "gender":["m","f","m","f","f","m","m","f","f"]
      }
df=pd.DataFrame(data)
df.tail(5)

#calling info() on dataframe
import pandas as pd
data={
      "age":[20,21,23,34,45,41,35,24,28],
      "salary":[30000,40000,35000,42000,36000,41000,38000,28000,25000],
      "experience":[1,2,3,4,5,10,7,8,9],
      "department":["it","hr","finance","it","hr","finance","it","hr","finance"],
      "gender":["m","f","m","f","f","m","m","f","f"]
      }
df=pd.DataFrame(data)
df.info(5)

#calling describe() on dataframe
import pandas as pd
data={
      "age":[20,21,23,34,45,41,35,24,28],
      "salary":[30000,40000,35000,42000,36000,41000,38000,28000,25000],
      "experience":[1,2,3,4,5,10,7,8,9],
      "department":["it","hr","finance","it","hr","finance","it","hr","finance"],
      "gender":["m","f","m","f","f","m","m","f","f"]
      }
df=pd.DataFrame(data)
df.describe()

#calculating df.mean() on dataframe 
import pandas as pd
data={
      "age":[20,21,23,34,45,41,35,24,28],
      "salary":[30000,40000,35000,42000,36000,41000,38000,28000,25000],
      "experience":[1,2,3,4,5,10,7,8,9],
      "department":["it","hr","finance","it","hr","finance","it","hr","finance"],
      "gender":["m","f","m","f","f","m","m","f","f"]
      }
df.mean(numeric_only=True)

#caculating df.median() on dataframe
    import pandas as pd
data={
      "age":[20,21,23,34,45,41,35,24,28],
      "salary":[30000,40000,35000,42000,36000,41000,38000,28000,25000],
      "experience":[1,2,3,4,5,10,7,8,9],
      "department":["it","hr","finance","it","hr","finance","it","hr","finance"],
      "gender":["m","f","m","f","f","m","m","f","f"]
      }
df.median(numeric_only=True)

#calculating df.max() on dataframe
import pandas as pd
data={
      "age":[20,21,23,34,45,41,35,24,28],
      "salary":[30000,40000,35000,42000,36000,41000,38000,28000,25000],
      "experience":[1,2,3,4,5,10,7,8,9],
      "department":["it","hr","finance","it","hr","finance","it","hr","finance"],
      "gender":["m","f","m","f","f","m","m","f","f"]
      }
df.max(numeric_only=True)

#differentiating salary per experiance
import pandas as pd
data={
      "age":[20,21,23,34,45,41,35,24,28],
      "salary":[30000,40000,35000,42000,36000,41000,38000,28000,25000],
      "experience":[1,2,3,4,5,10,7,8,9],
      "department":["it","hr","finance","it","hr","finance","it","hr","finance"],
      "gender":["m","f","m","f","f","m","m","f","f"]
      }
df["salary_per_experience"] = df["salary"] / df["experience"]
df[["experience", "salary", "salary_per_experience"]]

#graph comparison between Salary and Experience using a scatter plot 
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "age": [20, 21, 23, 34, 45, 41, 35, 24, 28],
    "salary": [30000, 40000, 35000, 42000, 36000, 41000, 38000, 28000, 25000],
    "experience": [1, 2, 3, 4, 5, 10, 7, 8, 9],
    "department": ["it", "hr", "finance", "it", "hr", "finance", "it", "hr", "finance"],
    "gender": ["m", "f", "m", "f", "f", "m", "m", "f", "f"]
}

df = pd.DataFrame(data)

# Scatter plot: Salary vs Experience
plt.figure()
plt.scatter(df["experience"], df["salary"])
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Comparison between Salary and Experience")
plt.show()

#Task 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example dataset
data = {
    "Price": [2500000, 3000000, 2800000, 4500000, 6000000,
              3200000, 2900000, 10000000, 12000000],
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai",
             "Delhi", "Chennai", "Mumbai", "Mumbai"]
}

df = pd.DataFrame(data)

# Histogram with KDE
plt.figure()
sns.histplot(df["Price"], kde=True)
plt.xlabel("House Price")
plt.ylabel("Frequency")
plt.title("Distribution of House Prices")
plt.show()

#Calculating Skewness & Kurtosis
skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("Skewness:", skewness)
print("Kurtosis:", kurtosis)

#creating a count plot
plt.figure()
sns.countplot(x="City", data=df)
plt.xlabel("City")
plt.ylabel("Number of Houses")
plt.title("Number of Houses by City")
plt.show()

#Task 2
# for Creating a scatter plot (squarefootage vs price)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
data = {
    "SquareFootage": [600, 800, 1000, 1200, 1500, 1800, 2200, 2500],
    "Price": [2000000, 2600000, 3200000, 3800000,
              4800000, 5600000, 7000000, 8200000],
    "City": ["Delhi", "Delhi", "Bangalore", "Bangalore",
             "Mumbai", "Mumbai", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

#creating a Scatter Plot
plt.figure()
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.xlabel("Square Footage")
plt.ylabel("House Price")
plt.title("Square Footage vs House Price")
plt.show()

#creating a boxplot (City vs Price)
plt.figure()
sns.boxplot(x="City", y="Price", data=df)
plt.xlabel("City")
plt.ylabel("House Price")
plt.title("House Prices by City")
plt.show()

#Task 3
#Correlation Matrix + Heatmap
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Price": [2000000, 2600000, 3200000, 3800000, 4800000, 5600000, 7000000],
    "SquareFootage": [600, 800, 1000, 1200, 1500, 1800, 2200],
    "Bedrooms": [1, 2, 2, 3, 3, 4, 4],
    "Bathrooms": [1, 1, 2, 2, 3, 3, 4]
}

df = pd.DataFrame(data)

#creating a Correlation matrix
corr_matrix = df.corr()

# Heatmap
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()

#Using Boxplot to Identify Outliers
plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of House Prices")
plt.ylabel("Price")
plt.show()















