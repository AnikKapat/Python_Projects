import random

# List 1: Numbers from 0 to 9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List 2: Letters (lowercase and uppercase)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List 3: Special characters
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':',
          ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{',
          '|', '}', '~']

print("Welcome to Py-Password Generator!")
in_letters=int(input("Enter the number of letters: "))
in_symbols=int(input("Enter the number of symbols: "))
in_numbers=int(input("Enter the number of numbers: "))
#easyone
password1 = ""
for i in range(1, in_letters+1):
    password1+= random.choice(letters)
for j in range(1, in_symbols+1):
    password1+= random.choice(symbols)
for k in range(1, in_numbers+1):
    password1+= random.choice(numbers)

print("The Normie one:", password1)

#hardone
password2 = []
for i in range(1, in_letters+1):
    password2.append(random.choice(letters))
for j in range(1, in_symbols+1):
    password2.append(random.choice(symbols))
for k in range(1, in_numbers+1):
    password2.append(random.choice(numbers))
random.shuffle(password2)  # Shuffles password2 in-place
password3 = ''.join(password2)  # Convert list to string
print("The Gen-Z one:", password3)
