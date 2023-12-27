# 11. Write a python program that randomly generates a 5 digit number. The user has a
# maximum of 5 tries to guess the randomly generated number.
import random

def guess_number():
   random_number = str(random.randint(10000, 99999))
   for attempt in range(1, 6):
       guess = input(f"Attempt {attempt}: Enter a 5-digit number: ")

       # Validate the guess
       while not guess.isdigit() or len(guess) != 5:
           guess = input("Invalid input. Please enter a 5-digit number: ")
       clues = ""
       for i in range(5):
           if guess[i] == random_number[i]:
               clues += "C"  # Correct digit and position
           elif guess[i] in random_number:
               clues += "B"  # Correct digit, wrong position
           else:
               clues += "A"  # Wrong digit

       print(clues)

       if clues == "CCCCC":
           print("Congratulations! You guessed the number correctly!")
           return

   print("You ran out of attempts. The number was", random_number)

guess_number()
