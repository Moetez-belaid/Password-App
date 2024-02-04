import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`!@#$%^&*()_+-={}[]|:;'<>,.?/"
Number = input('Number of Passwords : ')
Number = int(Number)
lenght = input('password lenght : ')
lenght = int(lenght)
 
print('\nPasswords :')

for pwd in range(Number):
	passwords = ''
	for i in range(lenght):
		passwords += random.choice(chars)
	print(passwords)