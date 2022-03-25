def QuizGame(playing):
    if playing.lower() != "yes":
    	print("See you next time!:wq")
        quit()

    print("Okay! Let's play")
    print("There ar 5 questions in this quiz. Best of Luck!")
    score = 0

    answer = raw_input("What is 11 * 11? ")
    if answer == "121":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = raw_input("What is the square root of 64? ")
    if answer == "8":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = raw_input("What is the value of pi ")
    if answer == "3.14":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = raw_input("How many sides a quadrilateral has? ")
    if answer == "4":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = raw_input("If 6 is 50% of a number, what is the number? ")
    if answer == "12":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("You got " + str(score) + " questions correct")
    print("You got " + str(int(score / 5) * 100) + "%.")


print("Welcome to my math quiz!")

playing = raw_input("Do you want to play? ")
QuizGame(playing)
