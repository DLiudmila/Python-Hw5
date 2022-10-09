# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?    
#     a) Добавьте игру против бота    
#     b) Подумайте как наделить бота "интеллектом"    

from random import randint

def getCandyNumber(name, totalCandies, isBotMove):
    print(name, ', ваш ход')
    if isBotMove:
        # 'логика :)'
        if totalCandies < 29:
            count = totalCandies
        else:
            count = randint(1, totalCandies+1)
        print(name, 'взял', count)
        return count
    count = 0
    count = int(input("Сколькоф конфет вы возмёте: "))
    while count < 1 or count > 28 or count > totalCandies:
        print('Неверное количество конфет за один раз -', count)
        if totalCandies < 28:
            print('Можно взять от 1 до', totalCandies)
        else:
            print('Можно взять от 1 до 28')
        count = int(input("Ввведите cколько конфет вы возмёте: "))
    return count

def checkResults(name, total, taken, isBotMove):
    total = total - taken
    print('осталось конфет', total)
    if total < 1:
        if isBotMove:
            print(name, ', выиграл !')    
        else:
            print(name, ', поздравляем, вы победили !')
        exit(0)
    return total


counter = 55
print('Правила:')
print('1. Всего конфет в начале - ', counter, 'шт')
print('2. Игроки ходят по очереди')
print('3. За один ход можно забрать не более чем 28 конфет')
print('4. Побеждает взявший последние конфеты')

playerNames = ['', '']*2
playerNames[0] = input("Введите имя первого игрока: ")
isBot = bool(input("Хотите поиграть с ботом (0 - нет; 1 - да): "))
if isBot == 1:
    playerNames[1] = 'Бот Вася'
else:
    playerNames[1] = input("Введите имя второго игрока: ")

# print("игрок1 - это", player1)
moveOfFirsrstPlayer = randint(0, 100)%2
moverOfSecondPlayer = 1 - moveOfFirsrstPlayer

print('осталось конфет', counter)
while counter > 0:
    move = 0
    count = getCandyNumber(playerNames[moveOfFirsrstPlayer], counter, (isBot and move == moverOfSecondPlayer))
    counter = checkResults(playerNames[moveOfFirsrstPlayer], counter, count, (isBot and move == moverOfSecondPlayer))
    
    move = 1
    count = getCandyNumber(playerNames[moverOfSecondPlayer], counter, (isBot and move == moverOfSecondPlayer))
    counter = checkResults(playerNames[moverOfSecondPlayer], counter, count, (isBot and move == moverOfSecondPlayer))
