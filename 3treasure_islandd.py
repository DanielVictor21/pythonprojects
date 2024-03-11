print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if direction == 'left':
    decision = input("Swim or wait? ").lower()
    if decision == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?")
        door = input().lower()
        if door == 'yellow':
            print("You Win!")
        else:
            print("Eaten by beasts. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else: 
    print("Fall into a hole. Game Over.")