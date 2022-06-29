import string
import random

all_symbols = ['!', '@', '#', '$', '%', '^',
               '&', '*', '(', ')', '_' '-', '+', '*']

all_letters = list(string.ascii_letters)
all_digits = list(string.digits)

print("Random Password Generator")

number_of_letters = int(input("How many letters do you want? "))
number_of_digits = int(input("How many digits do you want? "))
number_of_symbols = int(input("How many symbols do you want? "))


generated_password = random.choices(all_letters, k=number_of_letters) + \
    random.choices(all_digits, k=number_of_digits) + \
    random.choices(all_symbols, k=number_of_symbols)

password_strength = input(
    "Do you want an easy password or a hard one ? ").lower()
if password_strength == 'easy':
    print("".join(generated_password))
elif password_strength == 'hard':
    random.shuffle(generated_password)
    print("".join(generated_password))
else:
    print("Invalid input")
