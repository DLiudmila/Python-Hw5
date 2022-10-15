# Создайте программу для игры в "Крестики-нолики".

# Игровое поле
from operator import concat


def draw_board(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-' * 13)

# Запрашиваем ход
def take_input(player_token):
    valid = False
    while not valid:
        print('Куда поставим', player_token, '?')
        player_answer = input()
        try:
            player_answer = int(player_answer)
        except:
            print('Вводить нужно числа от 1 до 9')
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer-1]) not in 'ХО':
               board[player_answer-1] = player_token
               valid =True
            else:
                print('Эта клетка уже занята')
        else:
            print('Вводить нужно числа от 1 до 9')

# Проверка победы
def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter+= 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'Победили!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    draw_board(board)

# if __name__ == '__main__':
print("Игра Крестики-нолики для двух игроков")
board = list(range(1, 10))

main(board)
input("Нажмите Enter для выхода!")