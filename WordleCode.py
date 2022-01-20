goal_word = "BINGO"
guess_word = ""
order_words = ["first", "second", "third", "fourth", "fifth", "sixth and final"]
colors = []
for i in range(6):
    print(f"Make your {order_words[i]} guess:")
    guess_word = input()
    guess_word = guess_word.upper()
    print(f"You just guessed {guess_word}")
    if guess_word == goal_word:                         # Checks if you won
        print("Congrats you won!")
        break
    for i in range(5):
