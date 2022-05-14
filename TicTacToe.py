import time

print('''Welcome to the TIC TAC TOE game!!!''')

top_mod = ['  7  ', '||', '  8  ', '||', '  9  ']
middle_mod = ['  4  ', '||', '  5  ', '||', '  6  ']
bottom_mod = ['  1  ', '||', '  2  ', '||', '  3  ']
space1 = ['     ', '||', '     ', '||', '     ']
space2 = ['.....', '||', '.....', '||', '.....']

time.sleep(1)

print('Positions on the board are represented as shown below:')
time.sleep(1)
print((' '*20) + ''.join(space1))
print((' '*20) + ''.join(top_mod))
print((' '*20) + ''.join(space2))
print((' '*20) + ''.join(space1))
print((' '*20) + ''.join(middle_mod))
print((' '*20) + ''.join(space2))
print((' '*20) + ''.join(space1))
print((' '*20) + ''.join(bottom_mod))
print((' '*20) + ''.join(space1))


def play_action(value):
    if player == 1:
        if value == '1':
            bottom_list[2] = player1
        elif value == '2':
            bottom_list[9] = player1
        elif value == '3':
            bottom_list[16] = player1
        elif value == '4':
            mid_list[2] = player1
        elif value == '5':
            mid_list[9] = player1
        elif value == '6':
            mid_list[16] = player1
        elif value == '7':
            top_list[2] = player1
        elif value == '8':
            top_list[9] = player1
        elif value == '9':
            top_list[16] = player1

    elif player == 2:
        if value == '1':
            bottom_list[2] = player2
        elif value == '2':
            bottom_list[9] = player2
        elif value == '3':
            bottom_list[16] = player2
        elif value == '4':
            mid_list[2] = player2
        elif value == '5':
            mid_list[9] = player2
        elif value == '6':
            mid_list[16] = player2
        elif value == '7':
            top_list[2] = player2
        elif value == '8':
            top_list[9] = player2
        elif value == '9':
            top_list[16] = player2

    print((' '*20) + ''.join(space1))
    print((' '*20) + ''.join(top_list))
    print((' '*20) + ''.join(space2))
    print((' '*20) + ''.join(space1))
    print((' '*20) + ''.join(mid_list))
    print((' '*20) + ''.join(space2))
    print((' '*20) + ''.join(space1))
    print((' '*20) + ''.join(bottom_list))
    print((' '*20) + ''.join(space1))


play_condition = 'y'
while play_condition == 'y':
    top_list = [' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ']
    mid_list = [' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ']
    bottom_list = [' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ']
    list_values = []

    tile = input('Player 1, please select a tile for the game: X or O? ').upper()
    while tile != 'X' and tile != 'O':
        tile = input('Player 1, please select a valid tile for the game: X or O? ').upper()
    else:
        player1 = tile
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

        while True:
            player = 1
            value = input('Player 1, select the position you would like to play in: ')
            while value in list_values:
                value = input('That position is occupied already. Player 1, please select another position!')
            else:
                time.sleep(1)
                print((' '*20) + '......................')
                time.sleep(1)
                play_action(value)
                list_values.append(value)
                list_values.sort()
                if bottom_list[2] == mid_list[2] == top_list[2] == player1 or top_list[9] == mid_list[9] == bottom_list[
                    9] == player1 or top_list[16] == mid_list[16] == bottom_list[16] == player1 or top_list[2] == \
                        top_list[9] == top_list[16] == player1 or mid_list[2] == mid_list[9] == mid_list[16] == \
                        player1 or bottom_list[2] == bottom_list[9] == bottom_list[16] == player1 or top_list[2] == \
                        mid_list[9] == bottom_list[16] == player1 or bottom_list[2] == mid_list[9] == top_list[16] == \
                        player1:
                    print('Congratulations Player 1!! You have won the game!!!')
                    break
                elif list_values == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    print('The game ends in a stalemate!!!')
                    break
                else:
                    print(' ' * 100)

            player = 2
            value = input('Player 2, select the position you would like to play in: ')
            while value in list_values:
                value = input('That position is occupied already. Player 2, please select another position!')
            else:
                time.sleep(1)
                print((' '*20) + '......................')
                time.sleep(1)
                play_action(value)
                list_values.append(value)
                if bottom_list[2] == mid_list[2] == top_list[2] == player2 or top_list[9] == mid_list[9] == bottom_list[
                    9] == player2 or top_list[16] == mid_list[16] == bottom_list[16] == player2 or top_list[2] == \
                        top_list[9] == top_list[16] == player2 or mid_list[2] == mid_list[9] == mid_list[16] == \
                        player2 or bottom_list[2] == bottom_list[9] == bottom_list[16] == player2 or top_list[2] == \
                        mid_list[9] == bottom_list[16] == player2 or bottom_list[2] == mid_list[9] == top_list[16] == \
                        player2:
                    print('Congratulations Player 2!! You have won the game!!!')
                    break

        print(' ' * 100)
    play_condition = input('Would you like to play again? Y/N: ').lower()
