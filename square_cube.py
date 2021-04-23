#Program to print when a number is even calculate its square otherwise calculate cube.
num = int(input("Eneter any number :"))
if num%2 == 0:
    result = num*num
    print("This number is even and its square is", result)
else:
    result = num*num*num
    print("This number is odd and its cube is", result)