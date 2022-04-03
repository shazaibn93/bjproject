print("Club -> \u2663")
print("Spades -> \u2660")
print("Diamond -> \u2666")
print("Heart -> \u2665")

import random
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

sum_cards = 0

cards = {
    '\u2663A':11 if sum_cards<21 else 1,
    '\u2663K':10,
    '\u2663Q':10,
    '\u2663J':10,
    '\u266310':10,
    '\u26639':9,
    '\u26638':8,
    '\u26637':7,
    '\u26636':6,
    '\u26635':5,
    '\u26634':4,
    '\u26633':3,
    '\u26632':2,
    '\u2660A':11 if sum_cards<21 else 1,
    '\u2660K':10,
    '\u2660Q':10,
    '\u2660J':10,
    '\u266010':10,
    '\u26609':9,
    '\u26608':8,
    '\u26607':7,
    '\u26606':6,
    '\u26605':5,
    '\u26604':4,
    '\u26603':3,
    '\u26602':2,
    '\u2666A':11 if sum_cards<21 else 1,
    '\u2666K':10,
    '\u2666Q':10,
    '\u2666J':10,
    '\u266610':10,
    '\u26669':9,
    '\u26668':8,
    '\u26667':7,
    '\u26666':6,
    '\u26665':5,
    '\u26664':4,
    '\u26663':3,
    '\u26662':2,
    '\u2665A':11 if sum_cards<21 else 1,
    '\u2665K':10,
    '\u2665Q':10,
    '\u2665J':10,
    '\u266510':10,
    '\u26659':9,
    '\u26658':8,
    '\u26657':7,
    '\u26656':6,
    '\u26655':5,
    '\u26654':4,
    '\u26653':3,
    '\u26652':2,
    }


shuffled_deck = list(cards.keys())
random.shuffle(shuffled_deck)


dsum_list = []
dealer_cards = []


psum_list = []
player_cards = []



class Dealer():
    
    def __init__ (self):
        self.dsum = 0
        self.dcards = {}

    def dhand(self):
        
        dealer_cards.append(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
        dealer_cards.append(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
                
                
                
    def dscore(self):
        for k, v in cards.items():
            if k in dealer_cards:
                self.dsum = 0
                dsum_list.append(v)
                
        self.dsum = sum(dsum_list)

    
        

class Player():
    
    def __init__ (self, player):
        self.psum = 0
        self.pcards = {}
        self.player = player

    def phand(self):
       
        player_cards.append(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
        player_cards.append(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
                
               

    def pscore(self):
        for k, v in cards.items():
            if k in player_cards:
                self.psum = 0
                psum_list.append(v)
        self.psum = sum(psum_list)
        

class UI(Player, Dealer):
    def __init__ (self):
        self.player = Player
        self.dealer = Dealer
  
    def hit(self):
        Dealer.dhand(self) 
        Dealer.dscore(self) 
        Player.phand(self) 
        Player.pscore(self) 


        while True:
            
            print("Dealer's Cards:")
            print(f'[ ] [{dealer_cards[1]}]')
            print('\n')
            print("Your Cards:")
            print(player_cards)
            print(f'Your Cards = {self.psum}')
            hit = input("Would you like to HIT/STAY? ")
            if hit.lower() == 'stay':

                
                clear_screen()

                print(dealer_cards)
                print(f"Dealer's cards = {self.dsum}")
                print('\n')
                print(player_cards)
                print(f"Your cards = {self.psum}")

                while self.dsum < 17:
                    dealer_cards.append(shuffled_deck[0])
                    shuffled_deck.remove(shuffled_deck[0])
                    dsum_list.clear()
                    Dealer.dscore(self)
                    print(f'dsum_list = {dsum_list}')
                    print("Dealer's Cards:")
                    print(dealer_cards)
                    print(self.dsum)
                    print("Player's Cards:")
                    print(player_cards)
                    print(self.psum)
                break

                
            elif hit.lower() == 'hit':
                clear_screen()
                player_cards.append(shuffled_deck[0])
                shuffled_deck.remove(shuffled_deck[0])
                psum_list.clear()
                Player.pscore(self)
            else:
                print('Invalid Response')

    def results(self):
        while True:

            if self.psum > 21:
                clear_screen()
                print(f"Your cards = {self.psum} Dealer cards = {self.dsum}")
                print("Dealer's Cards:")
                print(dealer_cards)
                print("Player's Cards:")
                print(player_cards)
                print("YOU LOSE!")
                dsum_list.clear()
                psum_list.clear()
                dealer_cards.clear()
                player_cards.clear()
                break

            elif self.dsum > 21:
                clear_screen()
                print(f"Your cards = {self.psum} Dealer cards = {self.dsum}")
                print("Dealer's Cards:")
                print(dealer_cards)
                print("Player's Cards:")
                print(player_cards)
                print("YOU WIN!")
                print(dsum_list)
                dsum_list.clear()
                psum_list.clear()
                dealer_cards.clear()
                player_cards.clear()
                break

            
            
            
            elif self.psum > self.dsum:
                clear_screen()
                print(f"Your cards = {self.psum} Dealer cards = {self.dsum}")
                print("Dealer's Cards:")
                print(dealer_cards)
                print("Player's Cards:")
                print(player_cards)
                print("YOU WIN!")
                dsum_list.clear()
                psum_list.clear()
                dealer_cards.clear()
                player_cards.clear()
                break
            elif self.psum <= self.dsum:
                clear_screen()
                print(f"Your cards = {self.psum} Dealer cards = {self.dsum}")
                print("Dealer's Cards:")
                print(dealer_cards)
                print("Player's Cards:")
                print(player_cards)
                print("YOU LOSE!")
                dsum_list.clear()
                psum_list.clear()
                dealer_cards.clear()
                player_cards.clear()
                break


    


    def game(self):
        while True:
            start_response = input('Do you want to BLACK JACK? Y/N ')
            if start_response.lower() == 'y':
               
                self.hit()
                self.results()
                
            elif start_response.lower() == 'n':
                break
            else:
                print("Invalid Response, just 1 letter")

run = UI()
run.game()