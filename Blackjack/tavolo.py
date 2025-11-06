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
        for i in range(2):
            self.__player_hand.add_card(self.__deck.pick())
            self.__dealer_hand.add_card(self.__deck.pick())


    def __points_calculator(self, hand: Hand) -> int:
        cards = hand.cards()
        points = 0

        for card in cards:
            if points >= 11:
                if card == "A":
                    points += 1
            points += card.value
        return points


    def __player_turn(self) -> None:
        while True:
            choice = input("Chiedi (C) o Stai (S)?")
            choice.upper()
            if choice != "S" and choice != "C":
                print("La scelta non è valida!")
                continue
            if choice == "S":
                break
            if choice == "C":
                self.__player_hand.add_card(self.__deck.pick())

    def __dealer_turn(self) -> None:
        while True:
            if self.__points_calculator(self.__dealer_hand) >= 16:
                break
            else:
                self.__dealer_hand.add_card(self.__deck.pick())
