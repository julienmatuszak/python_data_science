import pandas as pd

data = {"Val1": [1,2,5,3,4],
		"Val2": [1,2,3,4,5],
		"Val3": [7,9,6,2,3]}

df = pd.DataFrame(data)

'''
print(df.sort_values(2, axis = 1))
print(df.sort_values(["Val1"]))
print(df.sort_values(["Val1"], axis = 0))
print(df.sort_values(["Val2"]))
print(df.sort_values(["Val3"]))
'''
df.sort_values(0, axis = 1,
				ascending = False,
				inplace = True,
				kind = "quicksort",
				na_position = "last")

df.sort_index(axis = 1, inplace = True)
print(df)

df.set_value(index = 3, col = "Val2", value = 5)
print(df)

newData = [9,8,7,6,5]
df["Val4"] = newData
print(df)

dataUpdate = {"Val5":[1,9,2,8,3]}
df = df.append([1,9,2,8,3], sort = True)
print(df)
'''
df.sort_values("Val5", axis = 0,
				ascending = False,
				inplace = True,
				kind = "quicksort",
				na_position = "first")
'''
print(df)

df = df.add(2)
print(df)

dfFinal = pd.concat([df,df])
print(dfFinal.reset_index())
