#!/usr/bin/env python3

from deck import Deck
from player import Player

player1 = Player("Player 1")
player2 = Player("Player 2")
deck = Deck()
deck.shuffle()

for x in range(len(deck) // 2):
    player1.add_cards(deck.deal_one())
    player2.add_cards(deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player1.all_cards) == 0:
        print("Player 1 ran out of cards. Player 2 won!")
        game_on = False
        break

    if len(player2.all_cards) == 0:
        print("Player 2 ran out of cards. Player 1 won!")
        game_on = False
        break

    player1_cards, player2_cards = [], []

    player1_cards.append(player1.remove_one())
    player2_cards.append(player2.remove_one())

    at_war = True

    while at_war:
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            at_war = False
        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            at_war = False
        else:
            print("WAR!")

            if len(player1.all_cards) < 5:
                print("Player 1 is unable to play war. Game over at war.")
                print("Player 2 won!")
                game_on = False
                break
            elif len(player2.all_cards) < 5:
                print("Player 2 is unable to play war. Game over at war.")
                print("Player 1 won!")
                game_on = False
                break
            else:
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())
