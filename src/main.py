def new_board():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]

def get_char(char):
    if char == "X" or char == "O":
        return char
    else:
        return " "

def render(board):
    print("  0 1 2")
    print("  ------")

    for i in range(3):
        print(f"{i}|{get_char(board[i][0])} {get_char(board[i][1])} {get_char(board[i][2])}|")
    print("  ------")

def get_move():
    print("X: ", end="")
    x = int(input())
    print("Y: ", end="")
    y = int(input())
    return (y, x)

def make_move(board, coords, side):
    if board[coords[0]][coords[1]] == None:
        board[coords[0]][coords[1]] = side
        return True
    else:
        print("This square is not empty, try again.")
    return False

board = new_board()
side = "X"
move_count = 0

while move_count < 9:
    render(board)
    print(f"{side}'s Turn")
    if make_move(board, get_move(), side):
        side = "O" if side == "X" else "X"
        move_count += 1
    print("----------------------------")

render(board)
print("----------------------------")
