# Twisted pig latin. Prompt the user to enter a single word. Then form a new word by taking the first letter of the original word, moving it to the end, and adding "ay". Thus "school" becomes "choolsay".

userInput = input("Enter any string: ")
newWord = userInput.replace(userInput[0], userInput[len(userInput)-1])
newWord = newWord.removeprefix(newWord[0])
newWord = newWord + userInput[0] + "ay"
print(newWord)
