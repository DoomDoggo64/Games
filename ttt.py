board=[]
colomn=[]
for i in range(3):
    row = []
    for i in range(3):    
        colomn = [i]
        row.append(colomn)
    board.append(row)
print(board)
print(board[0])
print(board[0][1])
def display_board(board):
    print("+-------+"*3)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.
