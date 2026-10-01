import random
import csv

# import lists with valid words
with open('word_lists/valid_guesses.csv', mode='r') as file:
    reader1 = csv.DictReader(file)
    legal_words = set()
    for row in reader1:
        legal_words.add(row['word'].lower())

with open('word_lists/valid_solutions.csv', mode='r') as file:
    reader2 = csv.DictReader(file)
    legal_solutions = []
    for row in reader2:
        legal_solutions.append(row['word'].lower())

def play_again():
    answer = 0
    while answer == 0:
            again = input("Would you like to play again? (y/n) ").lower()
            if again in ("y", "n"):
                return again
            print("Please answer with 'y' for yes or 'n' for no!")

def get_guess():
    while True:
        guess = input("Guess a word with five letters: ").lower()
        if len(guess) != 5:
            print("Your word has the wrong length!")
        elif guess.lower() not in legal_words:
            print("Your word is not in the list!")
        else:
            return guess

def check_guess(guess, solution):
    correct_letters = ["_"] * 5
    for i in range(0, len(solution)):
        if guess[i] == solution[i]:
            correct_letters[i] = guess[i].upper()
    for i in range(0, len(solution)):
        if guess[i] != solution[i] and correct_letters.count(guess[i].lower()) + correct_letters.count(guess[i].upper()) < solution.count(guess[i].lower()):
            correct_letters[i] = guess[i].lower()
    return correct_letters

def final_output(guess, solution, counter):
    if guess == solution:
        print("Congratulations, you have guessed the word in " + str(counter) + " tries! The word was: " + solution.upper())
    else:
        print("You ran out of guesses. The word was: " + solution.upper())

# Gameplay
play = "y"

while play == "y":
    solution = random.choice(legal_solutions)
    counter = 0
    guess = ""

    answer = 0

    while guess != solution and counter < 6:
        guess = get_guess()
        counter += 1

        correct_letters = check_guess(guess, solution)
        print(correct_letters)

    final_output(guess, solution, counter)
    play = play_again()
