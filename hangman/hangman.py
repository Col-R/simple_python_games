from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()



def hangman():
    lives = 6
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # get user input
    while len(word_letters) > 0 and lives != 0: # while length of word letters still exists, iterate
        # letters used
        print (f'{lives} lives left. You have used these letters: ', ' '.join(used_letters))

        # what current word is (W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print ('Current word: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if (user_letter) in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
        
        elif user_letter in used_letters:
            print('You already guessed that letter!')
        
        else:
            print("Please use a valid character")
    # when they guess the word or lose last life
    if lives == 0:
        print(f'Out of lives. Game over. The word was {word}')
    else:
        print(f'Nicely done, you win! The word was {word}')

hangman()