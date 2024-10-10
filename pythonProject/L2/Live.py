def welcome():
    name = input("Hi! what's your name?\n")    # \n at the end so the input will be on a different line
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def load_game():
    game_key = input("Please choose a game to play:")  # To avoid writing a very long line here with 3 \n's - I'll split
    print("Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("Guess Game - guess a number and see if you chose like the computer")
    print("Currency Roulette - try and guess the value of a random amount of USD in ILS")

    if game_key == 1: pass  # memo
    elif game_key == 2: pass  # guess
    elif game_key == 3: pass  # currency


# the inner procedures go here
def memory_game():
    pass


def guess_game():
    pass


def currency_game():
    pass


welcome()
load_game()

