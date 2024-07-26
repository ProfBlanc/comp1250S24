"""
This is a guessing game.
The user will have 3 or  guesses to guess a number
We will allow 2 game modes: easy and hard
for easy, user has 5 guesses; hard, user has 3 guesses

Once user only has 1 more guess left, the program will generate
half the number is {value}

The game will store data. User will get a summary of stats at the end
of the game
"""
import csv
import os.path, random

app_root_dir = "data/"
user_root_dir = ""
games_modes = "easy hard".split(" ")
selected_game_mode = games_modes[0]
MIN_NUM = 1
MAX_NUM = 100
map_mode_to_num_guesses = {"easy": 5, "hard": 3}
NUM_GUESSES = map_mode_to_num_guesses[selected_game_mode]

number_to_guess = 0

def init():
    # ensure that a data exists
    if not os.path.exists(app_root_dir):
        os.mkdir(app_root_dir)

def ask(question:str)->str:
    return input(question)


def setup():
    global user_root_dir, selected_game_mode, NUM_GUESSES, number_to_guess
    # ask user for username
    uname = ask("What is your username?")
        # create a sub-direct for username in data if not found
    user_root_dir = app_root_dir + uname
    if not os.path.exists(user_root_dir):
        os.mkdir(user_root_dir)
    # ask user for game mode (easy or hard)
    game_mode = ask("Enter a game mode: " + ", ".join(games_modes)).lower()
    if game_mode in games_modes:
        selected_game_mode = games_modes[games_modes.index(game_mode)]
        NUM_GUESSES = map_mode_to_num_guesses[game_mode]

    number_to_guess = random.randint(MIN_NUM, MAX_NUM)

def run():
    history_of_guesses = list()
    num_user_guesses = 0
    result = "loss"
    for turn in range(1, NUM_GUESSES+1):
        num_user_guesses += 1
        num = int(input(f"Guess # {turn} of {NUM_GUESSES}!\n"
              f"Enter a number between {MIN_NUM} and {MAX_NUM}: "))
        history_of_guesses.append(str(num))
        if number_to_guess == num:
            print("Congratulations! You guessed the number!")
            result ="won"
            break
        else:
            direction = "higher" if num < number_to_guess else "lower"
            print("Sorry, but", num, "is incorrect. The number "
                                     "to guess is", direction)

            if turn == NUM_GUESSES - 1:
                print("Here is a super helpful hint. "
                      "Half of the number is ", number_to_guess / 2)

    game_files = os.listdir(user_root_dir)
    new_game_file = "game_" + str(len(game_files) + 1) + ".csv"
    with open(user_root_dir + "/" + new_game_file, "w") as file:

        fieldnames = "Username-Game Mode-Number to Guess"\
                      "-Number of Guesses"\
                      "-Result-History".split("-")
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        data = {fieldnames[0]: user_root_dir.split(app_root_dir)[1],
                fieldnames[1]: selected_game_mode,
                fieldnames[2]: str(number_to_guess),
                fieldnames[3] : str(num_user_guesses),
                fieldnames[4] : result,
                fieldnames[5]: ",".join(history_of_guesses)
                }
        writer.writerow(data)

def main():
    init()
    print("Welcome to our guessing game")
    setup()
    run()

if __name__ == '__main__':
    main()

