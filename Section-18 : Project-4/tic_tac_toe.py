import random


def init_player():
    player_name = input('Enter your name : ')
    player_symbol = ''
    while player_symbol not in ['X', 'O']:
        player_symbol = input('Enter player symbol (X/O) : ').upper()
        if player_symbol not in ['X', 'O']:
            print('Invalid user input.')
    return {
        'name': player_name,
        'symbol': player_symbol
    }


def new_board():
    return [' '] * 9


def display_board(board):
    print('\t-----------')
    print(f'\t {board[0]} | {board[1]} | {board[2]} ')
    print(f'\t {board[3]} | {board[4]} | {board[5]} ')
    print(f'\t {board[6]} | {board[7]} | {board[8]} ')
    print('\t-----------')


def player_move(board, pos, player):
    if not is_board_full(board):
        if board[pos - 1] == ' ':
            board[pos - 1] = player['symbol']
        else:
            print(f'Position: {pos} is already taken...')
    else:
        check_winner(board, player['symbol'])


def is_board_full(board):
    return not board.__contains__(' ')


def check_winner(board, symbol):
    if (board[0] == symbol and board[1] == symbol and board[2] == symbol) or (
            board[3] == symbol and board[4] == symbol and board[5] == symbol) or (
            board[6] == symbol and board[7] == symbol and board[8] == symbol) or (
            board[0] == symbol and board[3] == symbol and board[6] == symbol) or (
            board[1] == symbol and board[4] == symbol and board[7] == symbol) or (
            board[2] == symbol and board[5] == symbol and board[8] == symbol) or (
            board[0] == symbol and board[4] == symbol and board[8] == symbol) or (
            board[2] == symbol and board[4] == symbol and board[6] == symbol):
        return True
    return False


def ai_move(board, player_symbol):
    symbols = ['X', 'O']
    symbols.remove(player_symbol)
    ai_symbol = symbols[0]

    # first check if ai can win in next move
    # assuming than 1 entry can make him win
    for i in range(9):
        # create a board copy to make temporary changes
        board_c = board.copy()
        if board_c[i] == ' ':
            board_c[i] = ai_symbol
            if check_winner(board_c, ai_symbol):
                # finalize the move
                board[i] = ai_symbol
                return

                # check if opponent can win on the next move
    # if yes then block their move
    for i in range(9):
        # create a board copy to make temporary changes
        board_c = board.copy()
        if board_c[i] == ' ':
            board_c[i] = player_symbol
            if check_winner(board_c, player_symbol):
                # finalize the move
                board[i] = ai_symbol
                return

    # try to get one of the corners if empty
    corner_index = [0, 2, 6, 8]
    available_corner = []
    for i in corner_index:
        if board[i] == ' ':
            available_corner.append(i)
    if available_corner:
        index = random.choice(available_corner)
        board[index] = ai_symbol
        return

    # try to get mid
    if board[4] == ' ':
        board[4] = ai_symbol
        return

    edges = [1, 3, 5, 7]
    available_edges = []
    for i in edges:
        if board[i] == ' ':
            available_edges.append(i)
    if available_edges:
        index = random.choice(available_edges)
        board[index] = ai_symbol


def continue_playing():
    choice = input('Press \'y\' to continue playing : ').lower()
    if choice == 'y':
        return True
    return False


if __name__ == '__main__':
    board = new_board()
    player = init_player()

    while True:
        display_board(board)
        playing = True
        while playing:
            pos = 0
            try:
                pos = int(input('Enter Position (1-9) : '))
                if not 9 >= pos >= 1:
                    raise AttributeError
            except TypeError:
                print('Invalid User input.')
                continue
            except AttributeError:
                print('Invalid input range.')
                continue
            player_move(board, pos, player)
            if not is_board_full(board):
                ai_move(board, player['symbol'])
            display_board(board)
            if check_winner(board, player['symbol']):
                playing = False
                print(f'----------- {player["name"]} WON! -----------')
            else:
                if player['symbol'] == 'X':
                    ai_sym = 'O'
                else:
                    ai_sym = 'X'
                if check_winner(board, ai_sym):
                    print(f'----------- {player["name"]} LOST! -----------')
                    playing = False
                elif is_board_full(board):
                    print(f'----------- GAME TIE! -----------')
                    playing = False
        if not continue_playing():
            break
    exit('Program Terminated...')
