str1 = "Hell String World"
str2 = "String operations"
str3 = "String"
str4=" String with space at end "
num = 200

print(str1[0])  # H

print(str2[0:5])  # Sub string extraction 'Strin'

print(str1 + str2)  # String concatenation
print("{}{}".format(str1, num))  # or print(str3 + str(num)) -- String and int contatenation

print(str3 in str2)  # Check if the string is there or not

print(str1.split( )) #string Split using space

print(str4.strip())  #Trimming spaces at begining and end
print(str4.rstrip())
print(str4.lstrip())


