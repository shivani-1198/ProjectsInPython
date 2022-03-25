import random



def GameStart():
    user_wins = 0
    computer_wins = 0

    options = ["rock", "paper", "scissors"]

    while True:
        user_pick = raw_input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_pick == 'q':
            break

        if user_pick not in options:
            print("Wrong input")
            continue


        random_number = random.randint(0,2)
        # rock is 0, paper is 1, scissors is 2
        computer_pick = options[random_number]
        print("Computer picked " + str(computer_pick) + ".")

        if user_pick == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1

        elif user_pick == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1

        elif user_pick == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
        elif user_pick == computer_pick:
            print ("you both chose the same thing so nobody win")

        else:
            print("You lost!")
            computer_wins += 1

    print("You won " + str(user_wins) + " times.")
    print("The computer won " + str(computer_wins) + " times")
    print("Goodbye!")






print ("Welcome to a short game of RockPaperScissors!\n")
GameStart()
