"""
Allow user to guess a number between X and Y.
Limit the guesses to a maximum of 5 guesses
Give the user the choice of Easy or Hard game modes
    Easy: give a super easy hint to guess number when they only have 1 guess left
        EX: num = 10, half of this number is 5
    Hard: no hint, instead, output trash talk message such as "You know you only have one guess left, right?" "Woah! You incorrectly guessed X times. That's impressive."
Allow user to play a game then get history of games plays (stats of games played)
After each game, whether user wins or losses, game data is saved to file
"""
import os
import random

MIN_NUM = 1
MAX_NUM = 100
MAX_GUESSES = 5
game_modes = ["easy", "hard"]
selected_game_mode = game_modes[0]

number_to_guess = -1

root_path = "data/"
current_game_file = ""
current_game_path = ""

trash_talk_sentences = ["You know you only have one guess left, right?",
                        "Woah! How many times are you going to guess incorrectly?",
                        "This isn't such a hard game, why are you not succeeding?",
                        "Times is almost up! What are you made of?",
                        ]

def setup_game():
    global number_to_guess, current_game_file, current_game_path
    number_to_guess = random.randint(MIN_NUM, MAX_NUM + 1)

    if not os.path.exists(root_path):
        os.mkdir(root_path)

    all_games = os.listdir(root_path)
    num_games = int(len(all_games))
    num_games += 1
    current_game_file = "game_" + str(num_games) + ".txt"
    current_game_path = root_path + current_game_file

    open(current_game_path, "w").close()

def play_game():
    user_guesses = 0
    has_user_won = False
    guess_history = list()
    while user_guesses < MAX_GUESSES:
        user_guesses += 1

        if selected_game_mode == game_modes[0] and MAX_GUESSES - user_guesses == 0:
            # give user a super easy hint
            print("Half of this number is", number_to_guess / 2)
        elif selected_game_mode == game_modes[1] and MAX_GUESSES - user_guesses == 0:
            print(random.choice(trash_talk_sentences))


        number_user_guessed = int(input(f"Enter a number between {MIN_NUM} & {MAX_NUM}: "))
        guess_history.append(number_user_guessed)

        if number_to_guess == number_user_guessed:
            print("Congrats, you correctly guessed the number")
            has_user_won = True
            break
        print("Sorry but", number_user_guessed, "is NOT the correct number")

        hint = "LOWER or EQUAL" if number_to_guess <= number_user_guessed else "HIGHER"
        print("The number is", hint,"then your guess of", number_user_guessed)


        if MAX_GUESSES - user_guesses > 0:
            print("You have", MAX_GUESSES - user_guesses, "remaining")

    if not has_user_won:
        print("Unfortunately, you didn't guess the correct number")
        print("The correct number was", number_to_guess)

    # save stats here
    content = (f"Game Stats\n\nGame Mode: {selected_game_mode}\nMin Num: {MIN_NUM}\n"
               f"Max Num: {MAX_NUM}\nNumber to Guess: {number_to_guess}\n"
               f"Amount of User Guesses: {user_guesses}\nWon:{has_user_won}"
               f"\n\nUser Guess History:\n\n")

    for guess in guess_history:
        content += str(guess) + "\n"

    with open(current_game_path, "w") as file:
        file.write(content)


def display_stats():
    print("Here are you stats")
    all_games = os.listdir(root_path)
    games_played = len(all_games)

    wins = 0
    for game in all_games:
        wins += open(root_path + game, "r").read().count("True")

    losses = games_played - wins

    print("Global Stats")
    print(f"Games Played: {games_played}\nWins: {wins}\nLosses: {losses}")

    print("Individual Game Stats")

    for game in all_games:
        print(game)
        print(open(root_path + game).read())
        print("\n" * 3)

def main():
    print("Welcome to our guessing game")
    print("Game is starting ........ NOW!")
    setup_game()
    play_game()
    display_stats()


if __name__ == '__main__':
    main()