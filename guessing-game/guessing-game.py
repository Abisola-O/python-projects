import random

random_number = random.randint(1,10)  # numbers 1 - 10
guess = None

while guess != random_number:
	guess = input("Pick a number from 1 to 10: ")
	guess = int(guess)
	if guess < random_number:
		print("TOO LOW! TRY AGAIN.")
	elif guess > random_number:
		print("TOO HIGH! TRY AGAIN.")
	else:
		print("YOU GUESSED CORRECTLY!!!!")

print(random_number)