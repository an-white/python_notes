# aplicacion de diccionarios y ciclos para armar un juego sencillo

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


printBoard(board)
t = 'X'
for i in range(9):
    print('\nTurno para ' + t + ', en que posicion desea jugar\n')
    pos = input()
    if board[pos] == 'X' or board[pos] == 'O':
        print('Debe colocarse en una posicion vacia\n')
        printBoard(board)
    else:
        board[pos] = t
        if t == 'X':
            t = 'O'
        else:
            t = 'X'
        printBoard(board)
