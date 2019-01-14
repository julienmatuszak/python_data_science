import pandas as pd
import numpy as np 

df = pd.read_csv("outbreaks.csv", index_col = False)
print(df.head())

print(df.columns)

print(df.isnull().sum())

print(df["State"])

print(df.describe())
print()
print(df["State"].value_counts())
print()
print(df["Location"].value_counts())
print()
print(df["Food"].value_counts())
print()
print(df["Fatalities"].value_counts())

fatalityDF = df.loc[df["Fatalities"] > 0]
print(fatalityDF.head())
print()
print(fatalityDF["Location"].value_counts())
'''
fatalityDF.hist(column = "Year",
				bins = len(fatalityDF["Year"].unique()))
fatalityDF.hist(column = "Hospitalizations",
				by = "Month",
                figsize = (15, 10),
                bins = 30)
'''
print()
stateWise = df.loc[df["State"] == "California"]
print(stateWise["Food"].value_counts())
print()
locationWise = df.loc[df["Location"] == "Restaurant"]
print(locationWise["State"].value_counts())
print()
hospWise = df.loc[df["Hospitalizations"] > 0]
print(hospWise["Food"].value_counts())