# Python3 code to convert tuple 
# into string 
def convertTuple(tup): 
	str = ''.join(tup) 
	return str

# Driver code 
tuple = ('g', 'e', 'e', 'k', 's') 
str = convertTuple(tuple) 
print(str) 


# Python3 code to demonstrate working of
# Convert Tuple to integer
# Using reduce() + lambda
import functools

# initialize tuple
test_tuple = (1, 4, 5)

str_tuple = str(test_tuple)

# printing original tuple
print("The original tuple : " + str_tuple)

# Convert Tuple to integer
# Using reduce() + lambda
res = functools.reduce(lambda sub, ele: sub * 10 + ele, str_tuple)

# printing result
print("Tuple to integer conversion : " + res)

