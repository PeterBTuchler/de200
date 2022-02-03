import numpy as np
import random
from single_instance_wordle import run_wordle_once

goal_word = "GREAT"                                                # Define the Goal word (don't worry, the algorithm doesn't "peak")

scrabble_words = open("scrabble_words.txt", "r+")
scrabble_words = scrabble_words.read().strip(' ').split(',')            # All English Words

len5words = [] 
for word in scrabble_words:                                             # Stores all english 5 letter words
    if len(word) == 5:
        len5words.append(word)

#FOR TESTING-----
len5words = ['GRUEL', 'SPUDS', 'GREAT', 'FLING', 'SNARE', 'TINGE', 'TOAST', 'SMILE', 'RUSTY', "PLOTT", 'REFER', 'RELAY']
#----------------

for guess_num in range(6):
    print(f"There are {len(len5words)} viable words remaining")             # FOR TESTING
    letter_prob = np.zeros((5,26), dtype=float)                             # This np 2d array will store the probability of each letter in each location
    for word in len5words:                                                  # Loops through each word
        for i in range(len(word)):                                          # Loops through each letter in the word
            letter_prob[i,ord(word[i]) - 65] += 1                           # Fills letter prob using ascii values
    letter_prob = letter_prob / len(len5words)

    best_word = ""                                                          # This part of the code finds the most probable word
    best_word_score = 0
    for word in len5words:                                                  # Loops through each word
        word_score = 0
        for i in range(len(word)):                                          # Loops through each letter in the word
            word_score += letter_prob[i,ord(word[i]) - 65]                  # Sum probability of each letter to get an overall score of the word
        print(f"The word score of {word} is {word_score}")
        if word_score > best_word_score and len(set(word)) == len(word):    # Makes sure the guess does not repeat letters (MAKE SURE THIS IS NOT ALWAYS ON!!!!!!)
            best_word = word
            best_word_score = word_score

    wordle_feedback = run_wordle_once(goal_word, best_word, scrabble_words) # Makes guess and recieves feedback Ex. output:  [' C' '.A' '.R' '.E' ' S']
    print(wordle_feedback)

    # Determine if the guess won
    won = True
    for letter in wordle_feedback:
        if letter[0] != '*':
            won = False

    if won:
        print("--- Congrats you won! ---")
        break
    # len5words.remove(best_word)                                           # Remove the guess from len5words if it is not the winning word
    # Remove invalid words from len5words
    for letter_index in range(5):
        color_code = wordle_feedback[letter_index][0]
        letter = wordle_feedback[letter_index][1]
        for word in len5words:
            if color_code == ' ' and letter in word:                # Removes words with grey letters
                len5words.remove(word)
                print(f"{word}: GREY!")
            if color_code == '.' and letter not in word:      #ERROR HERE      # Removes words without yellow letter in the word
                len5words.remove(word)
                print(f"{word}: YELLOW!")
            if color_code == '*' and letter != word[letter_index]:  # Removes words without green perfect match
                len5words.remove(word)
                print(f"{word}: GREEN!")
    

    # For debugging------
    print(len5words)
    #--------------------

# for whatever reason, it does not successfully check and remove all words. For instance, after guessing GATER and knowing that the
# final word starts with G and has A T E R somewhere in it, it still keeps ARENA, AVERS, CARET, etc. It seems to only check A,R,E for some reason
                 