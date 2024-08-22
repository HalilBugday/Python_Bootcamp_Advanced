import random
from hagman_words import word_list
import hangman_art

lives = 6
print(hangman_art.logo)


chosen_word = random.choice(word_list)
#print(chosen_word)

place_holder = ""
chosen_word_length = len(chosen_word)
for position in range(chosen_word_length):
    place_holder += "_"
print(place_holder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed that letter: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"Game over! The word was {chosen_word}.")


    if "_" not in display:
        game_over = True
        print("You win!")

    print(hangman_art.stages[lives])
