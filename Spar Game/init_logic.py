import random

class GameInit:

    def __init__(self, p1_name=None, p2_name=None):
        self.p1_name = p1_name
        self.p2_name = p2_name


    def shuffled_cards(self):

        ranks = ['spades', 'clubs', 'hearts', 'diamonds']
        names = ['6', '7', '8', '9', '10', 'joker', 'queen', 'king']
        shuffled_list=[]

        for n in names:
            for r in ranks:
                shuffled_list.append(n + ' of ' + r)
        random.shuffle(shuffled_list)

        return shuffled_list
    

    def player_init(self):

        self.p1_name = input('Enter name for player 1: ')
        self.p2_name = input('Enter name for player 2: ')

        return self.p1, self.p2
    

    def card_init_dist(self):

        shuffled_list = self.shuffled_cards()
        p1_cards = []
        p2_cards = []
        p1_name, p2_name = self.player_init()

        for i in range(5):
            p1_cards.append(shuffled_list.pop())
            p2_cards.append(shuffled_list.pop())

        return p1_name, p1_cards, p2_name, p2_cards












