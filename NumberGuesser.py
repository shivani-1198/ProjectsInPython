import random

def GuessGame(top_of_range):
    # isdigit check if the input from the user is number or not
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print("Please give a number greater than 0 next time.")
            quit()
    else:
        print("Please give a number next time.")
        quit()

    random_num = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = raw_input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please give a number next time.")
            continue

        if user_guess == random_num:
            print("You got it!")
            break
        elif user_guess > random_num:
            print("You were above the number!")
        else:
            print("You were below the number!")

    print("You got it in " + str(guesses) + " guesses")



top_of_range = raw_input("Type a number: ")
GuessGame(top_of_range)
