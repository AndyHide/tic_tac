field = [['-' for j in range(3)] for i in range(3)]
keys = {'a' : 0, 'b' : 1, 'c' : 2}


def print_field():
    print('  1 2 3')
    print(f'a {field[0][0]} {field[0][1]} {field[0][2]}')
    print(f'b {field[1][0]} {field[1][1]} {field[1][2]}')
    print(f'c {field[2][0]} {field[2][1]} {field[2][2]}')


def make_move(move, player):
    if len(move) != 2 \
            or move[0] not in 'abc' \
            or move[1] not in '123' \
            or player not in 'XO'\
            or field[keys[move[0]]][int(move[1])-1] != '-':
        return 'Invalid Move'
    field[keys[move[0]]][int(move[1])-1] = player
    return 0


def player_move(current_player):
    pass


def check_victory(current_player):
    pass


if __name__ == '__main__':
    current_player = 'X'

    print('Lets play Tic Tac Toe!')
    while True:
        player_move(current_player)
        if check_victory(current_player):
            break
        current_player = 'O' if current_player == 'X' else current_player = 'X'
