# Write a function to read two numbers and return their quotient and reminder.

def FindQuotient(x, n):
    quotient = int(x / n)
    reminder = int(x % n)
    return quotient, reminder


print(FindQuotient(12, 5))
