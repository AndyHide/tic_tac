field = [['-' for x in range(3)] for x in range(3)]

def print_field():
    print('  1 2 3')
    print(f'a {field[0][0]} {field[0][1]} {field[0][2]}')
    print(f'b {field[1][0]} {field[1][1]} {field[1][2]}')
    print(f'c {field[2][0]} {field[2][1]} {field[2][2]}')