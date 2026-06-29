import random

words = ["python", "java", "apple", "tiger", "computer"]
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")

while incorrect_guesses < max_attempts:
    display = ""
    for letter in word:
        display += letter + " " if letter in guessed_letters else "_ "

    print("\nWord:", display)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("Already guessed.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess! Remaining:", max_attempts - incorrect_guesses)

if incorrect_guesses == max_attempts:
    print("Game Over! Word was:", word)
