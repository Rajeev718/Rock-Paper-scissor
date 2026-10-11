
print("------------ Rock-Paper-Scissor Game -----------")
import random

options = {1: "Rock", 2: "Paper", 3: "Scissor"}


wins_against = {
    "Rock": "Scissor",
    "Paper": "Rock",
    "Scissor": "Paper",
}

while True:
    print("\n1. Rock\n2. Paper\n3. Scissor\n4. Exit")

    try:
        choice = int(input("Choose any option: "))
    except ValueError:
        print("Please enter a number (1-4).")
        continue

    if choice == 4:
        print("Thanks for playing!")
        break

    if choice not in options:
        print("Please enter a valid choice.")
        continue

    user = options[choice]
    computer = random.choice(list(options.values()))

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("Tie")
    elif wins_against[user] == computer:
        print("You win")
    else:
        print("You lost")  
