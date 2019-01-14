import pandas as pd
import numpy as np

data = {"Part 1": [1,2,3,4,1,10],
		"Part 4": [1,2,3,4,1,2],
		"Part 2": [5,4,3,2,4,10],
		"Part 3": [1,9,2,8,1,10],
		"Nan part": [4,3,np.nan,1,4,3]}

newIndex = ["A", "B", "C", "D", "E", "F"]

df = pd.DataFrame(data, index = newIndex)

print(df)

'''
print("Getting value:",df.get_value("A", "Part 2"))
'''
for index, series in df.iterrows():
	if int(series["Part 1"]) == int(1):
		df.drop(index, axis = 0, inplace = True)

print("After iteration:\n", df)
'''
print(df.isnull())
print(df.notnull())

df.dropna(1, thresh = 5, inplace = True)
print(df


df.drop_duplicates(subset = ["Nan part", "Part 4"], keep = "last", inplace = False)

df.drop(["A", "C", "D"], axis = 0, inplace = True)
print(df)
'''