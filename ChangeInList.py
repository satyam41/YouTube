# Write a function change(L) in Python, which accecpts a list L of numbers, the function will replace the even number by half its value and multiply odd number by 3.

def change(L):
    lst = []
    for i in L:
        if (i%2==0):
            lst.append(i/2)
        else:
            lst.append(i*3)
    return lst

newList = [10, 23, 30, 45]
changeInList = change(newList)
print(changeInList)