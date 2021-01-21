import random
import hangman_art as ha
import hangman_words as hw
import os

def clear(): 
    os.system('cls') #on Windows System

chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
already_guessed_msg = False
congrats = False

#hangman logo
print(ha.logo)

#testing code
print(f'\nPssst, the solution is {chosen_word}.\n')

#create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        already_guessed_msg = True

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            congrats = True

    clear()
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")

    if already_guessed_msg == True:
        print(f"You already have guessed {guess}. Guess again! \n")
        already_guessed_msg = False

    if congrats == True:
        print(f"Well done. {guess} is one of the letters in the secret word\n")
        congrats = False

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
  
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(ha.stages[lives])
