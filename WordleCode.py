import numpy as np
import random

words = open("words.txt", "r+")
words = words.read().strip(' ').split(',')

scrabble_words = open("scrabble_words.txt", "r+")
scrabble_words = scrabble_words.read().strip(' ').split(',')

goal_word = random.choice(words)
goal_word = goal_word.upper()
guess_word = ""
order_words = ["first", "second", "third", "fourth", "fifth", "sixth and final"]
empty_6x5 = [["  ", "  ", "  ", "  ", "  "], 
["  ", "  ", "  ", "  ", "  "], 
["  ", "  ", "  ", "  ", "  "], 
["  ", "  ", "  ", "  ", "  "], 
["  ", "  ", "  ", "  ", "  "], 
["  ", "  ", "  ", "  ", "  "]]
colors = np.array(empty_6x5, dtype='object')
won = False

print(goal_word)

print("----------------------------------------------------------")             # Makes it look nice
print("                    New Game of Wordle                    ")
print("----------------------------------------------------------")

for i in range(6):
    print(colors)
    print(f"Make your {order_words[i]} guess:")
 
    valid_input = False                                # Checks for valid input (actual 5 letter word)
    while valid_input == False:
        guess_word = input()
        guess_word = guess_word.upper()
        if len(guess_word) == 5 and f"{guess_word}" in scrabble_words:
            valid_input = True
        else:
            print("Guess must be an actual 5 letter word")
 
    #                                                   # Counts goal_word letters for yellow condition
    letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,'L': 0,'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,'Y': 0,'Z': 0}                                   
    for char in goal_word:
        char_count = goal_word.count(char)
        letter_count.update({char: char_count})
    for j in range(5):                                  # Subractss for all green matches       
        if guess_word[j] == goal_word[j]:
            letter_count.update({ guess_word[j]: (letter_count[guess_word[j]] - 1) })
 
    for j in range(5):                                  # Assigning colors
        if guess_word[j] == goal_word[j]:
            colors[i,j] = f"*{guess_word[j]}"           # * means green
        elif letter_count[guess_word[j]] > 0:           
            colors[i,j] = f".{guess_word[j]}"           # . means yellow
            letter_count.update({ guess_word[j]: (letter_count[guess_word[j]] - 1) })
        else:
            colors[i,j] = f" {guess_word[j]}"           #   means grey
 
 
    if guess_word == goal_word:                         # Checks if you won
        print(colors)
        print("--- Congrats you won! ---")
        won = True
        break
 
if won == False:
    print(colors)
    print(f"--- You lose. The answer is {goal_word} ---")

