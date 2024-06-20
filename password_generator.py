import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword Generator!")
use_letter=int(input(f"How many letters would you like in your password?\n"))
use_symbol=int(input(f"How many symbols would you like?\n"))
use_numbers=int(input(f"How many numbers would you like?\n"))

password=[]
for char in range(1,use_letter+1 ):
  password.append(random.choice(letters))

for char in range(1,use_symbol+1 ):
  password += random.choice(symbols)

for char in range(1,use_numbers+1 ):
  password += random.choice(numbers)

random.shuffle(password)
final_pass=""
for char in password:
  final_pass += char
print(final_pass)