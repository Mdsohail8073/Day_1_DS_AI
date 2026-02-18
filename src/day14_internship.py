#Task 1
import pandas as pd

# Create sample dataset
df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})

print(df)
#lable encoding 
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

print(df)

#one hot encoding 
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print(df)

#Task 2
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures,OneHotEncoder
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

d={
      "Age":[35,26,43,39,32,19,25],
      "Salary":[30000,40000,25000,65000,35000,33000,27000]
      }


d2=pd.DataFrame(d)

sns.histplot(x=d2["Age"],kde=True)
plt.title("Age Histogram")
plt.show()
scaler= StandardScaler()
scaled_features=scaler.fit_transform(d2[['Age','Salary']])


scaler=MinMaxScaler()
d2[['Age','Salary']]=scaler.fit_transform(d2[['Age','Salary']])
print("AGE AND SALARY\n")
print(d2)

#Task 3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures,OneHotEncoder
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("gdp.csv")
X_train,X_test,y_train,y_test = train_test_split(df[['Year']],df[['Value']],test_size=0.2,random_state=42)


model=LinearRegression()
model.fit(X_train,y_train)
baseline_pred=model.predict(X_test)
baseline_score=r2_score(y_test, baseline_pred)

print(baseline_score)


poly=PolynomialFeatures(degree=2,include_bias=False)

X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.transform(X_test)

poly_model=LinearRegression()
poly_model.fit(X_train_poly,y_train)
poly_pred=poly_model.predict(X_test_poly)
poly_score=r2_score(y_test, poly_pred)
print(poly_score)