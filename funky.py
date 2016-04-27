def funky (a,b):
	'''concanate data types'''
	# if type (a) and type (b) == str:
	# 	print (a+b)
	# elif type(a) and type(b) == int or type(a) and type (b) == float:
	# 	return sum
	if type(a) == str and type(b) == str:
		print (a + b)
	elif (type(a) == int or type(a) == float) or (type(b) == int or type(b) == float):
		print (a+b)
	elif type(a) == list and type(b) == list:
		print (a+b)
	elif type(a) == dict and type(b) == dict:
		return (a,b)
	else:
		print "None"


funky([10,20],[1.5,6])
funky(1,2.4)
funky("Euster", "japheth")
funky({"name": 20, "age": 39}, {"height": 68})



# test code
