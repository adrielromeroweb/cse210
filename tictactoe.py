def main():
 
    count = 0
    number_list = [1,2,3,4,5,6,7,8,9]
    print()
    grid(number_list[0], number_list[1], number_list[2], number_list[3], number_list[4], number_list[5], number_list[6], number_list[7], number_list[8])
    print()
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")
    print()

    while count < 9:

        player_call = player(count, player1, player2)
        symbol_call = symbol(count)

        answer = int(input(f"{player_call}'s turn to choose a square (1-9): "))
        print()
        
        index = answer - 1
        number_list[index] = symbol_call

        grid(number_list[0], number_list[1], number_list[2], number_list[3], number_list[4], number_list[5], number_list[6], number_list[7], number_list[8])
        print()

        if (number_list[0] == "X" and number_list[1] == "X" and number_list[2] == "X") or \
           (number_list[3] == "X" and number_list[4] == "X" and number_list[5] == "X") or \
           (number_list[6] == "X" and number_list[7] == "X" and number_list[8] == "X") or \
           (number_list[0] == "X" and number_list[3] == "X" and number_list[6] == "X") or \
           (number_list[1] == "X" and number_list[4] == "X" and number_list[7] == "X") or \
           (number_list[2] == "X" and number_list[5] == "X" and number_list[8] == "X") or \
           (number_list[0] == "X" and number_list[4] == "X" and number_list[8] == "X") or \
           (number_list[2] == "X" and number_list[4] == "X" and number_list[6] == "X") or \
           (number_list[0] == "O" and number_list[1] == "O" and number_list[2] == "O") or \
           (number_list[3] == "O" and number_list[4] == "O" and number_list[5] == "O") or \
           (number_list[6] == "O" and number_list[7] == "O" and number_list[8] == "O") or \
           (number_list[0] == "O" and number_list[3] == "O" and number_list[6] == "O") or \
           (number_list[1] == "O" and number_list[4] == "O" and number_list[7] == "O") or \
           (number_list[2] == "O" and number_list[5] == "O" and number_list[8] == "O") or \
           (number_list[0] == "O" and number_list[4] == "O" and number_list[8] == "O") or \
           (number_list[2] == "O" and number_list[4] == "O" and number_list[6] == "O"):

           print(f"{player_call} wins. Thanks for playing!")
           break

        count += 1
        
        if count == 9:
            print("It's a draw!")


def grid(one, two, three, four, five, six, seven, eight, nine):

    print(f"{one}|{two}|{three}")
    print("-+-+-")
    print(f"{four}|{five}|{six}")
    print("-+-+-")
    print(f"{seven}|{eight}|{nine}")


def symbol(count):

    if count % 2 == 0:
        return "X"
    else:
        return "O"


def player(count, X, O):

    if count % 2 == 0:
        return X
    else:
        return O


if __name__ == "__main__":
    main()