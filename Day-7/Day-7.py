# Yay it's Day - 0️⃣7️⃣ Today I made Hangman game🤪

import random
import hangman_art
import hangman_words
from replit import clear


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(hangman_art.logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guess_ls = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()
    

    if guess in display:
      print("you have already guessed that letter")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

        

    #Check if user is wrong.
    if guess not in chosen_word:
 
        print(f"{guess} is not present in the given word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(hangman_art.stages[lives])
