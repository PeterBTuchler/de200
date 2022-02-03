import numpy as np
import random

def run_wordle_once(goal_word, guess_word, scrabble_words):
    assert type(scrabble_words) == list, 'scrabble_words must be a list'
    assert type(goal_word) == str, 'goal_word must be a string'
    assert len(goal_word) == 5, 'goal_word must be length 5'
    assert goal_word in scrabble_words, 'goal_word must be a real word'
    assert type(guess_word) == str, 'guess_word must be a string'
    assert len(guess_word) == 5, 'guess_word must be length 5'
    assert guess_word in scrabble_words, 'guess_word must be a real word'


    goal_word = goal_word.upper()
    guess_word = guess_word.upper()
    empty_1x5 = ["  ", "  ", "  ", "  ", "  "]
    colors = np.array(empty_1x5, dtype='object')
    won = False
    valid_input = False                                 # Checks for valid input (actual 5 letter word)

 
    #                                                   # Counts goal_word letters for yellow condition
    letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,'L': 0,'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,'Y': 0,'Z': 0}                                   
    for char in goal_word:
        char_count = goal_word.count(char)
        letter_count.update({char: char_count})
    for j in range(5):                                  # Subracts for all green matches       
        if guess_word[j] == goal_word[j]:
            letter_count.update({ guess_word[j]: (letter_count[guess_word[j]] - 1) })
 
    for j in range(5):                                  # Assigning colors
        if guess_word[j] == goal_word[j]:
            colors[j] = f"*{guess_word[j]}"             # * means green
        elif letter_count[guess_word[j]] > 0:           
            colors[j] = f".{guess_word[j]}"             # . means yellow
            letter_count.update({ guess_word[j]: (letter_count[guess_word[j]] - 1) })
        else:
            colors[j] = f" {guess_word[j]}"             #   means grey
    return(colors)

