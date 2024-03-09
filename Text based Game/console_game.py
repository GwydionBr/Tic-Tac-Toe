WINNING_RESULTS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (7, 5, 3), (1, 5, 9)]

STARTING_GAME = (f"   |   |   \n"
                  f"-----------\n"
                  f"   |   |   \n"
                  f"-----------\n"
                  f"   |   |   ")

NUMBERS =  (f" 7 | 8 | 9 \n"
            f"-----------\n"
            f" 4 | 5 | 6 \n"
            f"-----------\n"
            f" 1 | 2 | 3 ")

print("Welcome to Tic Tac Toe.")
print("For your information: To choose your field you have to enter the number of the field.\n"
      "The field is build like a numpad or the interface of a calculator.")
print("To see an example of the field numbers, type (numbers) instead of the number of a field.\n"
      "To exit the game, type (off) instead.")

game_on = True
game_start = True

while game_on:
    if game_start:
        field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        fields_x = []
        fields_o = []
        no_winner = True
        
        starter = input("What sign wants to start? Type (x) or (o).\n")
        if starter == ("x" or "X"):
            player = "X"
            game_start = False
            print(STARTING_GAME)
        elif starter == ("o" or "O" or "0"):
            player = "O"
            game_start = False
            print(STARTING_GAME)
        else:
            print("Invalid input. Please try again!")

    elif not game_start:
        choice = input(f"({player}) Please enter your choice or type (number) to see the field-numbers:")
        try:
            choice = int(choice)
        except ValueError:
            choice = choice.lower()
        finally:

            # if input is a number
            if type(choice) == int:
                # If valid number input
                if choice in possible_numbers:
                    field[choice - 1] = player
                    print(( f" {field[6]} | {field[7]} | {field[8]} \n"
                            f"-----------\n"
                            f" {field[3]} | {field[4]} | {field[5]} \n"
                            f"-----------\n"
                            f" {field[0]} | {field[1]} | {field[2]} \n"))
                    possible_numbers.remove(choice)

                    # Change the Player
                    if player == "X":
                        fields_x.append(choice)
                        player = "O"
                    else:
                        fields_o.append(choice)
                        player = "X"

                #     Check for result
                    for result in WINNING_RESULTS:
                        if result[0] in fields_x and result[1] in fields_x and result[2] in fields_x:
                            print("X is the winner!")
                            restart = input("Enter anything to play a new game or enter (off) to exit the game.")
                            if restart == "off":
                                game_on = False
                            else:
                                game_start = True
                            no_winner = False
                        elif result[0] in fields_o and result[1] in fields_o and result[2] in fields_o:
                            print("O is the winner!")
                            restart = input("Enter anything to play a new game or enter (off) to exit the game.")
                            if restart == "off":
                                game_on = False
                            else:
                                game_start = True
                            no_winner = False

                    if possible_numbers == [] and no_winner:
                        print("It's a Tie! Nobody wins.")
                        restart = input("Enter anything to play a new game or enter (off) to exit the game.")
                        if restart == "off":
                            game_on = False
                        else:
                            game_start = True

                elif choice not in possible_numbers and choice in range(1, 10):
                    print("The chosen field is already used. Try another one.")
                else:
                    print("The number is not a valid field-number. Please try again!")

            # if input is a string
            else:
                if choice == "off":
                    game_on = False
                elif choice == "number":
                    print(NUMBERS)


