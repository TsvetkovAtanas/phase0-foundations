import random

TOTAL_ATTEMPTS = 7
BOUNDARY = (1, 100)
MIN, MAX = BOUNDARY

def display_rules():
    print("Welcome to Number Guessing Game!\n")
    print(f"I have selected a number between {MIN} and {MAX}.")
    print(f"You have {TOTAL_ATTEMPTS} attempts to guess it.\n")

def generate_random_number():
    return random.randint(MIN, MAX)

def make_guess():
    while True:
        try :
            guess = int(input("Try a number: "))
        except ValueError:
            print(f"Please enter a valid number between {MIN} and {MAX}.\n")
            continue

        if MIN <= guess <= MAX:
            return guess
        else:
            print(f"Please enter a valid number between {MIN} and {MAX}.\n")

def play_game(number):

    for _ in range(TOTAL_ATTEMPTS):
    
        guess = make_guess()

        if guess == number:
            print(":) CONGRATS!!! You guessed it correctly.\n")
            print(f"The number was {number}\n")
            return
        elif guess > number:
            print("Too High! Try again.")
        else:
            print("Too Low! Try again.")

    print(f":( You failed... The number was {number}.\n")




if __name__ == "__main__":
    number = generate_random_number()

    display_rules()

    play_game(number)