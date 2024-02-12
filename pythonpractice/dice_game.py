import random

def roll():
    roll_value = random.randint(1,6)
    return roll_value
def set_score():
    max_score = input("What would you like to play to? (100 recommended): ")
    if max_score.isdigit():
        max_score = int(max_score)
        if 0 < max_score <= 400:
            print("Game is starting now...")
            return max_score
        else:
            "Here we go! Good luck!"
            return max_score
    else:
        print("Not a valid score. try again!")
        set_score()

while True:
    get_players = input("How many players? (2-4): ")
    if get_players.isdigit():
        get_players = int(get_players)
        if 2 <= get_players <= 4:
            max_score = set_score()
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Not a valid input. Try again.")

player_scores = [0 for _ in range(get_players)]


while max(player_scores) < max_score:
    for player_idx in range(len(player_scores)):
        current_turn = 0
        print("\nPlayer: ",player_idx+1,"\nCurrent Score: ",player_scores[player_idx])
        while True:
            roll_status = input("Would you like to roll? (y): ")
            if roll_status.lower() != 'y':
                player_scores[player_idx] = player_scores[player_idx]+current_turn
                break
            roll_value = roll()
            if roll_value == 1:
                print("You rolled a one! Turn over")
                current_turn = 0
                break
            else:
                current_turn = current_turn + roll_value
                print("You rolled a",roll_value,"...You are currently at",current_turn,"for this turn.")
                print("If you stopped now, you would be at",player_scores[player_idx]+current_turn)
                

            


print(player_scores)
