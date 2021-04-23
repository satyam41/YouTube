#Program to print area and perimeter of the circle
radius = float(input("Enter value of radius"))
print("1.Area")
print("2.Perimeter")
choice = int(input("Enter your choice(1 or 2) :"))
if choice == 1:
    area = 3.14*radius*radius
    print("Area of the circle is", area)
else:
    perm = 2*3.14*radius
    print("Perimeter of the circle is", perm)
