# Write a short program that asks for your height in centimeters and then converts your height to feet and inches. (1foot = 12inches, 1inch = 2.54cm)

height = int(input("Enter your height in cm: "))
print(f"Your height is {height}cm.")
heightInInch = height/2.54
print(f"Your height is {heightInInch}inch.")
heightInFoot = heightInInch/12
print(f"Your height is {heightInFoot}foot.")
