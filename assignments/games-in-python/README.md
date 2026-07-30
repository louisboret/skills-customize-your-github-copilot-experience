
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python that uses string handling, loops, conditionals, and user input to create an interactive word-guessing experience.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the Hangman game logic and select a random word from a predefined list for the player to guess.

#### Requirements
Completed program should:

- Define a list of words and choose one randomly using Python's `random` module.
- Display blanks for each letter in the selected word.
- Keep the chosen word hidden from the player until it is guessed.

### 🛠️ Guess Handling and Game Progress

#### Description
Allow players to guess letters, update the display, and track the number of incorrect attempts.

#### Requirements
Completed program should:

- Accept letter guesses from the player using `input()`.
- Reveal correctly guessed letters in the word display (e.g. `_ a _ g _ a _`).
- Track and display incorrect guesses remaining.
- End when the word is fully guessed or the player has no remaining attempts.
- Show a win message if the player guesses the word and a lose message if they run out of attempts.
