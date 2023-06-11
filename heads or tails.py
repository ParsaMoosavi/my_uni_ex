import random

possible_actions = ["shir", "khat"]

while True:
    computer_answer = random.choice(possible_actions)
    my_answer=input("please Enter your chance (shir / khat )")

    if my_answer==computer_answer:
        print("you win! ")

    

    else:
        print("you lose :( ")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
