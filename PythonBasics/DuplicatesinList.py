mylist = [10, 4, 8, 10, 9, 15, 6, 8, 19, 10]

#print set of duplicates in a list
print(set([x for x in mylist if mylist.count(x) > 1] ))

mylist2=[]
for x in mylist:
    if mylist.count(x) > 1 and x not in mylist2:
        mylist2.append(x)
print(mylist2)


#Remove duplicates in a list
mylist2=[]
for i in mylist:
    if i not in mylist2:
        mylist2.append(i)
print(mylist2)

