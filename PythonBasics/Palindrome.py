s = input("Enter a string: ")
revstr = s[::-1]

if revstr == s:
    print("It is a palindrome")
else:
    print("Not a palindrome")