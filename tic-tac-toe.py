
board = [" " for _ in range(9)]


def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def check_draw():
    return " " not in board


def play_game():
    current_player = "X"

    for turn in range(9):
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
            if board[move] != " ":
                print("Position already taken! Try again.")
                continue
            board[move] = current_player
        except:
            print("Invalid input! Try again.")
            continue

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            return

        if check_draw():
            print_board()
            print("It's a draw!")
            return

        current_player = "O" if current_player == "X" else "X"


play_game()
