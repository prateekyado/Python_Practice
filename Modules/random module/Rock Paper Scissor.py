#Programming  Rock Paper and Scissor Game in python
import random

options=("rock", "paper", "scissors")
#computer=random.choice(options)
#print(computer)


is_running=True

while True:

    computer=random.choice(options)
#    print(computer)
    player = input("Enter rock, paper or scissors: ")
    if player not in options:
        print("Wrong!!!")
        player = input("Enter again rock, paper or scissors: ")
    
    if player=="rock" and computer=="scissors":
        print("YOU WIN!!!")
    elif player=="paper" and computer=="rock":
        print("YOU WIN!!!")
    elif player=="scissors" and computer=="paper":
        print("YOU WIN!!!")
    elif player==computer:
        print("It's a Tie")
    else:
        print("YOU lose!!!")
        print(f"It's {computer}")

    yes = input("Do you want to continue the game (y to continue): ").lower()
    if yes != "y":
        break
