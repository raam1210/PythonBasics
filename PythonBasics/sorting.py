l = [1, 353, 14, 67, 89, 11, 23, 2, 10, 5, 54]

for i in range(0, len(l)):
    for j in range(i + 1, len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]

print(l)
