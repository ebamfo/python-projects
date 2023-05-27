from init_logic import GameInit
import random

class MainGameLogic:

    def __init__(self):
        
        game_init = GameInit()
        self.p1_name, self.p1_cards, self.p2_name, self.p2_cards = game_init.card_init_dist()
        self.player_turn=None
        self.player_details = [[1, self.p1, self.p1_cards],[1, self.p2, self.p2_cards]]
        self.p1_played_cards, self.p2_played_cards = [],[]
        

    ##Chooses randomly which player starts, player_turn var is TRUE for player 1 and false for player 2
    def player_start(self):
        if random.randint(1,2)==1:
            self.player_turn=True
        else:
            self.player_turn=False
       
    

    ##player_start function has to be passed here
    ##This function shows curren
    def play_card(self):
        ##If Player 1 turn
        if self.player_turn==True:
            print(f'{self.p1_cards}\n')
            selected_card=int(input('Choose card from above, 1 for beginning: '))-1
            self.p1_played_cards.append(self.p1_cards.pop(selected_card))

        ##If Player 2 turn
        else:
            print(f'{self.p2_cards}\n')
            selected_card=int(input('Choose card from above, 1 for beginning: '))-1
            self.p2_played_cards.append(self.p2_cards.pop(selected_card))

            

            


