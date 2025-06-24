#len(12345) # len doesnot like working with integers

print(len("12345"))


print(type("hello")) # Type os used to find the what is the data type
print(type(123))
print(type(32.5))
print(type(True))

#type conversion
print(len(str(12345))) # type conversion
print(str(123))
print(int("6")+ int("7"))
print(float(123))

length = len(input("Enter your name"))
print("Number of letters in your name: " + str(length))

print("Number of letters in your name: " + str(len(input("Enter your name"))))