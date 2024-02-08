import random

a = 0
b = 0
count = 0

while a == 0:
	print("Welcom to the gusseing game the range of the guess is from 0 to 10\n")
	y = random.randint(1, 10)
	x = int(input("Enter your choice: "))

	while x != y:
		if x == y:
			print("You've Won !!\n")
			print("you have taken total of " + str(count) + "  steps to win!\n")
			break

		if x > y:
			print("guess lower !!\n")
			count += 1
			x = int(input("Enter your choice: "))
			print("\n")

		if x < y:
			print("guess higher !!\n")
			count += 1
			x = int(input("Enter your choice: "))
			print("\n")

	if x == y:
		print("You've Won !!\n")
		print("you have taken total of " + str(count) + " steps to win!\n")

	print("Want to continue playing the game ? press 0 for yes or 1 for no\n")
	a = int(input(""))
