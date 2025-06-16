import random
import figures
print("Welcome👋, to the Rock, Paper, Scissors Game!🕹️ \n")
print("What Kind Of play🎮 you want to choose? 0️⃣ For Rock, 1️⃣ For Paper, 2️⃣ For Scissors. \n")
user_choice = int(input("Enter your choice (0, 1, or 2): "))
computer_choice = random.randint(0, 2)

print(f"You chose: \n{figures.figures[user_choice]}")
print(f"Computer chose: \n{figures.figures[computer_choice]}")

if user_choice == computer_choice:
    print("It's a tie! 🤝")
elif(user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("Yehhhh 🤩, You win! 🏆")
elif(user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print("Ohh No 🤦‍♂️, You lose! 😢")
else:
    print("Invalid input😡! Please enter 0, 1, or 2. ❌")