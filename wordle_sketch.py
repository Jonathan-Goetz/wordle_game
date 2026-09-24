import random
import csv

with open('word_lists/valid_guesses.csv', mode='r') as file:
    reader1 = csv.DictReader(file)
    legal_words = []
    for row in reader1:
        legal_words.append(row['word'])

with open('word_lists/valid_solutions.csv', mode='r') as file:
    reader2 = csv.DictReader(file)
    legal_solutions = []
    for row in reader2:
        legal_solutions.append(row['word'])


index = random.randint(0,len(legal_solutions)-1)

solution = legal_solutions[index]

counter = 0

guess = "00000"

correct_letters = ["_"]*5

while guess != solution and counter < 6:
    correct_letters = ["_", "_", "_", "_" ,"_"]
    guess = input("Guess a word with five letters: ").lower()
    if len(guess) != 5:
        print("Your word has the wrong length!")
    elif guess.lower() not in legal_words:
        print("Your word is not in the list!")
    else:
        for i in range(0, len(solution)):
            if guess[i] == solution[i]:
                correct_letters[i] = guess[i].upper()
        for i in range(0, len(solution)):
             if guess[i] != solution[i] and correct_letters.count(guess[i].lower()) + correct_letters.count(guess[i].upper()) < solution.count(guess[i].lower()):
                  correct_letters[i] = guess[i].lower()
        print(correct_letters)
        counter += 1

if guess == solution:
    print("Congratulations, you have guessed the words in " + str(counter) + " tries! The word was: " + solution.upper())
else:
    print("You ran out of guesses. The word was: " + solution.upper())