import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator!")

number_of_letters = int(input("How many letters would you like? \n"))
number_of_numbers = int(input("How many numbers would you like? \n"))
number_of_symbols = int(input("How many symbols would you like? \n"))

password_list = []

for char in range (0, number_of_letters):
    password_list.append(random.choice(letters))

for char in range (0, number_of_numbers):
    password_list.append(random.choice(numbers))

for char in range (0, number_of_symbols):
    password_list.append(random.choice(symbols))

#Make it more strong
random.shuffle(password_list)

password = ""

for i in password_list:
    password = password + i

print(f"Your password is: {password}")