import datetime
import random


def play_game():
    player = input("What is your name?: ")
    secret = random.randint(1, 30)
    attempts = 0

    while True:
        class Results:
            def __init__(self, score, player_name, date):
                self.score = score
                self.player_name = player_name
                self.date = date

        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:

            new_player = Results(score=attempts, player_name=player, date=str(datetime.datetime.now()))

            with open("result.txt", "a") as result_file:
                result_file.write(str(new_player.__dict__))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Player's data: {0}".format(new_player.__dict__))

            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")