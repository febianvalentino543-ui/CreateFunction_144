"""def printme( text1 ): # "This is a print function“
	print(text1)
	return 

printme("I'm first call to user defined function!") 
printme("Again second call to the same function")
printme(0348993884)
printme(87468178)"""


"""def changeme( mylist ): #This changes a passed list#
	mylist.append([1,2,3,4]); 
	print("Values inside the function: ", mylist) 
	return 
mylist = [10,20,30]; 
changeme( mylist ); 

print ("Values outside the function: ", mylist) 
"""



"""def printinfo( name, age ): #Test function 
	print ("Name: ", name); 
	print ("Age: ", age); 
	return; 
printinfo( age = 50, name = "miki" ); 
printinfo( 30, "maka" ); 
printinfo( age = 20, name = "muku" ); 
"""

"""def printinfo( name, age = 35 ): #Test function# 
	print("Name: ", name ) 
	print ("Age ", age ) 
	return; 
printinfo( age=50, name="miki" ); 
printinfo( name="miki" ); 
"""


"""def printinfo( arg1, *vartuple ): #This is test 
	print ("Output is: ") 
	print (arg1)
	for var in vartuple: 
			print (var) 
	return; 
printinfo( 10, 20, 30 )
printinfo( 70, 60, 50 )
"""


"""sum = lambda arg1, arg2: arg1 + arg2;
print ("Value of total : ", sum( 10, 20 )) 
print ("Value of total : ", sum( 20, 20 ) )
"""
