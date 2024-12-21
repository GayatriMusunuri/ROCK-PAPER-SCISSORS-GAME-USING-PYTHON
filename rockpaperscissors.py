#importing Random Module
import random 

# Instructions for winning the game
print('Winning rules of the game ROCK PAPER SCISSORS are:'
       "\n a) Rock vs Paper ---> Paper wins "
       "\n b) Rock vs Scissors ---> Rock wins "
       "\n c) Paper vs Scissors ---> Scissors wins "
       "\n")

while True:

    print("choices to enter:"
    "\n 1 - Rock"
    "\n 2 - Paper"
    "\n 3 - Scissors"
    "\n")

    # Ask the user to provide the input
    choice = int(input("Enter your choice: "))

    # Looping until user enters the valid input
    while choice > 3 or choice < 1:
        choice = int(input('Please, Try To Enter a valid choice : '))

    # Assign the value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Printing  the  user choice
    print(f"User chooses :{choice_name}")
    print("\n Now it's Computer's Turn...")

    # Computer chooses randomly any number among 1, 2, and 3
    comp_choice = random.randint(1, 3)

    # Initialize value of comp_choice_name variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer chooses:", comp_choice_name)
    
    print(f"\n {choice_name}, 'vs', {comp_choice_name}")

    # Finding the winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Scissors'

    # Print the result
    if result == "DRAW":
        print("<== It was a  TIE ! ==>")
    elif result == choice_name:
        print("<== User WINS! ==>")
    else:
        print("<== Computer WINS! ==>")

    # Ask  the user if he/she wants to play again
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break


print("Thanks for playing!")