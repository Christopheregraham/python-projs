import random

user_wins = 0
cp_wins = 0
choice = ["rock", 'paper', 'scissors']
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit game: ").lower()
    if user_input == "q":
        break

    if user_input not in choice:
        continue
    random_number = random.randint(0,2)
    # rock = 0, papper = 1, scissors = 2
    cp_chose = choice[random_number]
    print('CP chose ', cp_chose + "!")

    if user_input == 'rock' and cp_chose == 'scissors':
        print('You won!')
        user_wins += 1
    elif user_input == 'scissors' and cp_chose == 'paper':
        print('You won!')
        user_wins += 1
    elif user_input == 'paper' and cp_chose == 'rock':
        print('You won!')
        user_wins += 1
    else:
        print('Yos lost!')
        cp_wins += 1



print("You won", user_wins, " times.")
print("The cp won", cp_wins, " times.")  
print('Goodbye')
