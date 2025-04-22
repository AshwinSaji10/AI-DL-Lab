##### Globals #####

# Starting the game with X
XO = 'X'

# Initialize the grid/board
grid = [[None, None, None],
        [None, None, None],
        [None, None, None]]

winner = None
running = True
won = False


def evaluate_move():
    '''
    Evaluate each move in the grid
    '''
    global grid

    for row in range(0, len(grid)):
        if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2]:

            if grid[row][0] == 'X':
                return 10
            elif grid[row][0] == 'O':
                return -10

    for col in range(0, len(grid)):
        if grid[0][col] == grid[1][col] and grid[1][col] == grid[2][col]:

            if grid[0][col] == 'X':
                return 10
            elif grid[0][col] == 'O':
                return -10

    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:

        if grid[0][0] == 'X':
            return 10
        elif grid[0][0] == 'O':
            return -10

    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:

        if grid[0][2] == 'X':
            return 10
        elif grid[0][2] == 'O':
            return -10

    return 0


def are_moves_left():
    '''
    Check if any moves are left
    '''
    global grid

    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] is None:
                return True

    return False


def minimax(depth, player_type):
    '''
    Run the Mini-Max algorithm
    '''
    global grid

    score = evaluate_move()

    if score == 10:
        return score

    if score == -10:
        return score

    if not are_moves_left():
        return 0

    if player_type:
        best_val = -10_000
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] is None:
                    grid[i][j] = XO
                    value = minimax(depth + 1, not player_type)
                    best_val = max(best_val, value)
                    grid[i][j] = None

    else:
        best_val = 10_000
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] is None:
                    grid[i][j] = XO
                    value = minimax(depth + 1, not player_type)
                    best_val = min(best_val, value)
                    grid[i][j] = None

    return best_val


def get_best_move(Piece):
    '''
    Get the best possible move for X/O
    '''
    best_move_val = -10_000
    x = 0
    y = 0

    if Piece == 'X':
        is_max = True
    else:
        is_max = False

    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] is None:
                grid[i][j] = XO
                value = minimax(0, is_max)
                grid[i][j] = None

                if best_move_val < value:
                    x = i
                    y = j
                    best_move_val = value
    return x, y


def print_board():
    '''
    Print the current state of the board
    '''
    global grid
    print("\n")
    for row in grid:
        print(" | ".join([cell if cell is not None else " " for cell in row]))
        print("-" * 10)


def draw_status():
    '''
    Print the current status of the game
    '''
    global XO, winner

    if winner is None:
        print(f"{XO}'s turn. AI is thinking...")
    else:
        print(f"{winner} won!")


def change():
    '''
    Switch between X and O
    '''
    global XO

    if XO == 'X':
        XO = 'O'
    else:
        XO = 'X'


def check_if_won():
    '''
    Check if X/O has won
    '''
    global grid, winner, won

    for row in range(0, 3):
        if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] is not None:
            winner = grid[row][0]
            won = True
            break

    for col in range(0, 3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] is not None:
            winner = grid[0][col]
            won = True
            break

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] is not None:
        winner = grid[0][0]
        won = True

    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] is not None:
        winner = grid[0][2]
        won = True


def player_move():
    '''
    Allow the player to make a move
    '''
    while True:
        try:
            row, col = map(int, input(f"Enter your move ({XO}): ").split())
            if grid[row][col] is None:
                grid[row][col] = XO
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as two integers between 0 and 2.")


if __name__ == '__main__':
    '''
    Main function
    '''

    print("Welcome to Tic-Tac-Toe AI!")
    print_board()

    while running:
        check_if_won()
        
        if not won:
            if XO == 'X':
                player_move()  # Player's turn
            else:
                print(f"AI ({XO}) is thinking...")
                x, y = get_best_move(XO)  # AI's turn
                grid[x][y] = XO

            draw_status()
            print_board()
            change()

        else:
            print(f"{winner} won!")
            running = False
