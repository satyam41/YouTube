# Write a program that prompt the user for two strings and checks if the strings is a prefix of the other. Print an appropriate message to inform the user which is the prefix of which or that neither is a prefix. For example, if the user input "evergreen" and "ever", the program would respond: "ever" is a prefix of "evergreen". But if the input was "evergreen" and "green", the program would respond that neither is a prefix of the other.

userInput1 = input("Enter any valid string: ")
userInput2 = input("Enter any valid string: ")
if userInput1.startswith(userInput2[0]):
    print(f"{userInput2} is a prefix of {userInput1}")
else:
    print(f"{userInput1} and {userInput2} neither is a prefix of the other.")
