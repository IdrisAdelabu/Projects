"""
This code is for the game BLACKJACK
"""
import random
import time


class Profile:
    """
    DOCSTRING: This class is created for the game of Blackjack, also known as 21.
    """
    A = 'A'
    J = 'J'
    K = 'K'
    Q = 'Q'

    def __init__(self, amount, data='Dealer'):
        self.data = data
        self.amount = amount

    def __str__(self):
        return f'{self.data} has {self.amount} naira.'

    def deck(self, records):
        """
        DOCSTRING: this function returns a card chosen at random from a deck of cards.
        :return: card string
        """

        num_list = [Profile.A, 2, 3, 4, 5, 6, 7, 8, 9, Profile.J, Profile.K, Profile.Q]
        shape_list = ['♠', '♥', '♦', '♣']

        if not records:
            card_num = random.choice(num_list)
            card_shape = random.choice(shape_list)

        else:
            card_num = random.choice(num_list)
            card_shape = random.choice(shape_list)

            while (card_num, card_shape) in records:
                card_num = random.choice(num_list)
                card_shape = random.choice(shape_list)

        tup_it = (card_num, card_shape)
        return tup_it

    def card_deck(self, tup_it):
        card_num = tup_it[0]
        card_shape = tup_it[1]

        card = f'''
          _____
         |{card_num}    |
         |{card_shape}    |
         |    {card_shape}|
         |____{card_num}|
        '''
        records.append(tup_it)
        return card

    def turn_record(self, turn, card, tup_it, i):

        if turn == player:
            if i == 1:
                if tup_it[0] == Profile.A:
                    player.append('hold')

                elif tup_it[0] == Profile.J:
                    player.append(10)

                elif tup_it[0] == Profile.K:
                    player.append(10)

                elif tup_it[0] == Profile.Q:
                    player.append(10)

                else:
                    player.append(tup_it[0])

            else:
                if 'hold' in player:
                    damp = player.index('hold')
                    decide = int(input("select a value for 'A', 1 or 11? "))
                    player[damp] = decide

                else:
                    if tup_it[0] == Profile.A:

                        decide = int(input("select a value for 'A', 1 or 11? "))
                        player.append(decide)

                    elif tup_it[0] == Profile.J:
                        player.append(10)

                    elif tup_it[0] == Profile.K:
                        player.append(10)

                    elif tup_it[0] == Profile.Q:
                        player.append(10)

                    else:
                        player.append(tup_it[0])

            rec_player.append(card)
        elif turn == dealer:
            if tup_it[0] == Profile.A:
                if sum(dealer) + 11 <= 21:
                    dealer.append(11)
                else:
                    dealer.append(1)

            elif tup_it[0] == Profile.J:
                dealer.append(10)

            elif tup_it[0] == Profile.K:
                dealer.append(10)

            elif tup_it[0] == Profile.Q:
                dealer.append(10)

            else:
                dealer.append(tup_it[0])

            rec_dealer.append(card)
        return None

    def game_check(self, turn, amount, player, dealer, i):

        if turn == player:
            if sum(player) > 21:
                scond = False
                statement = "BUSTED!!! You have exceeded 21 and lost the game."
                hit_again = 'no'
                return (scond, statement, hit_again)

            elif sum(player) == 21:
                scond = False
                if sum(dealer) == 21:
                    statement = 'This game is a tie!!'

                else:
                    amount *= 1.5
                    statement = f"CONGRATULATIONS!!! You have won the game!\nYour new balance is {amount}"
                hit_again = 'no'
                return (scond, statement, hit_again)
            else:
                scond = True
                statement = 'L'
                if i == 3:
                    hit_again = input('would you like to receive another card? Y/N ').lower()

                else:
                    hit_again = None
                return (scond, statement, hit_again)

        elif turn == dealer:

            if sum(dealer) > 21:
                scond = False
                amount *= 1.5
                statement = f"CONGRATULATIONS {name}! Dealer has busted and you have won the game!\nYour new balance is \
                    {amount}"
                hit_again = None
                return (scond, statement, hit_again)

            elif sum(dealer) == 21:
                scond = False
                if sum(player) == 21:
                    statement = 'This game is a tie!!'
                else:
                    statement = 'BUSTED!! Dealer wins!'
                hit_again = None
                return (scond, statement, hit_again)

            else:
                scond = None
                statement = None
                hit_again = None
                return (scond, statement, hit_again)


print('WELCOME TO THE ROYAL FLAME CASINO!!!')
name = input('PLEASE ENTER YOUR FULL NAME: ').upper()
amount = int(input('HOW MUCH WOULD YOU LIKE TO BET? '))
blank_card = f'''
      _____
     |     |
     |     |
     |     |
     |_____|
    '''

repeat = 'yes'

while repeat in ['yes', 'y']:
    records = []
    player = []
    dealer = []
    rec_player = []
    rec_dealer = []
    cond = True
    i = 0
    while cond and i <= 3:

        i += 1

        for turn in [player, dealer]:

            if cond and i <= 2:
                if turn == player:
                    card_play = Profile(amount, name)
                    card1 = card_play.deck(records)
                    Card = card_play.card_deck(card1)
                    card_play.turn_record(player, Card, card1, i)
                    player_str = '   '.join(rec_player)
                    print(f'Player card deck contains:\n{player_str}')
                elif turn == dealer:
                    if i == 1:
                        card_play = Profile(amount)
                        card1 = card_play.deck(records)
                        Card = card_play.card_deck(card1)
                        card_play.turn_record(dealer, Card, card1, i)
                        dealer_str = '   '.join(rec_dealer)
                        print(f'Dealer card deck contains:\n{dealer_str}')
                    else:
                        dealer_str = '   '.join(rec_dealer)
                        print(f'Dealer card deck contains:{dealer_str}\n{blank_card}')
                        card_play = Profile(amount)
                        card1 = card_play.deck(records)
                        Card = card_play.card_deck(card1)
                        card_play.turn_record(dealer, Card, card1, i)

                gamer = card_play.game_check(turn, amount, player, dealer, i)
                cond = gamer[0]
                statement1 = gamer[1]
                print(statement1)

            elif cond and i > 2:
                if turn == player:
                    hit = input('would you like to receive another card? Y/N ').lower()
                    while hit in ['y', 'yes']:
                        card_play = Profile(amount, name)
                        card1 = card_play.deck(records)
                        Card = card_play.card_deck(card1)
                        card_play.turn_record(player, Card, card1, i)
                        player_str = '   '.join(rec_player)
                        print(f'Player card deck contains:\n{player_str}')
                        gamer = card_play.game_check(turn, amount, player, dealer, i)
                        cond = gamer[0]
                        statement1 = gamer[1]
                        hit = gamer[2]
                        print(statement1)

                elif turn == dealer:
                    dealer_str = '   '.join(rec_dealer)
                    print(f'Dealer card deck fully revealed contains:\n{dealer_str}')
                    while cond:
                        card_play = Profile(amount)
                        card1 = card_play.deck(records)
                        Card = card_play.card_deck(card1)
                        card_play.turn_record(dealer, Card, card1, i)
                        dealer_str = '   '.join(rec_dealer)
                        print(f'Dealer card deck contains:\n{dealer_str}')
                        gamer = card_play.game_check(turn, amount, player, dealer, i)
                        cond = gamer[0]
                        statement1 = gamer[1]
                        print(statement1)
            time.sleep(1)

    repeat = input("would you like to play again? Y/N: ").lower()

else:
    print('PLEASE COME BACK AGAIN ❤')


