import random

# Word list
words = ["python", "hangman", "programming", "computer", "github"]

# Choose random word
chosen_word = random.choice(words)
print(f"Word has {len(chosen_word)} letters")

# Create initial placeholder
placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

# Keep track of guessed letters
guessed_letters = []
lives = 6

# Game loop
game_over = False
while not game_over:
    print(f"\nLives remaining: {lives}")
    guess = input("Guess a letter: ").lower()
    
    # Check if already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again!")
        continue
    
    # Add to guessed letters
    guessed_letters.append(guess)
    
    # Create new display
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    
    print(display)
    
    # Check if guess was wrong
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong! '{guess}' is not in the word.")
        
        if lives == 0:
            print(f"\nGame Over! The word was '{chosen_word}'")
            game_over = True
    
    # Check if won
    if "_" not in display:
        print(f"\nCongratulations! You guessed '{chosen_word}' correctly!")
        game_over = True

print("Thanks for playing!")
