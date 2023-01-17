#step 1
import random as rd
import hangman_words as words
from hangman_arts import logo, stages
from replit import clean

print(logo)
chosen_word = rd.choice(words.word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
word_lenght = len(chosen_word)
lives = 6

#for letter in chosen_word: or
for letter in range(word_lenght):
    display += "_"
print(display)

end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    #TODO-3 - Check if the letter the user guessed(guess) is one of the letters in the chosen_word.
    if guess in display:
        print(f"You've already guessed {guess}")

    #for letter in chosen_word: or
    for position in range(word_lenght):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n"
        #     f"Current letter: {letter}\n"
        #      f"Guess letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not, in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
    print(f"{' '.join(display)}")

if "_" not in display:
    end_of_game = True
    print("You win!!")

print(stages[lives])