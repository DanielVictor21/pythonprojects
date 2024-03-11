import random

types = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
 

escolhas = ["Rock", "Paper", "Scissors"]
user_choice = escolhas[types]
print(user_choice)
computer_choice = random.choice(escolhas)
print(computer_choice)


if types < 0 or types > len(escolhas):
    print("Escolha invalida")
elif user_choice == computer_choice:
        print("empate")   
elif user_choice == "Rock" and computer_choice == "Paper":
        print("Computer Won!")    
elif user_choice == "Rock" and computer_choice == "Scissors":
        print("User Won!")
elif user_choice == "Paper" and computer_choice == "Rock":
        print("User Won!")
elif user_choice == "Paper" and computer_choice == "Scissors":
        print("Computer Won!")
elif user_choice == "Scissors" and computer_choice == "Rock":
        print("Computer Won!")
elif user_choice == "Scissors" and computer_choice == "Paper":
        print("User Won!")
   
    



