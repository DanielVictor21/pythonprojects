import random

def chances(difficulty):
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    
def guessing(number, difficulty):
    lives = chances(difficulty)
    print(f"You have {lives} attempts remaining to guess the number")
    while lives > 0:
        attempt = int(input("Make a guess: "))
        if attempt == number:
            print(f"You got it! The answer was {number}.")
            return  # Saia da função se o usuário acertar
        elif attempt > number:
            lives -= 1
            print("Too high.\nGuess again.")
        else:
            lives -= 1
            print("Too Low.\nGuess again.")
        print(f"You have {lives} attempts remaining to guess the number")
    
    # Se chegou aqui, significa que o usuário ficou sem vidas
    print(f"Sorry, you're out of attempts. The correct answer was {number}.")
            
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100\n")
difficulty = input("choose a difficulty. Type 'easy' or 'hard' ")
number = random.randint(1, 100)
guessing(number, difficulty)