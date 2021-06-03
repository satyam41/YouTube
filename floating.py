# Write a program to read a floating point number n. Print n, n^2, n^3, n^4 and n^5

def floatingNumber(n):
    i = 1
    while i <= 5:
        print(n ** i)
        i += 1


floatingNumber(2)
