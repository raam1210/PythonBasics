def Fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibo(n - 1) + Fibo(n - 2)


n = int(input("Enter any number: "))
for i in range(0, n):
    print(Fibo(i))
