import pandas as pd

df = pd.read_csv("outbreaks.csv", 
				#delim_whitespace = False,
				#sep = ",",
				#header = 0,
				#names = ,
				usecols = ["Year", "Month", 
						   "Hospitalizations"],
				index_col = None,
				#decimal = ".",
				#nrows = 200,
				#na_values = ["February"]
				#skip_blank_lines = True
				)
#print(df)

#print(df.head(10))

#df.to_csv("test.csv")

#f = open("test.csv", "w")

'''
with open("test.csv", "w") as f:
	df.to_csv(f, sep = ";", na_rep = "nothing",
				float_format = "%5.3f",
				header = True,
				#index = False,
				index_label = "count",
				mode = "a")
'''

#print()
#f.close()

print(df.head(10))
print(df.tail())
print("Number of rows of data: ", len(df))
print()
print("Number of missing data:\n" + str(df.isnull().
									sum()))
print()
print("Number of missing data points,",
	  "for individual column:\n" + 
	  str(df.isnull()["Hospitalizations"].sum()))


print(df.describe())
df = df.dropna()
print(len(df))

df = df.sort_values("Hospitalizations",
					ascending = False)

print("Printing new head:\n", df.head(10))
print()
print("Hospitalizations > 0\n")
#print(df["Hospitalizations"] > 0)
df2 = df[df.Hospitalizations > 0]
print(len(df2))

print()
print(df["Year"].value_counts())
print("Counting occurrences df2:\n" + str(df2["Year"].
									  value_counts()))
print("Length of df2:\n" + str(len(df2)))
print()
yearlyData = df2.loc[df2["Year"] == 2006]
print(yearlyData)
print(yearlyData["Year"].value_counts())
print()
months = df2["Month"].unique()
print()
print("Monthly occurrences for df:\n" +
	  str(df["Month"].value_counts()))
print()
print("Monthly occurrences for df2:\n" +
	  str(df2["Month"].value_counts()))
print()
years = df2["Year"].unique()
years.sort()
print(years)

'''
for year in years:
	currentYearData = df2.loc[df2["Year"] == year]
	print()
	print(year)
	print(currentYearData["Month"].value_counts())
'''

print()
print(df2.describe(percentiles = [0.2, 0.4, 0.6,
								  0.8, 0.9, 0.95]))
df2.hist()

