# Write a function in python reverse(x) which accepts a list x of numbers and display elements in reverse order such that each displayed element is twice of the original element of list x.

def reverse(x):
    x.reverse()
    double = []
    for i in x:
        double.append(i*2)
    return double

lst = [1,2,3,4,5]
print(reverse(lst))