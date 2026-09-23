import random


def explain_rules():
    print("Wellcome to the WORD GUESSING GAME")
    print("Try to guess the word or its letters")
    print("The word is: ")
    print("_"*len(random_word), end="\n\n")


def display_word(final_word, random_word, guess):
    for index, char in enumerate(random_word):
        if guess == char:
            final_word[index] = char

    print("".join(final_word))


def play_game():
    remaining_attemts = total_attepts
    guess = input("Guess a letter: ").lower()
    for _ in range(total_attepts):

        if guess == random_word or "".join(final_word) == random_word:
            print("CONGRATS!!! You guessed correctly!\n")
            print(f"The word is {random_word}")
            return

        remaining_attemts -= 1
        print(f"You have {remaining_attemts} attempts remaining.")   

        display_word(final_word, random_word, guess)

        guess = input("Guess a letter: ").lower()

    print("You failed misserably. I'm not mad... I'm dissapointed...\n")
    print(f"The word was {random_word}.")     


if __name__ == "__main__":
    words = ('Banana', 'Chair', 'Marketing', 'Volleyball', 'Cup', 'Foundations', 'Python')
    random_word = random.choice(words).lower()
    total_attepts = len(random_word) * 2
    final_word = list("_"*len(random_word))

    explain_rules()
    play_game()