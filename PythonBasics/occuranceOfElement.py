mylist = [10, 4, 8, 10, 9, 15, 6, 8, 19, 10]

# Using count method
x = 19
print("{} has occured {} times".format(x, mylist.count(x)))

#Using for loop
count = 0
for ele in mylist:
    if ele == x:
        count = count+1
print("{} has occured {} times".format(x, count))


#using counter method
from collections import Counter
dic = Counter(mylist) # {10:2, 4:1, 8:2, 9:1....}
print("{} has occured {} times".format(x, dic[x]))




