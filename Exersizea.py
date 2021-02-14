
import random
list = ["Rock", "Paper", "Scissors"]

def randlist(list):
    use = random.choice(list)
    return use

def play():
    use = randlist(list)
    user_play = (input("Please Enter your play: R, P, S"))
    user_play= user_play.upper()
    if user_play == "R":
        user_play = "Rock"
    if user_play == "P":
        user_play = "Paper"
    if user_play == "S":
        user_play = "Scissors"
    print(use)

    if user_play == use:
        print("Snap you got the same: "+user_play, " + ", use)
    elif user_play == "Rock" and use == "Scissors":
        print("You win, Smash the rock beat the scissors")
    elif user_play == "Paper" and use == "Rock":
        print("You win, Squeeze, The paper wrapped the rock")
    elif user_play == "Scissors" and use == "Paper":
        print("You win, The scissors cut the paper")
    elif user_play == "Rock" and use == "Paper":
        print("You lose, Your Rock got Wrapped by the paper")
    elif user_play == "Scissors" and use == "Rock":
        print("You lose, Your scissors got smashed by the rock")
    elif user_play == "Paper" and use == "Scissors":
        print("You lose, Your paper got cut by the scissors")


def main():
    play()


while True:
    main()