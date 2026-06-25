#HangMan Game in Python

import random

words = ("apple","banana","orange","coconut","pineapple","grapes","mango","kiwi", "blueberry", "watermelon", "avacado", "guava")

#dictionary of key: ()

hangman_art = {0:("     ",
                  "     ",
                  "     "),
               1:("  o  ",
                  "     ",
                  "     "),
               2:("  o  ",
                  "  |  ",
                  "     "),
               3:("  o  ",
                  " /|  ",
                  "     "),
               4:("  o  ",
                  " /|\ ",
                  "     "),
               5:("  o  ",
                  " /|\  ",
                  " /   "),
               6:("  o  ",
                  " /|\  ",
                  " / \  ")}

def display_man(wrong_guesses):
    print("--------------------------")
    for line in hangman_art [wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = ["_"]* len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running == True:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input ("Enter a letter:").lower()

        if guess in answer:
            for index in range(len(answer)):
               if answer[i] == guess:
                 hint[i] = guess

if __name__ == "__main__":
    main()
