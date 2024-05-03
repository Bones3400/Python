import random

mascotas = ['gato', 'perro', 'loro', 'pez']

word_to_guess = random.choice(mascotas)

guessed_word = ['_'] * len(word_to_guess)

num_guesses = 10

letters_guessed = []

while '_' in guessed_word and num_guesses > 0:
    print(' '.join(guessed_word))
    print('You have', num_guesses, 'guesses left.')

    letter = input('Guess a letter: ').lower()

    if letter in letters_guessed:
        print('You have already guessed that letter.')
    else:

        if letter in word_to_guess:
            for i, c in enumerate(word_to_guess):
                if c == letter:
                    guessed_word[i] = letter
        else:
            num_guesses -= 1

            print('That letter is not in the word.')


if '_' in guessed_word:
    print('Sorry, you ran out of guesses. The word was', word_to_guess)
else:
    print('Congratulations! You guessed the word:', ''.join(guessed_word))