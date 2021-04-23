# Sort list with the help of bubble sort.

lst = [5, 3, 4, 2, 1]
for i in range(0, len(lst)):
    for j in range(0, len(lst) - (i + 1)):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)