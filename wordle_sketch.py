import random

words = ["apple", "adieu", "plane", "sight", "minty", "slack"]

index = random.randint(0,len(words)-1)

solution = words[index].upper()

counter = 0

guess = "00000"

while guess != solution and counter < 6:
    guess = input("Guess a word with five letters: ").upper()
    if len(guess) != 5:
        print("Your word has the wrong length!")
    else:
        for i in range(0, len(solution)):
            if guess[i] == solution[i]:
                print(2)
            elif guess[i] in solution:
                print(1)
            else:
                print(0)
        counter += 1

if guess == solution:
    print("Congratulations, you hve guessed the words in " + str(counter) + " tries! The word was: " + solution)
else:
    print("You ran out of guesses.")