# Basic data type in Python: Numbers. Strings, Booleans, Sequences, Dictionaries

myint = 5
myflot = 13.2
mystr = "This is string"
mybool = True
mylist = [0,1,"two",3.2,False]
mytuple = (0,1,2)
mydict = {"one": 1,"two":2}


print(myint)
print(myflot)
print(mystr)
print(mybool)
print(myint)
print(mytuple)
print(mydict)

# re-declare a variable works
mystr = "abc"
print(mystr)


# to access a memeber of a sequence type , use []
print(mylist[1])
print(mytuple[1])



#  use slice to get parts to reverse a sequence

print(mylist[1:5:2])
print(mylist[1:5])

# you can use slices to reverse a sequence

print(mylist[::-1])

# dictionaries are accessed via keys

print(mydict["one"])

#Error : variables of different types cannot be combined
print("string type" + str(123))

# Global vs. local variables in functions


def someFunction():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)

del mystr
print(mystr)