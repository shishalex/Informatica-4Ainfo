from carta import Card
from mano import Hand
from mazzo import Deck


class BlackjackTable:
    def __init__(self, player_hand: Hand, dealer_hand: Hand, ):
        self.__player_hand = player_hand
        self.__dealer_hand = dealer_hand
        self.__deck = self.__create_deck()
        self.__deck.shuffle_deck()

    def __create_deck(self) -> Deck:
        seeds = ['C', 'D', 'H', 'S']  # Clubs, Diamonds, Hearts, Spades
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        return Deck([Card(seed, rank) for seed in seeds for rank in ranks])

    def game(self):
        return

    def __points_calculator(self, hand: Hand) -> int:
        cards = hand.cards()
        points = 0

        for card in cards:
            if points >= 11:
                if card == "A":
                    points += 1
            points += card.value
        return points


    def __player_turn(self):
        return

    def __dealer_turn(self):
        return