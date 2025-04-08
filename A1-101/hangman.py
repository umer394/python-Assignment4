from words import words
import random
import string
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or  " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    print("Welcome to Hangman!")
    print(f"You have {lives} lives. Good luck!")
    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("\nGuess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Letter {user_letter} is not in the word. You have {lives} lives left.")
        elif user_letter in used_letters:
            print("You already guessed that letter. Try again.")
        else:
            print("Invalid character. Please try again.")
    if lives == 0:
        print("You died! The word was ", word)
    else:
        print("You guessed the word " ,word,"!!")
hangman()

