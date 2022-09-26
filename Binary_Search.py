# Binary Search
def Bsearch(x,n):
    beg = 0
    end = len(x)-1
    flag = False
    while (beg<=end):
        mid = int((beg+end)/2)
        if (x[mid]==n):
            flag = True
            break
        elif (n>x[mid]):
            beg = mid+1
        elif (n<x[mid]):
            end = mid-1
    return flag
lst = [1,2,34,2,452,5]
lst.sort()
item = eval(input("Enter what you have to search?..."))
if Bsearch(lst, item):
    print("Data Found")
else:
    print("No Data Found")
