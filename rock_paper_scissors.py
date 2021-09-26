import random

choices = ['rock','paper','scissors']
print('USE ONLY LOWERCASE LETTERS!')
def play(user_choice):
    computer_choice = random.choice(choices)
    print("Computer's choice: " + computer_choice)
    if user_choice == computer_choice:
        return 'Tie!'
    if user_choice == 'rock' and computer_choice == 'scissors' or user_choice == 'scissors' and computer_choice == 'paper' or user_choice == 'paper' and computer_choice == 'rock':
        return 'You won!'
    else:
        return 'You lost!'

print(play(user_choice=input('rock, paper or scissors? ')))
