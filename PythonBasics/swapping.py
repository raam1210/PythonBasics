a = int(input("Enter A value: "))
b = int(input("Enter B value: "))

#Using 3rd variable
print("Before Swapping: A is", a, "and B is", b)
temp = a
a = b
b = temp
print("After Swapping: A is", a, "and B is", b)
print ("---------------------------------------------")

#Without using 3rd variable
print("Before Swapping: A is", a, "and B is", b)
a = a + b
b = a - b
a = a - b
print("After Swapping: A is", a, "and B is", b)

