def change(L):
    lst = []
    for i in L:
        if (i%2==0):
            lst.append(i/2)
        else:
            lst.append(i*3)
    return lst

lst = [10,23,20,45]
print("Original List: ",lst)
changeInList = change(lst)
print("Change in the list: ",changeInList)