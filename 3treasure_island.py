# height = int(input("What is your height in cm?"))
# bill = 0

# if height >= 120:
#      age = int(input("What is your age?"))
#      print("You can enter the rollercoaster")
#      if age < 12:
#          bill = 5
#          print("Child tickets are 5 USD")
#      elif age <= 18:
#          bill = 7
#          print("Youth tickets are 7 USD")
#      elif age >= 45 and age <= 55:
#          print("Everything is going to be ok. Have a free ride on us!")
#      else:
#          bill = 12
#          print("Adult tickets are $12 USD")

#      wants_photo = input("Do you want a photo taken? Y or N. ")
#      if wants_photo == "Y":
#         bill += 3
        
#         print(f"Your final bill is ${bill}")
# else:
#      print("You cannot enter the rollercoaster")






# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = weight / height**2

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")





# year = int(input())

# if year % 4 ==0:
#     if year % 100 == 0:
#         if year % 400 ==0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")


# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill +=25


# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1


# print(f"Your final bill is: ${bill}.")

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

counting = name1.lower() + name2.lower()
true_words = counting.count('t') + counting.count('r') + counting.count('u') + counting.count('e') 
love_words = counting.count('l') + counting.count('o') + counting.count('v') + counting.count('e')
love_score = int(str(true_words) + str(love_words))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")




