#python number guessing number

import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("--- PYTHON NUMBER GUESSING GAME ---")
print()
print(f"select a number between {lowest_num} and {highest_num}: ")

while is_running:
    guess = input("Enter you guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess< lowest_num or guess > highest_num:
            print("Number is out of Range !!!")
            print(f"Please Select a number between {lowest_num} and {highest_num}: ")
        
        elif guess < answer:
            print("Too low!! try again.")
        elif guess > answer:
            print("Too high!! Try again. ")
        else:
            print(f"Correct!!! The answer is {answer}")
            print(f"Total Guesses: {guesses}")
            is_running = False

    
    else:
        print("Wrong!!!")
        print(f"Please Select a number between {lowest_num} and {highest_num}: ")

