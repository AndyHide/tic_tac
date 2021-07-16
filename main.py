field = [['-' for j in range(3)] for i in range(3)]
keys = {'a': 0, 'b': 1, 'c': 2}


def print_field():
    print('  1 2 3')
    print(f'a {field[0][0]} {field[0][1]} {field[0][2]}')
    print(f'b {field[1][0]} {field[1][1]} {field[1][2]}')
    print(f'c {field[2][0]} {field[2][1]} {field[2][2]}')


def make_move(move, player):
    """This function checks if move is valid and applies it to the field."""
    if len(move) != 2 \
            or move[0] not in 'abc' \
            or move[1] not in '123' \
            or player not in 'XO' \
            or field[keys[move[0]]][int(move[1]) - 1] != '-':
        return False
    field[keys[move[0]]][int(move[1]) - 1] = player
    return True


def player_move(current_player):
    """This function draws field, then asks player to input his move. Then it passes result to make_move function."""
    print_field()
    print(f"""Now {current_player}'s turn""")
    print(f"Input cell address in 'a1' format:")
    while True:
        move = input()
        if make_move(move, current_player):
            break
        print('Invalid move, try again')
    return 0


def check_victory(current_player):
    """This function checks if current player won the game."""
    for i in range(3):
        if field[i][0] == current_player and field[i][1] == current_player and field[i][2] == current_player:
            return True
        if field[0][i] == current_player and field[1][i] == current_player and field[2][i] == current_player:
            return True
    if field[0][0] == current_player and field[1][1] == current_player and field[2][2] == current_player:
        return True
    if field[0][2] == current_player and field[1][1] == current_player and field[2][0] == current_player:
        return True
    return False


if __name__ == '__main__':
    current_player = 'X'

    print('Lets play Tic Tac Toe!')
    while True:
        player_move(current_player)
        if check_victory(current_player):
            print(f'Congratulations! Player {current_player} is a winner!')
            print_field()
            break
        current_player = 'O' if current_player == 'X' else 'X'
