from random import shuffle


class Deck:
    def __init__(self, deck: list):
        self.__deck = deck

    def shuffle_deck(self) -> None:
        shuffle(self.__deck)

    def pick(self):
        if len(self.__deck) == 0:
            raise IndexError("Il deck è vuoto!")
        return self.__deck.pop()