from def_num import play_game

while True:
    selection = input("""Hello, What would you like to do?
    A) Play a new game
    B) Exit
    """)

    if selection.upper() == "A":
        play_game()
    else:
        print("Leaving the Game......")
        break