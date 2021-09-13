# Write a program to print absolute value of a number. Absolute value of a number is:

# number --> if number is positive
# 0 number --> if number is zero
# - number --> if number is negative

num = int(input("Enter any valid integer number: "))

if num > 0:
    print("Number is Positive")

elif num == 0:
    print("Number is Zero")

elif num < 0:
    print("Number is Negative")

else:
    print("Please, enter valid integer number.")
