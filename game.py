import random

count_snake = count_water = count_gun = 0

def updtae_count(user_input):
    global count_water, count_gun, count_snake
    if user_input == 's':
        count_snake += 1
    elif user_input == 'w':
        count_water += 1
    elif user_input == 'g':
        count_gun += 1

def predict():
    if count_snake > count_water and count_snake > count_gun:
        pred = 's'
    elif count_water > count_snake and count_water > count_gun:
        pred = 'w'
    elif count_gun > count_snake and count_gun > count_water:
        pred = 'g'
    else:
        pred = random.choice(['s', 'w', 'g'])
    return pred

player_score = computer_score = 0

def update_score(user_input):
    global player_score, computer_score
    pred = predict()
    if user_input == 's':
        if pred == 's':
            print("You played Snake, Computer played Snake.")
            print(f"Player Score {player_score} \nComputer Score {computer_score}")
        elif pred == 'w':
            print("You played Snake, Computer played Water.")
            player_score += 1
            print(f"Player Score {player_score} \nComputer Score {computer_score}")
        elif pred == 'g':
            print("You played Snake, Computer played Gun.")
            computer_score += 1
            print(f"Player Score {player_score} \nComputer Score {computer_score}")
    elif user_input == 'w':
        if pred == 's':
            print("You played Water, Computer played Snake.")
            computer_score += 1
            print(f"Player Score {player_score} \nComputer Score {computer_score}")
        elif pred == 'w':
            print("You played Water, Computer played Water.")
            print(f"Player Score {player_score} \nComputer Score {computer_score}")
        elif pred == 'g':
            print("You played Water, Computer played Gun.")
            player_score += 1
            print(f"Player Score {player_score} \nComputer Score {computer_score}")
    elif user_input == 'g':
        if pred == 's':
            print("You played Gun, Computer played Snake.")
            player_score += 1
            print(f"Player Score {player_score} \nComputer Score {computer_score}")
        elif pred == 'w':
            print("You played Gun, Computer played Water.")
            computer_score += 1
            print(f"Player Score {player_score} \nComputer Score {computer_score}")
        elif pred == 'g':
            print("You played Gun, Computer played Gun.")
            print(f"Player Score {player_score} \nComputer Score {computer_score}")

valid_entries = ['s', 'w', 'g']
while True:
    pred = predict()
    user_input = input("Enter 's' for Snake, 'w' for Water and 'g' for Gun: ")
    while user_input not in valid_entries:
        print("Invalid Input!!!")
        user_input = input("Enter 's' for Snake, 'w' for Water and 'g' for Gun: ")

    updtae_count(user_input)
    update_score(user_input)

    if computer_score == 10:
        print("Computer Won!")
        break
    elif player_score == 10:
        print("You Won!")
        break