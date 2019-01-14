keyWord = "Hello"

#print(int(keyWord))

try:
	print(int(keyWord))
	#raise NameError("Error")
	#raise ValueError
except ValueError:
	print("got a ValueError")
except Exception as e:
	print("Other type of exception")
	print(str(e))

finally:
	print("finally")

print("Past exception")