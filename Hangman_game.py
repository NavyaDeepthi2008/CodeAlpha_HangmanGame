import random

# Predefined words
words = ["python", "apple", "coding", "laptop", "google"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Display hidden word
display_word = ["_"] * len(word)

print("🎮 Welcome to Hangman Game!")

while wrong_guesses < max_wrong and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        # Reveal letters
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Final Result
if "_" not in display_word:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n You lost! The word was:", word)
