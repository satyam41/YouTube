# Write a program that inputs a main string and then creates an encrypted string by embedding a short symbol based string after each character. The program should also be able to produce the decrypted string from encrypted string.

import random

num = random.random()

def encrypt(sttr, enkey=str(num)):
    return enkey.join(sttr)

def decrypt(sttr, enkey):
    return sttr.split(enkey)

mainString = input("Enter any string: ")
enStr = encrypt(mainString)
deLst = decrypt(mainString, str(num))
deStr = "".join(deLst)
print("The encrypted string is:", enStr)
print("The decrypt string is:", deStr)

