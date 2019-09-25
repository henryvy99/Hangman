import random

# Loop to play again with new word
again = True
while again:

    print("Welcome to the Hangman game!")

    random_file = open("Hangman.txt", "r")
    numLines = len(random_file.readlines()) - 1
    random_file.seek(0)  # resets pointer back to the top of the text file

    # chooses random word from list
    rand_word = random_file.readlines()[random.randint(0, numLines)]
    random_file.close()

    # Creates another array to hide word
    hide_word = ["*"] * (len(rand_word) - 1)
    print("The hidden word has " + str(len(rand_word) - 1) + " letters")
    for i in hide_word:
        print(i, end='')
    print("\n")

    prev_words = ""
    num_guess = 0
    limit = 10
    game = True
    correct = False
    done = False
    while game:
        # Prompts user for a one letter input
        while True:
            guess = input("Enter your letter guess: ")
            if len(guess) == 1:
                if guess not in prev_words and guess not in hide_word:
                    break
                else:
                    print("Letter already used!")
            else:
                print("Please enter ONE letter")

        g = guess.lower()

        # Converts the hidden word with the correct letter guessed
        for i in range(len(rand_word) - 1):
            if g in rand_word[i]:
                hide_word[i] = g
                correct = True

        # Prints out the hidden word
        print("\nSecret Word: ", end='')
        for i in hide_word:
            print(i, end='')
        print()

        if not correct:
            num_guess += 1
            prev_words += g + " "
        correct = False
        print("Previous Words Used: " + prev_words)

        print("Guess number: " + str(num_guess))
        print("Limit number: " + str(limit) + "\n")

        # Checks if they got the hidden word correct
        for i in range(len(hide_word) - 1):
            if "*" not in hide_word:
                done = True

        if done:
            print("You got the hidden word! The word was: " + rand_word)
            game = False

        # limits user of guessing
        if num_guess is limit: # num_guess == limit
            print("You lose!!! You passed your limit!!!")
            print("The correct word was: " + rand_word)
            game = False

    play = input("Would you like to play again? yes or no? ")
    if play.lower() == "no":
        again = False

print("Goodbye! Thanks for playing!")
