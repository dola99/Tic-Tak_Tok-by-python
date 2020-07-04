def start():
    print("""---------
|       |
|       |
|       |
---------""")


game = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
i = 0


def x_wins():
    if game[0] == "X" and game[1] == "X" and game[2] == "X":
        return True
    elif game[3] == "X" and game[4] == "X" and game[5] == "X":
        return True
    if game[6] == "X" and game[7] == "X" and game[8] == "X":
        return True
    if game[0] == "X" and game[3] == "X" and game[6] == "X":
        return True
    if game[1] == "X" and game[4] == "X" and game[7] == "X":
        return True
    if game[2] == "X" and game[5] == "X" and game[8] == "X":
        return True
    if game[0] == "X" and game[4] == "X" and game[8] == "X":
        return True
    if game[2] == "X" and game[4] == "X" and game[6] == "X":
        return True


def o_wins():
    if game[0] == "O" and game[1] == "O" and game[2] == "O":
        return True
    if game[3] == "O" and game[4] == "O" and game[5] == "O":
        return True
    if game[6] == "O" and game[7] == "O" and game[8] == "O":
        return True
    if game[0] == "O" and game[3] == "O" and game[6] == "O":
        return True
    if game[1] == "O" and game[4] == "O" and game[7] == "O":
        return True
    if game[2] == "O" and game[5] == "O" and game[8] == "O":
        return True
    if game[0] == "O" and game[4] == "O" and game[8] == "O":
        return True
    if game[2] == "O" and game[4] == "O" and game[6] == "O":
        return True




def your_turn():
    global i
    while i <= 10:
        if x_wins():
            print("X wins")
            break
        if o_wins():
            print("O wins")
            break
        if i == 9:
            print("Draw")
            break
        print("Enter the coordinates:")
        first, second = input().split()
        if i % 2 == 0:
            a = "X"
        else:
            a = "O"
        try:
            if 1 <= int(first) <= 3 and 1 <= int(second) <= 3:
                pass
            else:
                print("Coordinates should be from 1 to 3 !")
            if first == "1" and second == "3":
                if game[0] == " ":
                    game[0] = a
                    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")
                    i += 1
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif first == "2" and second == "3":
                if game[1] == " ":
                    game[1] = a
                    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")
                    i += 1
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif first == "3" and second == "3":
                if game[2] == " ":
                    game[2] = a
                    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")
                    i += 1
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif first == "1" and second == "2":
                if game[3] == " ":
                    game[3] = a
                    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")
                    i += 1
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif first == "2" and second == "2":
                if game[4] == " ":
                    game[4] = a
                    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")
                    i += 1
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif first == "3" and second == "2":
                if game[5] == " ":
                    game[5] = a
                    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")
                    i += 1
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif first == "1" and second == "1":
                if game[6] == " ":
                    game[6] = a
                    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")
                    i += 1
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif first == "2" and second == "1":
                if game[7] == " ":
                    game[7] = a
                    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")
                    i += 1
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif first == "3" and second == "1":
                if game[8] == " ":
                    game[8] = a
                    print(f"""---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------""")
                    i += 1
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
                    continue

        except ValueError as ve:
            print("you should enter numbers!")


start()
your_turn()
