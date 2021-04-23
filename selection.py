# Sort the list with the help of selection sort.

lst = [6,1,5,4,8,10]
print("Original list: ",lst)
for i in range(0,len(lst)):
    small = lst[i]
    for j in range(i, len(lst)):
        if lst[j]<=small:
            small = lst[j]
            pos = j
    lst[pos] = lst[i]
    lst[i] = small
print("Sorted list: ",lst)